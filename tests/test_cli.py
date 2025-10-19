"""Tests for CLI functionality."""

import tempfile
from pathlib import Path

import pytest
from typer.testing import CliRunner

from microforge.cli import app

runner = CliRunner()


def test_version_command() -> None:
    """Test version command."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "Microforge version" in result.stdout


def test_new_command_basic() -> None:
    """Test basic new command."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = runner.invoke(app, ["new", "testservice"], cwd=tmpdir)
        assert result.exit_code == 0
        assert "Successfully created project" in result.stdout
        
        # Check that project directory was created
        project_path = Path(tmpdir) / "testservice"
        assert project_path.exists()
        assert (project_path / "app").exists()
        assert (project_path / "worker").exists()
        assert (project_path / "tests").exists()


def test_new_command_with_options() -> None:
    """Test new command with all options."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = runner.invoke(
            app,
            [
                "new",
                "testservice",
                "--db",
                "postgres",
                "--broker",
                "redis",
                "--ci",
                "github",
                "--auth",
                "oauth2",
            ],
            cwd=tmpdir,
        )
        assert result.exit_code == 0
        
        project_path = Path(tmpdir) / "testservice"
        assert project_path.exists()
        assert (project_path / "app" / "db").exists()
        assert (project_path / "app" / "auth").exists()


def test_new_command_existing_directory() -> None:
    """Test new command with existing directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create directory first
        project_path = Path(tmpdir) / "testservice"
        project_path.mkdir()
        
        result = runner.invoke(app, ["new", "testservice"], cwd=tmpdir)
        assert result.exit_code == 1
        assert "already exists" in result.stdout


def test_new_command_invalid_broker() -> None:
    """Test new command with invalid broker."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = runner.invoke(
            app, ["new", "testservice", "--broker", "invalid"], cwd=tmpdir
        )
        assert result.exit_code == 1
        assert "broker must be" in result.stdout


def test_new_command_invalid_ci() -> None:
    """Test new command with invalid CI provider."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = runner.invoke(
            app, ["new", "testservice", "--ci", "invalid"], cwd=tmpdir
        )
        assert result.exit_code == 1
        assert "ci must be" in result.stdout

