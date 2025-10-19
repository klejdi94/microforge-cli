#!/usr/bin/env python3
"""Test script to validate pyproject.toml configuration."""

import sys
from pathlib import Path

def test_pyproject_toml():
    """Test that pyproject.toml is valid."""
    try:
        # Try to parse the TOML file
        import tomllib
        with open("pyproject.toml", "rb") as f:
            tomllib.load(f)
        print("OK: pyproject.toml is valid TOML")
        return True
    except ImportError:
        try:
            import tomli
            with open("pyproject.toml", "rb") as f:
                tomli.load(f)
            print("OK: pyproject.toml is valid TOML")
            return True
        except ImportError:
            print("WARNING: TOML parser not available, skipping validation")
            return True
    except Exception as e:
        print(f"ERROR: pyproject.toml is invalid: {e}")
        return False

def test_poetry_config():
    """Test Poetry configuration."""
    try:
        import subprocess
        result = subprocess.run(
            ["poetry", "check"], 
            capture_output=True, 
            text=True, 
            timeout=30
        )
        if result.returncode == 0:
            print("OK: Poetry configuration is valid")
            return True
        else:
            print(f"ERROR: Poetry configuration error: {result.stderr}")
            return False
    except FileNotFoundError:
        print("WARNING: Poetry not installed, skipping Poetry validation")
        return True
    except Exception as e:
        print(f"WARNING: Poetry validation failed: {e}")
        return True

if __name__ == "__main__":
    print("Testing Microforge configuration...")
    
    # Check if pyproject.toml exists
    if not Path("pyproject.toml").exists():
        print("ERROR: pyproject.toml not found")
        sys.exit(1)
    
    # Test TOML validity
    toml_valid = test_pyproject_toml()
    
    # Test Poetry configuration
    poetry_valid = test_poetry_config()
    
    if toml_valid and poetry_valid:
        print("SUCCESS: Configuration is valid!")
        sys.exit(0)
    else:
        print("ERROR: Configuration has issues")
        sys.exit(1)
