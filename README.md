# Microforge 🔥

A production-ready project generator for modern Python microservices.

## Quick Start

```bash
# Install (when published)
pip install microforge

# Generate a project
microforge new myservice

# Run the service
cd myservice
docker-compose up
```

## Features

- **FastAPI** - Modern async web framework
- **Celery** - Distributed task queue
- **Docker** - Containerization with docker-compose
- **Kubernetes** - Helm charts for deployment
- **CI/CD** - Azure DevOps, GitHub Actions, GitLab CI
- **Observability** - OpenTelemetry + Prometheus metrics
- **Database** - PostgreSQL support (optional)
- **Authentication** - OAuth2 support (optional)

## Usage

### Basic Project
```bash
microforge new myservice
```

### With Options
```bash
microforge new myservice --db postgres --broker redis --ci github --auth oauth2 --git
```

### Available Options
- `--db` - Database: `postgres`
- `--broker` - Message broker: `redis`, `kafka`
- `--ci` - CI/CD: `azure`, `github`, `gitlab`
- `--auth` - Authentication: `oauth2`
- `--git` - Initialize Git repository

## Generated Project

```
myservice/
├── app/                    # FastAPI application
├── worker/                # Celery worker
├── tests/                 # Test suite
├── helm/                  # Kubernetes deployment
├── Dockerfile             # Container image
├── docker-compose.yml     # Local development
└── pyproject.toml         # Dependencies
```

## Documentation

- **[Getting Started](docs/GETTING_STARTED.md)** - Complete tutorial
- **[Installation](docs/INSTALLATION.md)** - Setup guide
- **[Examples](examples/README.md)** - Usage examples
- **[Contributing](CONTRIBUTING.md)** - How to contribute

## Development

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Format code
poetry run black .

# Lint
poetry run ruff check .
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

