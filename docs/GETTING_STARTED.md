# Getting Started with Microforge

Welcome to Microforge! This guide will help you create your first production-ready Python microservice in minutes.

## What is Microforge?

Microforge is a CLI tool that generates complete, production-ready Python microservice projects with:

- 🚀 **FastAPI** - Modern async web framework
- ⚙️ **Celery** - Distributed task queue
- 🐳 **Docker** - Containerization
- ☸️ **Kubernetes** - Helm charts for deployment
- 📊 **Observability** - Logging, metrics, and tracing
- 🔒 **Security** - Best practices built-in
- 🧪 **Testing** - Test suite included
- 🔄 **CI/CD** - Pipeline templates

## Prerequisites

Before you begin, ensure you have:

- **Python 3.9+** installed
- **pip** or **Poetry** for package management
- **Docker** (optional, for running generated projects)
- **Git** (optional, for version control)

Check your Python version:
```bash
python --version
```

## Step 1: Install Microforge

### Option A: From PyPI (Recommended when published)

```bash
pip install microforge
```

### Option B: From Source

```bash
# Clone the repository
git clone https://github.com/yourusername/microforge.git
cd microforge

# Install with Poetry
poetry install

# Or with pip
pip install -e .
```

### Verify Installation

```bash
microforge version
```

You should see: `Microforge version: 0.1.0`

## Step 2: Create Your First Microservice

### Basic Project

Let's create a simple microservice called "myservice":

```bash
microforge new myservice
```

This creates a complete project with:
- FastAPI web application
- Celery worker
- Redis for message brokering
- Docker setup
- Kubernetes Helm chart
- Tests and CI/CD

### Navigate to Your Project

```bash
cd myservice
```

### Explore the Structure

```bash
ls -la
```

You'll see:
```
myservice/
├── app/              # FastAPI application
├── worker/           # Celery worker
├── tests/            # Test suite
├── helm/             # Kubernetes deployment
├── Dockerfile        # Container image
├── docker-compose.yml
├── pyproject.toml    # Dependencies
└── README.md
```

## Step 3: Run Your Microservice

### Option A: Using Docker Compose (Easiest)

```bash
# Start all services
docker-compose up
```

This starts:
- Your FastAPI application on port 8000
- Celery worker
- Redis

### Option B: Run Locally

```bash
# Install dependencies
poetry install

# Terminal 1: Start the API
poetry run uvicorn app.main:app --reload

# Terminal 2: Start the Celery worker
poetry run celery -A worker.worker worker --loglevel=info
```

## Step 4: Test Your API

### Open in Browser

Visit these URLs:

- **API Root**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs (Interactive Swagger UI)
- **Health Check**: http://localhost:8000/health
- **Metrics**: http://localhost:8000/metrics

### Using curl

```bash
# Health check
curl http://localhost:8000/health

# API root
curl http://localhost:8000/

# Readiness check
curl http://localhost:8000/health/ready
```

Expected response:
```json
{
  "status": "healthy",
  "service": "myservice",
  "environment": "development"
}
```

## Step 5: Add Your Business Logic

### Create a New Route

Create `app/routes/users.py`:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def list_users():
    """List all users."""
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }

@router.post("/users")
async def create_user(name: str):
    """Create a new user."""
    return {"id": 3, "name": name, "status": "created"}
```

### Register the Route

Edit `app/main.py` and add:

```python
from app.routes import users

# Add this line after other routers
app.include_router(users.router, prefix="/api/v1", tags=["users"])
```

### Test Your New Route

```bash
curl http://localhost:8000/api/v1/users
```

## Step 6: Add a Background Task

### Define a Task

Edit `worker/worker.py` and add:

```python
@celery_app.task(name="myservice.send_notification")
def send_notification(user_id: int, message: str):
    """Send a notification to a user."""
    logger.info("Sending notification", user_id=user_id, message=message)
    
    # Your notification logic here
    # e.g., send email, push notification, etc.
    
    return {"status": "sent", "user_id": user_id}
```

### Trigger from API

In your route:

```python
from worker.worker import send_notification

@router.post("/users/{user_id}/notify")
async def notify_user(user_id: int, message: str):
    """Send notification to user."""
    # Queue the task
    task = send_notification.delay(user_id, message)
    
    return {
        "status": "queued",
        "task_id": task.id,
        "user_id": user_id
    }
```

### Test the Background Task

```bash
curl -X POST "http://localhost:8000/api/v1/users/1/notify?message=Hello"
```

Check the Celery worker logs to see the task execution.

## Step 7: Run Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=app --cov=worker

# Run specific test
poetry run pytest tests/test_health.py -v
```

## Step 8: Advanced Features

### Add PostgreSQL Database

Create a new project with PostgreSQL:

```bash
microforge new mydbservice --db postgres
cd mydbservice
```

This adds:
- SQLAlchemy async ORM
- Database models
- Connection pooling
- Alembic for migrations

### Add OAuth2 Authentication

