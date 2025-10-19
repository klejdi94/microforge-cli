# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of Microforge CLI tool
- FastAPI microservice generation
- Celery worker configuration
- Docker and Docker Compose setup
- Kubernetes Helm charts
- CI/CD pipeline templates (Azure DevOps, GitHub Actions, GitLab CI)
- Optional PostgreSQL database support
- Optional OAuth2 authentication
- Redis and Kafka message broker support
- OpenTelemetry instrumentation
- Prometheus metrics
- Structured logging with Structlog
- Comprehensive test suite
- Complete documentation

### Features
- CLI interface with Typer
- Jinja2 template rendering
- Conditional feature inclusion
- Git repository initialization
- Rich terminal output
- Input validation
- Error handling

## [0.1.0] - 2025-01-19

### Added
- Initial release
- Core CLI functionality
- Project generation engine
- Template system
- Documentation
- GitHub Actions CI/CD
- PyPI publishing configuration
- Artifactory publishing support

### Commands
- `microforge new <name>` - Generate new microservice
- `microforge version` - Show version information

### Options
- `--db` - Database choice (postgres)
- `--broker` - Message broker (redis, kafka)
- `--ci` - CI/CD provider (azure, github, gitlab)
- `--auth` - Authentication (oauth2)
- `--git` - Initialize Git repository

### Generated Project Features
- FastAPI application with health checks
- Celery worker with task examples
- Docker containerization
- Kubernetes deployment
- CI/CD pipelines
- Observability (logging, metrics, tracing)
- Database integration (optional)
- Authentication (optional)
- Test suite
- Documentation
