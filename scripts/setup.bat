@echo off
REM Setup script for Microforge development (Windows)

echo 🔥 Setting up Microforge development environment...

REM Check if Poetry is installed
poetry --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Poetry is not installed. Please install Poetry first:
    echo    curl -sSL https://install.python-poetry.org | python3 -
    exit /b 1
)

REM Install dependencies
echo 📦 Installing dependencies...
poetry install

REM Run tests
echo 🧪 Running tests...
poetry run pytest

REM Run linting
echo 🔍 Running linters...
poetry run black --check .
poetry run ruff check .
poetry run mypy microforge

echo ✅ Setup complete! You can now:
echo    - Run tests: poetry run pytest
echo    - Format code: poetry run black .
echo    - Lint code: poetry run ruff check .
echo    - Test CLI: poetry run microforge --help
echo    - Generate project: poetry run microforge new testproject
