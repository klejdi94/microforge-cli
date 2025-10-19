# Publishing Guide

This guide explains how to publish Microforge to PyPI and Artifactory.

## Prerequisites

1. **PyPI Account**: Create account at [pypi.org](https://pypi.org)
2. **API Token**: Generate API token in PyPI account settings
3. **Artifactory Access**: Configure Artifactory repository (if using)

## Publishing to PyPI

### 1. Configure Poetry

```bash
# Configure Poetry with PyPI credentials
poetry config pypi-token.pypi your-pypi-api-token
```

### 2. Build Package

```bash
# Install dependencies
poetry install

# Build the package
poetry build
```

### 3. Publish to PyPI

```bash
# Publish to PyPI
poetry publish
```

## Publishing to Artifactory

### 1. Configure Artifactory Repository

Update `pyproject.toml` with your Artifactory URL:

```toml
[tool.poetry.repositories]
artifactory = { url = "https://your-artifactory-url/api/pypi/pypi-local/simple/" }
```

### 2. Configure Credentials

```bash
# Configure Artifactory credentials
poetry config repositories.artifactory https://your-artifactory-url/api/pypi/pypi-local/
poetry config http-basic.artifactory username password
```

### 3. Publish to Artifactory

```bash
# Publish to Artifactory
poetry publish --repository artifactory
```

## GitHub Actions (Automated)

The project includes GitHub Actions workflows:

### CI/CD Pipeline (`.github/workflows/ci.yml`)
- Runs tests on push/PR
- Builds package on main branch
- Publishes to PyPI and Artifactory on main branch

### Release Pipeline (`.github/workflows/release.yml`)
- Triggers on version tags (v*)
- Creates GitHub release
- Publishes to PyPI

### Required Secrets

Add these secrets to your GitHub repository:

- `PYPI_API_TOKEN`: PyPI API token
- `ARTIFACTORY_USERNAME`: Artifactory username
- `ARTIFACTORY_PASSWORD`: Artifactory password

## Manual Release Process

### 1. Update Version

```bash
# Update version in pyproject.toml
# Then commit and tag
git add pyproject.toml
git commit -m "Bump version to 0.1.1"
git tag v0.1.1
git push origin main --tags
```

### 2. GitHub Actions will automatically:
- Create GitHub release
- Publish to PyPI
- Publish to Artifactory

## Installation After Publishing

Users can install from PyPI:

```bash
pip install microforge
```

Or from Artifactory:

```bash
pip install --index-url https://your-artifactory-url/api/pypi/pypi-local/simple/ microforge
```

## Verification

After publishing, verify installation:

```bash
pip install microforge
microforge --help
microforge new testproject
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**: Check API tokens and credentials
2. **Version Conflicts**: Ensure version is unique
3. **Build Errors**: Check all dependencies are included

### Debug Commands

```bash
# Check package contents
poetry build
tar -tzf dist/microforge-0.1.0.tar.gz

# Test installation
pip install dist/microforge-0.1.0-py3-none-any.whl
```

## Best Practices

1. **Version Management**: Use semantic versioning (MAJOR.MINOR.PATCH)
2. **Testing**: Always test locally before publishing
3. **Documentation**: Keep README and docs updated
4. **Security**: Never commit API tokens or passwords
5. **Rollback**: Keep previous versions available

## Support

For publishing issues:
- Check [Poetry documentation](https://python-poetry.org/docs/)
- Review [PyPI documentation](https://packaging.python.org/)
- Check GitHub Actions logs for automated publishing
