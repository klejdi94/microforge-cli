"""CLI entrypoint for Microforge."""

import argparse
import sys
from pathlib import Path
from typing import Any, Optional

from microforge.generator import ProjectGenerator


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="A production-ready project generator for modern Python microservices.",
        prog="microforge"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # New command
    new_parser = subparsers.add_parser("new", help="Create a new microservice project")
    new_parser.add_argument("name", help="Name of the microservice project")
    new_parser.add_argument("--db", help="Database choice (postgres)")
    new_parser.add_argument("--broker", default="redis", help="Message broker (redis, kafka)")
    new_parser.add_argument("--ci", default="azure", help="CI/CD provider (azure, github, gitlab)")
    new_parser.add_argument("--auth", help="Authentication type (oauth2)")
    new_parser.add_argument("--git", action="store_true", help="Initialize Git repository")
    
    # Version command
    version_parser = subparsers.add_parser("version", help="Show version information")
    
    args = parser.parse_args()
    
    if args.command == "new":
        create_project(args)
    elif args.command == "version":
        show_version()
    else:
        parser.print_help()


def create_project(args: argparse.Namespace) -> None:
    """Create a new microservice project."""
    # Validate inputs
    if args.broker not in ["redis", "kafka"]:
        print("Error: broker must be 'redis' or 'kafka'")
        sys.exit(1)

    if args.ci not in ["azure", "github", "gitlab"]:
        print("Error: ci must be 'azure', 'github', or 'gitlab'")
        sys.exit(1)

    if args.db and args.db not in ["postgres"]:
        print("Error: db must be 'postgres'")
        sys.exit(1)

    if args.auth and args.auth not in ["oauth2"]:
        print("Error: auth must be 'oauth2'")
        sys.exit(1)

    # Display welcome message
    print(f"Creating microservice: {args.name}")
    print()

    # Show configuration
    print("Configuration:")
    print(f"  • Project name: {args.name}")
    print(f"  • Database: {args.db or 'none'}")
    print(f"  • Message broker: {args.broker}")
    print(f"  • CI/CD: {args.ci}")
    print(f"  • Authentication: {args.auth or 'none'}")
    print(f"  • Git init: {args.git}")
    print()

    # Create project
    project_path = Path.cwd() / args.name

    if project_path.exists():
        print(f"Error: Directory '{args.name}' already exists")
        sys.exit(1)

    try:
        print("Generating project...")
        
        generator = ProjectGenerator(
            name=args.name,
            path=project_path,
            db=args.db,
            broker=args.broker,
            ci=args.ci,
            auth=args.auth,
            git_init=args.git,
        )

        generator.generate()

        print(f"Successfully created project: {args.name}")
        print()
        print("Next steps:")
        print(f"  1. cd {args.name}")
        print("  2. poetry install")
        print("  3. docker-compose up")
        print()
        print("Happy coding!")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def show_version() -> None:
    """Show version information."""
    from microforge import __version__
    print(f"Microforge version: {__version__}")


if __name__ == "__main__":
    main()