```bash
microforge new myauthservice --auth oauth2
cd myauthservice
```

This adds:
- JWT token authentication
- Password hashing
- OAuth2 password flow
- Protected endpoints

### Use Kafka Instead of Redis

```bash
microforge new mykafkaservice --broker kafka
cd mykafkaservice
```

This configures:
- Kafka for message brokering
- Zookeeper for Kafka coordination
- Celery with Kafka backend

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
microforge new fullservice \
  --db postgres \
  --broker redis \
  --ci github \
  --auth oauth2 \
  --git
```

## Step 9: Deploy to Production

### Build Docker Image

```bash
# Build image
docker build -t myservice:latest .

# Test image
docker run -p 8000:8000 myservice:latest
```

### Deploy to Kubernetes

```bash
# Install with Helm
helm install myservice ./helm

# Check status
kubectl get pods
kubectl logs -f deployment/myservice

# Access service
kubectl port-forward svc/myservice 8000:80
```

### Configure for Production

Edit `helm/values.yaml`:

```yaml
replicaCount: 3

image:
  repository: myregistry/myservice
  tag: "1.0.0"

resources:
  limits:
    cpu: 1000m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
```

## Step 10: Monitor Your Service

### View Logs

```bash
# Docker Compose
docker-compose logs -f api

# Kubernetes
kubectl logs -f deployment/myservice
```

### Check Metrics

Visit http://localhost:8000/metrics to see Prometheus metrics.

### Health Checks

- **Liveness**: http://localhost:8000/health/live
- **Readiness**: http://localhost:8000/health/ready

## Common Tasks

### Update Dependencies

```bash
poetry add <package>
poetry update
```

### Run Code Quality Tools

```bash
# Format code
poetry run black .

# Lint
poetry run ruff check .

# Type check
poetry run mypy app worker
```

### Database Migrations (if using PostgreSQL)

```bash
# Create migration
poetry run alembic revision --autogenerate -m "Add users table"

# Run migrations
poetry run alembic upgrade head

# Rollback
poetry run alembic downgrade -1
```

### Environment Variables

Create `.env` file:

```env
APP_NAME=myservice
APP_ENV=development
LOG_LEVEL=INFO
REDIS_URL=redis://localhost:6379/0
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/mydb
SECRET_KEY=your-secret-key-here
```

## Troubleshooting

### Port Already in Use

```bash
# Use different port
uvicorn app.main:app --port 8001
```

### Redis Connection Error

```bash
# Start Redis
docker-compose up redis

# Or install locally
# Ubuntu: sudo apt-get install redis-server
# Mac: brew install redis
```

### Import Errors

```bash
# Reinstall dependencies
poetry install
```

### Docker Issues

```bash
# Rebuild without cache
docker-compose build --no-cache

# Clean up
docker-compose down -v
```

## Next Steps

1. **Read the Documentation**: Check out [README.md](README.md) for detailed information
2. **Explore Examples**: See [examples/](examples/) for more use cases
3. **Customize**: Modify the generated code to fit your needs
4. **Deploy**: Use the included CI/CD pipelines to deploy
5. **Monitor**: Set up logging and monitoring for production
6. **Scale**: Use Kubernetes HPA for auto-scaling

## Learning Resources

### Generated Project Documentation

Each generated project includes:
- Comprehensive README
- API documentation (Swagger UI)
- Example code with comments
- Test examples

### External Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Celery Documentation](https://docs.celeryproject.org/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/docs/)

## Getting Help

- 📖 **Documentation**: Read the full docs in this repository
- 🐛 **Issues**: Report bugs on GitHub Issues
- 💬 **Discussions**: Ask questions on GitHub Discussions
- 📧 **Email**: Contact support@example.com

## Tips for Success

1. **Start Simple**: Begin with basic features, add complexity as needed
2. **Use Docker**: Docker Compose makes local development easy
3. **Write Tests**: Use the included test framework
4. **Follow Best Practices**: The generated code follows industry standards
5. **Monitor Everything**: Use the built-in observability features
6. **Keep Updated**: Update dependencies regularly
7. **Read Logs**: Structured logging makes debugging easier
8. **Use Type Hints**: Better IDE support and fewer bugs

## Quick Reference

### Common Commands

```bash
# Generate project
microforge new myservice

# Run locally
poetry run uvicorn app.main:app --reload

# Run with Docker
docker-compose up

# Run tests
poetry run pytest

# Format code
poetry run black .

# Deploy to K8s
helm install myservice ./helm
```

### Project Structure

```
myservice/
├── app/           # Your API code here
├── worker/        # Background tasks here
├── tests/         # Tests here
├── helm/          # K8s deployment config
└── docker-compose.yml  # Local development
```

## Congratulations! 🎉

You've successfully created and run your first microservice with Microforge!

Now you can:
- Add your business logic
- Deploy to production
- Scale as needed
- Monitor and maintain

Happy coding! 🚀

---

For more information, see:
- [README.md](README.md) - Full documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [examples/](examples/) - More examples

