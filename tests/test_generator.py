"""Tests for project generator."""

import tempfile
from pathlib import Path

import pytest

from microforge.generator import ProjectGenerator


def test_generator_basic() -> None:
    """Test basic project generation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = Path(tmpdir) / "testservice"
        
        generator = ProjectGenerator(
            name="testservice",
            path=project_path,
        )
        generator.generate()
        
        # Check directory structure
        assert project_path.exists()
        assert (project_path / "app").exists()
        assert (project_path / "app" / "main.py").exists()
        assert (project_path / "app" / "routes").exists()
        assert (project_path / "app" / "core").exists()
        assert (project_path / "worker").exists()
        assert (project_path / "worker" / "worker.py").exists()
        assert (project_path / "tests").exists()
        assert (project_path / "helm").exists()
        assert (project_path / "Dockerfile").exists()
        assert (project_path / "docker-compose.yml").exists()
        assert (project_path / "pyproject.toml").exists()
        assert (project_path / "README.md").exists()


def test_generator_with_database() -> None:
    """Test project generation with database."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = Path(tmpdir) / "testservice"
        
        generator = ProjectGenerator(
            name="testservice",
            path=project_path,
            db="postgres",
        )
        generator.generate()
        
        # Check database files
        assert (project_path / "app" / "db").exists()
        assert (project_path / "app" / "db" / "database.py").exists()
        assert (project_path / "app" / "db" / "models.py").exists()


def test_generator_with_auth() -> None:
    """Test project generation with authentication."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = Path(tmpdir) / "testservice"
        
        generator = ProjectGenerator(
            name="testservice",
            path=project_path,
            auth="oauth2",
        )
        generator.generate()
        
        # Check auth files
        assert (project_path / "app" / "auth").exists()
        assert (project_path / "app" / "auth" / "oauth2.py").exists()


def test_generator_with_kafka() -> None:
    """Test project generation with Kafka."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = Path(tmpdir) / "testservice"
        
        generator = ProjectGenerator(
            name="testservice",
            path=project_path,
            broker="kafka",
        )
        generator.generate()
        
        # Check that docker-compose has Kafka
        docker_compose = (project_path / "docker-compose.yml").read_text()
        assert "kafka" in docker_compose


def test_generator_ci_azure() -> None:
    """Test project generation with Azure CI."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = Path(tmpdir) / "testservice"
        
        generator = ProjectGenerator(
            name="testservice",
            path=project_path,
            ci="azure",
        )
        generator.generate()
        
        assert (project_path / "azure-pipelines.yml").exists()


def test_generator_ci_github() -> None:
    """Test project generation with GitHub CI."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = Path(tmpdir) / "testservice"
        
        generator = ProjectGenerator(
            name="testservice",
            path=project_path,
            ci="github",
        )
        generator.generate()
        
        assert (project_path / ".github" / "workflows" / "ci.yml").exists()


def test_generator_ci_gitlab() -> None:
    """Test project generation with GitLab CI."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = Path(tmpdir) / "testservice"
        
        generator = ProjectGenerator(
            name="testservice",
            path=project_path,
            ci="gitlab",
        )
        generator.generate()
        
        assert (project_path / ".gitlab-ci.yml").exists()


def test_generator_context() -> None:
    """Test generator context creation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = Path(tmpdir) / "testservice"
        
        generator = ProjectGenerator(
            name="My Test Service",
            path=project_path,
            db="postgres",
            broker="redis",
            ci="github",
            auth="oauth2",
        )
        
        context = generator.get_context()
        
        assert context["project_name"] == "My Test Service"
        assert context["project_slug"] == "my_test_service"
        assert context["db"] == "postgres"
        assert context["broker"] == "redis"
        assert context["ci"] == "github"
        assert context["auth"] == "oauth2"
        assert context["has_db"] is True
        assert context["has_auth"] is True
        assert context["use_postgres"] is True
        assert context["use_redis"] is True
        assert context["use_github"] is True
        assert context["use_oauth2"] is True

