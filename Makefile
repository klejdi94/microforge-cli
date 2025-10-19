# Makefile for Microforge development

.PHONY: install test lint format clean build publish help

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	poetry install

test: ## Run tests
	poetry run pytest -v --cov=microforge --cov-report=term --cov-report=html

test-fast: ## Run tests without coverage
	poetry run pytest -v

lint: ## Run linters
	poetry run ruff check microforge
	poetry run mypy microforge

format: ## Format code
	poetry run black microforge

format-check: ## Check code formatting
	poetry run black --check microforge

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean ## Build package
	poetry build

publish: build ## Publish to PyPI
	poetry publish

dev: ## Run in development mode
	poetry run microforge --help

example: ## Generate example project
	poetry run microforge new example-service --db postgres --broker redis --ci github --auth oauth2

all: format lint test ## Run all checks

