# Microforge Project Structure

This document describes the structure and organization of the Microforge project.

## Repository Layout

```
microforge/
├── microforge/              # Main package
│   ├── __init__.py         # Package initialization
│   ├── cli.py              # CLI entrypoint with Typer
│   ├── generator.py        # Project generation logic
│   ├── config.py           # Template configuration
│   ├── py.typed            # Type checking marker
│   └── templates/          # Jinja2 templates
│       ├── app/            # FastAPI app templates
│       │   ├── __init__.py.j2
│       │   ├── main.py.j2
│       │   ├── routes/
│       │   │   ├── __init__.py.j2
│       │   │   └── health.py.j2
│       │   ├── core/
│       │   │   ├── __init__.py.j2
│       │   │   ├── config.py.j2
│       │   │   ├── logging.py.j2
│       │   │   └── telemetry.py.j2
│       │   ├── db/         # Database templates
│       │   │   ├── __init__.py.j2
│       │   │   ├── database.py.j2
│       │   │   └── models.py.j2
│       │   └── auth/       # Auth templates
│       │       ├── __init__.py.j2
│       │       └── oauth2.py.j2
│       ├── worker/         # Celery worker templates
│       │   ├── __init__.py.j2
│       │   └── worker.py.j2
│       ├── tests/          # Test templates
│       │   ├── __init__.py.j2
│       │   ├── conftest.py.j2
│       │   └── test_health.py.j2
│       ├── helm/           # Helm chart templates
│       │   ├── Chart.yaml.j2
│       │   ├── values.yaml.j2
│       │   └── templates/
│       │       ├── deployment.yaml.j2
│       │       └── service.yaml.j2
│       ├── ci/             # CI/CD templates
│       │   ├── azure-pipelines.yml.j2
│       │   ├── github-workflows.yml.j2
│       │   └── gitlab-ci.yml.j2
│       ├── pyproject.toml.j2
│       ├── README.md.j2
│       ├── gitignore.j2
│       ├── Dockerfile.j2
│       ├── docker-compose.yml.j2
│       └── .dockerignore.j2
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── test_cli.py        # CLI tests
│   └── test_generator.py  # Generator tests
├── examples/              # Usage examples
│   └── README.md
├── pyproject.toml         # Project dependencies
├── README.md              # Main documentation
├── QUICKSTART.md          # Quick start guide
├── CONTRIBUTING.md        # Contribution guidelines
├── LICENSE                # MIT License
├── Makefile               # Development tasks
└── .gitignore             # Git ignore rules
```

## Core Components

### 1. CLI (`microforge/cli.py`)

The command-line interface built with Typer:

- **Commands**:
  - `new`: Generate a new microservice project
  - `version`: Show version information

- **Options for `new` command**:
  - `--db`: Database choice (postgres)
  - `--broker`: Message broker (redis, kafka)
  - `--ci`: CI/CD provider (azure, github, gitlab)
  - `--auth`: Authentication type (oauth2)
  - `--git`: Initialize Git repository

### 2. Generator (`microforge/generator.py`)

The `ProjectGenerator` class handles:

- Creating directory structure
- Rendering Jinja2 templates with context
- Writing generated files
- Optionally initializing Git repository

**Key Methods**:
- `generate()`: Main generation orchestrator
- `get_context()`: Build template context from options
- `_create_directories()`: Create project folder structure
- `_generate_files()`: Render and write template files
- `_evaluate_condition()`: Check if conditional templates should be included

### 3. Configuration (`microforge/config.py`)

Centralized configuration mapping templates to output paths:

- Maps template files to their output locations
- Defines conditional templates (e.g., database, auth)
- Maintains single source of truth for file generation

### 4. Templates (`microforge/templates/`)

Jinja2 templates for all generated files:

**Template Variables**:
- `project_name`: Human-readable project name
- `project_slug`: Snake_case project identifier
- `db`: Database choice
- `broker`: Message broker choice
- `ci`: CI/CD provider
- `auth`: Authentication type
- Boolean flags: `has_db`, `has_auth`, `use_postgres`, etc.

**Template Features**:
- Conditional blocks with `{% if %}` statements
- Variable substitution with `{{ variable }}`
- Trim blocks and lstrip blocks for clean output

## Generated Project Structure

When you run `microforge new myservice`, it creates:

```
myservice/
├── app/                    # FastAPI application
│   ├── __init__.py
│   ├── main.py            # App entrypoint
│   ├── routes/            # API routes
│   ├── core/              # Core modules
│   ├── db/                # Database (optional)
│   └── auth/              # Auth (optional)
├── worker/                # Celery worker
│   ├── __init__.py
│   └── worker.py
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   └── test_health.py
├── helm/                  # Kubernetes Helm chart
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── .gitignore
```

## Development Workflow

### 1. Adding New Templates

1. Create Jinja2 template in `microforge/templates/`
2. Add template mapping to `microforge/config.py`
3. Update generator logic if needed
4. Add tests for the new template

### 2. Adding New Options

1. Add CLI option in `microforge/cli.py`
2. Pass option to `ProjectGenerator`
3. Update context in `get_context()`
4. Use in templates with conditional blocks
5. Add validation logic
6. Update documentation

### 3. Testing

```bash
# Run all tests
make test

# Run specific test
poetry run pytest tests/test_cli.py -v

# Test with coverage
poetry run pytest --cov=microforge
```

### 4. Code Quality

```bash
# Format code
make format

# Run linters
make lint

# All checks
make all
```

## Extension Points

### Custom Templates

Users can extend Microforge by:

1. Forking the repository
2. Adding custom templates
3. Modifying `config.py` to include them
4. Building their own distribution

### Template Inheritance

Templates can be organized hierarchically:

- Base templates with common structure
- Specialized templates for different use cases
- Conditional includes based on options

### Plugin System (Future)

Potential for plugin system to:

- Register custom templates
- Add new CLI commands
- Extend generation logic
- Provide custom validators

## Design Decisions

### Why Jinja2?

- Industry standard templating engine
- Powerful control structures
- Good error messages
- Familiar to Python developers

### Why Typer?

- Modern CLI framework
- Automatic help generation
- Type hints for validation
- Rich integration for beautiful output

### Why This Structure?

- **Separation of concerns**: CLI, generator, and config are separate
- **Testability**: Each component can be tested independently
- **Extensibility**: Easy to add new templates and options
- **Maintainability**: Clear organization and documentation

## Performance Considerations

- Templates are loaded on-demand
- File I/O is minimized
- No unnecessary dependencies in generated projects
- Efficient directory creation with `mkdir(parents=True)`

## Security Considerations

- No arbitrary code execution
- Template rendering is sandboxed
- Generated code follows security best practices
- Secrets management through environment variables
- Non-root Docker containers

## Future Enhancements

1. **Interactive Mode**: Prompt for options instead of flags
2. **Template Validation**: Verify templates before generation
3. **Custom Templates**: Allow users to provide custom template directories
4. **Update Command**: Update existing projects with new features
5. **Template Marketplace**: Share and discover community templates
6. **Configuration File**: Support `.microforge.yaml` for defaults
7. **Dry Run Mode**: Preview what would be generated
8. **Diff Mode**: Show changes before applying updates

