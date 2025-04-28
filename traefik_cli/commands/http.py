import typer
import json
import time
from rich.table import Table
from rich.console import Console
from traefik_cli.client import TraefikClient

app = typer.Typer()

client = None
console = Console()

@app.callback()
def init(ctx: typer.Context):
    """
    Initialize TraefikClient using --url and --token options.
    """
    settings = ctx.obj
    global client
    client = TraefikClient(base_url=settings.url, token=settings.token)

def print_routers_table(routers):
    table = Table(title="HTTP Routers")

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Rule", style="magenta")
    table.add_column("Service", style="green")
    table.add_column("Status", style="yellow")

    for router in routers:
        table.add_row(
            router.get("name", ""),
            router.get("rule", ""),
            router.get("service", ""),
            router.get("status", ""),
        )

    console.print(table)

def print_services_table(services):
    table = Table(title="HTTP Services")

    table.add_column("Name", style="cyan", no_wrap=True)

    for service in services:
        table.add_row(service.get("name", ""))

    console.print(table)

@app.command("list-routers")
def list_http_routers(
    output: str = typer.Option("json", help="Output format: json or table"),
    watch: bool = typer.Option(False, help="Watch and refresh every 5 seconds"),
):
    """List all HTTP routers"""
    try:
        while True:
            routers = client.get("/api/http/routers")
            console.clear()
            if output == "table":
                print_routers_table(routers)
            else:
                typer.echo(json.dumps(routers, indent=2))

            if not watch:
                break

            time.sleep(5)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)

@app.command("show-router")
def show_http_router(name: str):
    """Show specific HTTP router"""
    try:
        router = client.get(f"/api/http/routers/{name}")
        typer.echo(json.dumps(router, indent=2))
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)

@app.command("list-services")
def list_http_services(
    output: str = typer.Option("json", help="Output format: json or table"),
    watch: bool = typer.Option(False, help="Watch and refresh every 5 seconds"),
):
    """List all HTTP services"""
    try:
        while True:
            services = client.get("/api/http/services")
            console.clear()
            if output == "table":
                print_services_table(services)
            else:
                typer.echo(json.dumps(services, indent=2))

            if not watch:
                break

            time.sleep(5)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)

@app.command("show-service")
def show_http_service(name: str):
    """Show specific HTTP service"""
    try:
        service = client.get(f"/api/http/services/{name}")
        typer.echo(json.dumps(service, indent=2))
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
