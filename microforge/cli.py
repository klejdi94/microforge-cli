"""CLI entrypoint for Microforge."""

from pathlib import Path
from typing import Optional

import typer  # type: ignore
from rich.console import Console  # type: ignore
from rich.panel import Panel  # type: ignore

from microforge.generator import ProjectGenerator

app = typer.Typer(
    name="microforge",
    help="A production-ready project generator for modern Python microservices.",
    add_completion=False,
)
console = Console()


@app.command()
def new(
    name: str = typer.Argument(..., help="Name of the microservice project"),
    db: Optional[str] = typer.Option(
        None,
        "--db",
        help="Database choice (postgres)",
    ),
    broker: str = typer.Option(
        "redis",
        "--broker",
        help="Message broker (redis, kafka)",
    ),
    ci: str = typer.Option(
        "azure",
        "--ci",
        help="CI/CD provider (azure, github, gitlab)",
    ),
    auth: Optional[str] = typer.Option(
        None,
        "--auth",
        help="Authentication type (oauth2)",
    ),
    git: bool = typer.Option(
        False,
        "--git",
        help="Initialize Git repository",
    ),
) -> None:
    """Create a new microservice project."""
    # Validate inputs
    if broker not in ["redis", "kafka"]:
        console.print("[red]Error: broker must be 'redis' or 'kafka'[/red]")
        raise typer.Exit(1)

    if ci not in ["azure", "github", "gitlab"]:
        console.print("[red]Error: ci must be 'azure', 'github', or 'gitlab'[/red]")
        raise typer.Exit(1)

    if db and db not in ["postgres"]:
        console.print("[red]Error: db must be 'postgres'[/red]")
        raise typer.Exit(1)

    if auth and auth not in ["oauth2"]:
        console.print("[red]Error: auth must be 'oauth2'[/red]")
        raise typer.Exit(1)

    # Display welcome message
    console.print(
        Panel.fit(
            f"[bold cyan]Creating microservice: {name}[/bold cyan]",
            border_style="cyan",
        )
    )

    # Show configuration
    console.print("\n[bold]Configuration:[/bold]")
    console.print(f"  • Project name: [cyan]{name}[/cyan]")
    console.print(f"  • Database: [cyan]{db or 'none'}[/cyan]")
    console.print(f"  • Message broker: [cyan]{broker}[/cyan]")
    console.print(f"  • CI/CD: [cyan]{ci}[/cyan]")
    console.print(f"  • Authentication: [cyan]{auth or 'none'}[/cyan]")
    console.print(f"  • Git init: [cyan]{git}[/cyan]")
    console.print()

    # Create project
    project_path = Path.cwd() / name

    if project_path.exists():
        console.print(f"[red]Error: Directory '{name}' already exists[/red]")
        raise typer.Exit(1)

    try:
        console.print("Generating project...")
        
        generator = ProjectGenerator(
            name=name,
            path=project_path,
            db=db,
            broker=broker,
            ci=ci,
            auth=auth,
            git_init=git,
        )

        generator.generate()

        console.print(
            f"\n[green]Successfully created project: [bold cyan]{name}[/bold cyan]"
        )
        console.print("\n[bold]Next steps:[/bold]")
        console.print(f"  1. cd {name}")
        console.print("  2. poetry install")
        console.print("  3. docker-compose up")
        console.print("\n[dim]Happy coding![/dim]\n")

    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def version() -> None:
    """Show version information."""
    from microforge import __version__

    console.print(f"Microforge version: [cyan]{__version__}[/cyan]")


if __name__ == "__main__":
    app()

