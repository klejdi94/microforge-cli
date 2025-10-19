# Microforge Verification Checklist

Use this checklist to verify that Microforge is working correctly.

## ✅ Installation Verification

### 1. Check Installation

```bash
# Check if microforge is installed
microforge --help

# Check version
microforge version
```

**Expected**: Should show help text and version number without errors.

### 2. Verify Dependencies

```bash
# Check Python version (should be 3.9+)
python --version

# List installed packages
pip list | grep microforge
```

**Expected**: Python 3.9+ and microforge package listed.

## ✅ Basic Functionality

### 3. Generate Basic Project

```bash
# Create a test directory
mkdir test-microforge
cd test-microforge

# Generate basic project
microforge new testservice

# Verify project was created
ls testservice/
```

**Expected**: Directory `testservice` created with all files.

### 4. Verify Generated Structure

```bash
cd testservice

# Check main directories exist
ls -la

# Verify key files
test -f pyproject.toml && echo "✓ pyproject.toml"
test -f Dockerfile && echo "✓ Dockerfile"
test -f docker-compose.yml && echo "✓ docker-compose.yml"
test -f README.md && echo "✓ README.md"
test -d app && echo "✓ app/"
test -d worker && echo "✓ worker/"
test -d tests && echo "✓ tests/"
test -d helm && echo "✓ helm/"
```

**Expected**: All checks should pass with ✓.

## ✅ Advanced Features

### 5. Test with Database Option

```bash
cd ..
microforge new testdb --db postgres
cd testdb

# Verify database files
test -d app/db && echo "✓ Database module created"
test -f app/db/database.py && echo "✓ Database config"
test -f app/db/models.py && echo "✓ Database models"
```

**Expected**: Database files created.

### 6. Test with Authentication

```bash
cd ..
microforge new testauth --auth oauth2
cd testauth

# Verify auth files
test -d app/auth && echo "✓ Auth module created"
test -f app/auth/oauth2.py && echo "✓ OAuth2 implementation"
```

**Expected**: Auth files created.

### 7. Test with Kafka

```bash
cd ..
microforge new testkafka --broker kafka
cd testkafka

# Check docker-compose for Kafka
grep -q "kafka" docker-compose.yml && echo "✓ Kafka configured"
grep -q "zookeeper" docker-compose.yml && echo "✓ Zookeeper configured"
```

**Expected**: Kafka and Zookeeper in docker-compose.

### 8. Test CI/CD Options

```bash
# Azure DevOps
cd ..
microforge new testazure --ci azure
test -f testazure/azure-pipelines.yml && echo "✓ Azure pipeline"

# GitHub Actions
microforge new testgithub --ci github
test -f testgithub/.github/workflows/ci.yml && echo "✓ GitHub workflow"

# GitLab CI
microforge new testgitlab --ci gitlab
test -f testgitlab/.gitlab-ci.yml && echo "✓ GitLab CI"
```

**Expected**: Appropriate CI/CD files created.

### 9. Test Full-Featured Project

```bash
cd ..
microforge new fullfeatured \
  --db postgres \
  --broker redis \
  --ci github \
  --auth oauth2

cd fullfeatured

# Verify all features
test -d app/db && echo "✓ Database"
test -d app/auth && echo "✓ Authentication"
test -f .github/workflows/ci.yml && echo "✓ CI/CD"
grep -q "redis" docker-compose.yml && echo "✓ Redis"
```

**Expected**: All features present.

## ✅ Generated Project Verification

### 10. Verify Python Syntax

```bash
cd fullfeatured

# Check Python files for syntax errors
python -m py_compile app/main.py
python -m py_compile worker/worker.py
python -m py_compile app/core/config.py
```

**Expected**: No syntax errors.

### 11. Verify Dependencies

```bash
# Check if pyproject.toml is valid
cat pyproject.toml

# Verify key dependencies are listed
grep -q "fastapi" pyproject.toml && echo "✓ FastAPI"
grep -q "celery" pyproject.toml && echo "✓ Celery"
grep -q "redis" pyproject.toml && echo "✓ Redis"
grep -q "sqlalchemy" pyproject.toml && echo "✓ SQLAlchemy"
```

**Expected**: All dependencies listed.

### 12. Verify Docker Files

```bash
# Check Dockerfile syntax
docker build --no-cache -t test-image . --dry-run 2>/dev/null || echo "Dockerfile valid"

# Verify docker-compose syntax
docker-compose config > /dev/null && echo "✓ docker-compose.yml valid"
```

**Expected**: No syntax errors.

### 13. Verify Helm Chart

```bash
# Check Helm chart syntax
helm lint helm/ && echo "✓ Helm chart valid"

# Verify chart structure
test -f helm/Chart.yaml && echo "✓ Chart.yaml"
test -f helm/values.yaml && echo "✓ values.yaml"
test -f helm/templates/deployment.yaml && echo "✓ deployment.yaml"
test -f helm/templates/service.yaml && echo "✓ service.yaml"
```

**Expected**: Helm chart is valid.

## ✅ Runtime Verification

### 14. Install and Run Generated Project

```bash
# Install dependencies (requires Poetry)
poetry install

# Run tests
poetry run pytest

# Check if app starts (optional, requires dependencies)
# poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 &
# sleep 5
# curl http://localhost:8000/health
# kill %1
```

**Expected**: Tests pass, app starts successfully.

### 15. Docker Compose Test (Optional)

```bash
# Start services with Docker Compose
docker-compose up -d

# Wait for services to start
sleep 10

# Test health endpoint
curl http://localhost:8000/health

# Check logs
docker-compose logs api

# Stop services
docker-compose down
```

**Expected**: Services start and health check returns 200.

## ✅ Error Handling

### 16. Test Error Cases

```bash
# Try to create project in existing directory
cd ..
mkdir existing-dir
microforge new existing-dir
microforge new existing-dir  # Should fail

# Try invalid options
microforge new test --broker invalid  # Should fail
microforge new test --ci invalid      # Should fail
microforge new test --db invalid      # Should fail
```

**Expected**: Appropriate error messages displayed.

## ✅ Cleanup

### 17. Clean Up Test Projects

```bash
cd ..
rm -rf test-microforge testservice testdb testauth testkafka
rm -rf testazure testgithub testgitlab fullfeatured existing-dir
```

## 📊 Verification Summary

After completing all checks:

- [ ] Installation works
- [ ] Basic project generation works
- [ ] All optional features work
- [ ] Generated code is syntactically correct
- [ ] Docker files are valid
- [ ] Helm charts are valid
- [ ] Tests can run
- [ ] Error handling works
- [ ] Documentation is complete

## 🐛 Troubleshooting

If any checks fail:

1. **Installation Issues**: Reinstall with `pip install --force-reinstall microforge`
2. **Template Errors**: Check Jinja2 syntax in templates
3. **Docker Issues**: Ensure Docker is running
4. **Helm Issues**: Install Helm if not present
5. **Permission Issues**: Check file permissions

## 📝 Reporting Issues

If you find issues:

1. Note which check failed
2. Capture error messages
3. Note your environment (OS, Python version, etc.)
4. Create an issue on GitHub with details

## ✅ Success Criteria

Microforge is working correctly if:

1. ✅ All basic functionality checks pass
2. ✅ All optional features work
3. ✅ Generated projects are syntactically valid
4. ✅ Generated projects can be built and run
5. ✅ Error handling works as expected

---

**Note**: Some checks require additional tools (Docker, Helm, Poetry) to be installed.

