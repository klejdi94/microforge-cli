# Installation Guide

Complete guide for installing and setting up Microforge.

## Prerequisites

- **Python**: 3.9 or higher
- **Poetry**: 1.7.0 or higher (recommended) or pip
- **Git**: For version control (optional)
- **Docker**: For running generated projects (optional)

## Installation Methods

### Method 1: Install from PyPI (Recommended)

Once published to PyPI:

```bash
pip install microforge
```

Or with pipx (isolated environment):

```bash
pipx install microforge
```

### Method 2: Install from Source

#### Using Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/microforge.git
cd microforge

# Install with Poetry
poetry install

# Verify installation
poetry run microforge version
```

#### Using pip

```bash
# Clone the repository
git clone https://github.com/yourusername/microforge.git
cd microforge

# Install in development mode
pip install -e .

# Verify installation
microforge version
```

### Method 3: Install Specific Version

```bash
# Install specific version
pip install microforge==0.1.0

# Install latest pre-release
pip install --pre microforge
```

## Verifying Installation

After installation, verify that Microforge is working:

```bash
# Check version
microforge version

# Show help
microforge --help

# Show help for new command
microforge new --help
```

Expected output:

```
Microforge version: 0.1.0
```

## Setting Up Development Environment

For contributing to Microforge:

### 1. Clone and Install

```bash
git clone https://github.com/yourusername/microforge.git
cd microforge
poetry install
```

### 2. Install Pre-commit Hooks (Optional)

```bash
poetry run pre-commit install
```

### 3. Run Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=microforge

# Run specific test file
poetry run pytest tests/test_cli.py -v
```

### 4. Code Quality Tools

```bash
# Format code
poetry run black microforge

# Lint code
poetry run ruff check microforge

# Type check
poetry run mypy microforge
```

### 5. Build Package

```bash
# Build distribution
poetry build

# Check distribution
poetry run twine check dist/*
```

## Configuration

### Environment Variables

Microforge respects the following environment variables:

- `MICROFORGE_TEMPLATE_DIR`: Custom template directory (advanced)
- `MICROFORGE_CONFIG`: Path to custom config file (future)

### Shell Completion (Optional)

Enable shell completion for better CLI experience:

#### Bash

```bash
microforge --install-completion bash
```

#### Zsh

```bash
microforge --install-completion zsh
```

#### Fish

```bash
microforge --install-completion fish
```

## Upgrading

### From PyPI

```bash
pip install --upgrade microforge
```

### From Source

```bash
cd microforge
git pull origin main
poetry install
```

## Uninstalling

### If installed with pip

```bash
pip uninstall microforge
```

### If installed with pipx

```bash
pipx uninstall microforge
```

### If installed from source

```bash
pip uninstall microforge
# Then delete the cloned directory
```

## Troubleshooting

### Command Not Found

If `microforge` command is not found:

1. **Check PATH**: Ensure Python scripts directory is in PATH
   ```bash
   # On Linux/Mac
   export PATH="$HOME/.local/bin:$PATH"
   
   # On Windows
   # Add %APPDATA%\Python\Scripts to PATH
   ```

2. **Use full path**:
   ```bash
   python -m microforge.cli new myservice
   ```

3. **Reinstall**:
   ```bash
   pip uninstall microforge
   pip install microforge
   ```

### Import Errors

If you see import errors:

```bash
# Reinstall dependencies
poetry install

# Or with pip
pip install -r requirements.txt
```

### Permission Errors

On Linux/Mac, if you get permission errors:

```bash
# Install for user only
pip install --user microforge

# Or use virtual environment
python -m venv venv
source venv/bin/activate
pip install microforge
```

### Template Errors

If templates fail to render:

```bash
# Verify installation
pip show microforge

# Reinstall
pip install --force-reinstall microforge
```

## Platform-Specific Notes

### Windows

- Use PowerShell or Command Prompt
- Paths use backslashes: `microforge\templates\`
- May need to run as Administrator for global install

### macOS

- May need to install Xcode Command Line Tools:
  ```bash
  xcode-select --install
  ```

### Linux

- Ensure Python development headers are installed:
  ```bash
  # Debian/Ubuntu
  sudo apt-get install python3-dev
  
  # Fedora/RHEL
  sudo dnf install python3-devel
  ```

## Docker Installation (Alternative)

Run Microforge in a Docker container:

```bash
# Build image
docker build -t microforge .

# Run
docker run -it -v $(pwd):/workspace microforge new myservice
```

## Next Steps

After installation:

1. Read the [Quick Start Guide](QUICKSTART.md)
2. Generate your first project: `microforge new myservice`
3. Explore [examples](examples/)
4. Check the [documentation](README.md)

## Getting Help

- 📖 Documentation: [README.md](README.md)
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions
- 📧 Email: support@example.com

## System Requirements

### Minimum Requirements

- Python 3.9+
- 100 MB disk space
- 512 MB RAM

### Recommended Requirements

- Python 3.11+
- 500 MB disk space (for generated projects)
- 2 GB RAM
- Docker Desktop (for running generated projects)

## Dependencies

Microforge depends on:

- **typer**: CLI framework
- **jinja2**: Template engine
- **rich**: Terminal formatting
- **pyyaml**: YAML support

All dependencies are automatically installed.

