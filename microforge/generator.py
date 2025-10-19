"""Project generator logic."""

import subprocess
from pathlib import Path
from typing import Any, Dict, Optional

from jinja2 import Environment, PackageLoader, select_autoescape  # type: ignore

from microforge.config import TEMPLATE_CONFIG


class ProjectGenerator:
    """Generates a microservice project from templates."""

    def __init__(
        self,
        name: str,
        path: Path,
        db: Optional[str] = None,
        broker: str = "redis",
        ci: str = "azure",
        auth: Optional[str] = None,
        git_init: bool = False,
    ) -> None:
        """Initialize the project generator.

        Args:
            name: Project name
            path: Path where project will be created
            db: Database choice (postgres or None)
            broker: Message broker (redis or kafka)
            ci: CI/CD provider (azure, github, or gitlab)
            auth: Authentication type (oauth2 or None)
            git_init: Whether to initialize Git repository
        """
        self.name = name
        self.path = path
        self.db = db
        self.broker = broker
        self.ci = ci
        self.auth = auth
        self.git_init = git_init

        self.env = Environment(
            loader=PackageLoader("microforge", "templates"),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def get_context(self) -> Dict[str, Any]:
        """Get template context."""
        return {
            "project_name": self.name,
            "project_slug": self.name.lower().replace("-", "_").replace(" ", "_"),
            "db": self.db,
            "broker": self.broker,
            "ci": self.ci,
            "auth": self.auth,
            "has_db": self.db is not None,
            "has_auth": self.auth is not None,
            "use_postgres": self.db == "postgres",
            "use_redis": self.broker == "redis",
            "use_kafka": self.broker == "kafka",
            "use_azure": self.ci == "azure",
            "use_github": self.ci == "github",
            "use_gitlab": self.ci == "gitlab",
            "use_oauth2": self.auth == "oauth2",
        }

    def generate(self) -> None:
        """Generate the project structure."""
        context = self.get_context()

        # Create directory structure
        self._create_directories()

        # Generate files from templates
        self._generate_files(context)

        # Initialize Git if requested
        if self.git_init:
            self._init_git()

    def _create_directories(self) -> None:
        """Create project directory structure."""
        dirs = [
            self.path,
            self.path / "app",
            self.path / "app" / "routes",
            self.path / "app" / "core",
            self.path / "worker",
            self.path / "tests",
            self.path / "helm",
            self.path / "helm" / "templates",
        ]

        if self.db:
            dirs.append(self.path / "app" / "db")

        if self.auth:
            dirs.append(self.path / "app" / "auth")

        for directory in dirs:
            directory.mkdir(parents=True, exist_ok=True)

    def _generate_files(self, context: Dict[str, Any]) -> None:
        """Generate files from templates."""
        # Get file list from config
        files = TEMPLATE_CONFIG["files"]

        for file_config in files:
            template_name = file_config["template"]
            output_path = self.path / file_config["output"]

            # Check conditions
            if "condition" in file_config:
                condition = file_config["condition"]
                if not self._evaluate_condition(condition, context):
                    continue

            # Render template
            template = self.env.get_template(template_name)
            content = template.render(**context)

            # Write file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(content, encoding="utf-8")

    def _evaluate_condition(self, condition: str, context: Dict[str, Any]) -> bool:
        """Evaluate a condition string."""
        # Simple condition evaluation
        # Supports: has_db, has_auth, use_postgres, use_redis, etc.
        return bool(context.get(condition, False))

    def _init_git(self) -> None:
        """Initialize Git repository."""
        try:
            subprocess.run(
                ["git", "init"],
                cwd=self.path,
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError:
            # Git init failed, but don't fail the entire generation
            pass

