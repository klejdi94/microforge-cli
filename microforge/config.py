"""Configuration for template generation."""

from typing import Any, Dict, List

# Template configuration mapping
TEMPLATE_CONFIG: Dict[str, List[Dict[str, Any]]] = {
    "files": [
        # Root files
        {"template": "pyproject.toml.j2", "output": "pyproject.toml"},
        {"template": "README.md.j2", "output": "README.md"},
        {"template": "gitignore.j2", "output": ".gitignore"},
        {"template": "Dockerfile.j2", "output": "Dockerfile"},
        {"template": "docker-compose.yml.j2", "output": "docker-compose.yml"},
        {"template": ".dockerignore.j2", "output": ".dockerignore"},
        # App files
        {"template": "app/main.py.j2", "output": "app/main.py"},
        {"template": "app/__init__.py.j2", "output": "app/__init__.py"},
        {"template": "app/routes/__init__.py.j2", "output": "app/routes/__init__.py"},
        {"template": "app/routes/health.py.j2", "output": "app/routes/health.py"},
        {"template": "app/core/__init__.py.j2", "output": "app/core/__init__.py"},
        {"template": "app/core/config.py.j2", "output": "app/core/config.py"},
        {"template": "app/core/logging.py.j2", "output": "app/core/logging.py"},
        {"template": "app/core/telemetry.py.j2", "output": "app/core/telemetry.py"},
        # Worker files
        {"template": "worker/__init__.py.j2", "output": "worker/__init__.py"},
        {"template": "worker/worker.py.j2", "output": "worker/worker.py"},
        # Test files
        {"template": "tests/__init__.py.j2", "output": "tests/__init__.py"},
        {"template": "tests/test_health.py.j2", "output": "tests/test_health.py"},
        {"template": "tests/conftest.py.j2", "output": "tests/conftest.py"},
        # Helm files
        {"template": "helm/Chart.yaml.j2", "output": "helm/Chart.yaml"},
        {"template": "helm/values.yaml.j2", "output": "helm/values.yaml"},
        {
            "template": "helm/templates/deployment.yaml.j2",
            "output": "helm/templates/deployment.yaml",
        },
        {
            "template": "helm/templates/service.yaml.j2",
            "output": "helm/templates/service.yaml",
        },
        # CI/CD files
        {
            "template": "ci/azure-pipelines.yml.j2",
            "output": "azure-pipelines.yml",
            "condition": "use_azure",
        },
        {
            "template": "ci/github-workflows.yml.j2",
            "output": ".github/workflows/ci.yml",
            "condition": "use_github",
        },
        {
            "template": "ci/gitlab-ci.yml.j2",
            "output": ".gitlab-ci.yml",
            "condition": "use_gitlab",
        },
        # Database files
        {
            "template": "app/db/__init__.py.j2",
            "output": "app/db/__init__.py",
            "condition": "has_db",
        },
        {
            "template": "app/db/database.py.j2",
            "output": "app/db/database.py",
            "condition": "has_db",
        },
        {
            "template": "app/db/models.py.j2",
            "output": "app/db/models.py",
            "condition": "has_db",
        },
        # Auth files
        {
            "template": "app/auth/__init__.py.j2",
            "output": "app/auth/__init__.py",
            "condition": "has_auth",
        },
        {
            "template": "app/auth/oauth2.py.j2",
            "output": "app/auth/oauth2.py",
            "condition": "use_oauth2",
        },
    ]
}

