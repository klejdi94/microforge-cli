#!/bin/bash
# Setup script for Microforge development

set -e

echo "🔥 Setting up Microforge development environment..."

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry is not installed. Please install Poetry first:"
    echo "   curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
poetry install

# Install pre-commit hooks (if available)
if command -v pre-commit &> /dev/null; then
    echo "🔧 Installing pre-commit hooks..."
    poetry run pre-commit install
fi

# Run tests
echo "🧪 Running tests..."
poetry run pytest

# Run linting
echo "🔍 Running linters..."
poetry run black --check .
poetry run ruff check .
poetry run mypy microforge

echo "✅ Setup complete! You can now:"
echo "   - Run tests: poetry run pytest"
echo "   - Format code: poetry run black ."
echo "   - Lint code: poetry run ruff check ."
echo "   - Test CLI: poetry run microforge --help"
echo "   - Generate project: poetry run microforge new testproject"
