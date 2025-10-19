# Microforge Quick Start Guide

Get started with Microforge in 5 minutes! 🚀

## Installation

### From PyPI (when published)

```bash
pip install microforge
```

### From Source

```bash
git clone https://github.com/yourusername/microforge.git
cd microforge
poetry install
```

## Your First Microservice

### 1. Generate a Project

```bash
microforge new myservice
```

This creates a complete microservice with:
- FastAPI web application
- Celery worker for background tasks
- Redis for message brokering
- Docker setup for local development
- Kubernetes Helm chart
- OpenTelemetry instrumentation
- Structured logging
- Health check endpoints

### 2. Navigate to Your Project

```bash
cd myservice
```

### 3. Start the Services

Using Docker Compose (recommended):

```bash
docker-compose up
```

Or install dependencies and run locally:

```bash
# Install dependencies
poetry install

# Terminal 1: Start the API
poetry run uvicorn app.main:app --reload

# Terminal 2: Start the Celery worker
poetry run celery -A worker.worker worker --loglevel=info
```

### 4. Test Your API

Open your browser to:
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/health
- Metrics: http://localhost:8000/metrics

Or use curl:

```bash
# Health check
curl http://localhost:8000/health

# API root
curl http://localhost:8000/
```

## Advanced Usage

### With PostgreSQL Database

```bash
microforge new myservice --db postgres
```

This adds:
- SQLAlchemy async ORM
- Database models
- Alembic migrations
- PostgreSQL in docker-compose

### With OAuth2 Authentication

```bash
microforge new myservice --auth oauth2
```

This adds:
- JWT token authentication
- Password hashing with bcrypt
- OAuth2 password flow
- User authentication endpoints

### With Kafka

```bash
microforge new myservice --broker kafka
```

This replaces Redis with Kafka for:
- Message brokering
- Event streaming
- Celery backend

### Choose Your CI/CD

```bash
# GitHub Actions
microforge new myservice --ci github

# Azure DevOps
microforge new myservice --ci azure

# GitLab CI
microforge new myservice --ci gitlab
```

### Full-Featured Project

```bash
microforge new myservice \
  --db postgres \
  --broker redis \
  --ci github \
  --auth oauth2 \
  --git
```

## Project Structure

```
myservice/
├── app/                    # FastAPI application
│   ├── main.py            # Application entrypoint
│   ├── routes/            # API routes
│   │   └── health.py      # Health check endpoints
│   ├── core/              # Core functionality
│   │   ├── config.py      # Configuration
│   │   ├── logging.py     # Structured logging
│   │   └── telemetry.py   # OpenTelemetry setup
│   ├── db/                # Database (if --db)
│   │   ├── database.py    # DB connection
│   │   └── models.py      # SQLAlchemy models
│   └── auth/              # Authentication (if --auth)
│       └── oauth2.py      # OAuth2 implementation
├── worker/                # Celery worker
│   └── worker.py          # Task definitions
├── tests/                 # Test suite
│   ├── conftest.py        # Pytest fixtures
│   └── test_health.py     # Health check tests
├── helm/                  # Kubernetes Helm chart
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
├── Dockerfile             # Container image
├── docker-compose.yml     # Local development
├── pyproject.toml         # Dependencies
└── README.md              # Project documentation
```

## Next Steps

### 1. Add Your Business Logic

Create new routes in `app/routes/`:

```python
# app/routes/users.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def list_users():
    return {"users": []}
```

Register in `app/main.py`:

```python
from app.routes import users
app.include_router(users.router, prefix="/api/v1", tags=["users"])
```

### 2. Add Background Tasks

Define tasks in `worker/worker.py`:

```python
@celery_app.task
def send_email(to: str, subject: str, body: str):
    # Send email logic
    return {"status": "sent"}
```

Trigger from your API:

```python
from worker.worker import send_email

@router.post("/send-email")
async def trigger_email():
    send_email.delay("user@example.com", "Hello", "World")
    return {"status": "queued"}
```

### 3. Run Tests

```bash
poetry run pytest
```

### 4. Deploy to Kubernetes

```bash
# Build and push your image
docker build -t myregistry/myservice:latest .
docker push myregistry/myservice:latest

# Deploy with Helm
helm install myservice ./helm \
  --set image.repository=myregistry/myservice \
  --set image.tag=latest
```

## Tips & Best Practices

1. **Environment Variables**: Copy `.env.example` to `.env` and configure
2. **Database Migrations**: Use Alembic for schema changes
3. **Logging**: Use structured logging from `app.core.logging`
4. **Metrics**: Expose custom metrics via Prometheus client
5. **Testing**: Write tests for all endpoints and tasks
6. **Security**: Update SECRET_KEY in production
7. **Documentation**: Keep README.md updated with your changes

## Troubleshooting

### Port Already in Use

```bash
# Change port in docker-compose.yml or run locally on different port
uvicorn app.main:app --port 8001
```

### Redis Connection Error

```bash
# Ensure Redis is running
docker-compose up redis
```

### Import Errors

```bash
# Reinstall dependencies
poetry install
```

## Getting Help

- 📖 Read the full [README.md](README.md)
- 🐛 Report issues on GitHub
- 💬 Join our community discussions
- 📚 Check out [examples/](examples/)

Happy coding! 🎉

