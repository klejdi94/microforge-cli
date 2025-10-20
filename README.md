# Microforge 🔥

A production-ready project generator for modern Python microservices.

## Quick Start

```bash
# Install
pip install microforge

# Generate a microservice
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

## Generated Project Structure

```
myservice/
├── app/                    # FastAPI application
│   ├── main.py            # Main application
│   ├── routes/            # API routes
│   ├── core/              # Core functionality
│   ├── db/                # Database (if --db postgres)
│   └── auth/              # Authentication (if --auth oauth2)
├── worker/                # Celery worker
├── tests/                 # Test suite
├── helm/                  # Kubernetes deployment
├── Dockerfile             # Container image
├── docker-compose.yml     # Local development
└── pyproject.toml         # Dependencies
```

## Development

```bash
# Clone repository
git clone https://github.com/klejdi94/microforge-cli.git
cd microforge-cli

# Install dependencies
pip install -e .

# Run tests
python -m pytest

# Build package
python -m build
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Start forging microservices today!** 🔥