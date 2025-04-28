import typer
from traefik_cli.commands import http

# Create the Typer app
app = typer.Typer(
    help="Traefik CLI - Manage Traefik via API",
    invoke_without_command=True,
)

# Shared object to hold CLI global options
class Settings:
    def __init__(self, url: str = None, token: str = None):
        self.url = url
        self.token = token

# CLI callback function (renamed from main to cli)
@app.callback()
def cli(
    ctx: typer.Context,
    url: str = typer.Option(None, help="Traefik API base URL (overrides env var TRAEFIK_API_URL)"),
    token: str = typer.Option(None, help="Traefik API token (overrides env var TRAEFIK_API_TOKEN)"),
):
    """
    Traefik CLI entrypoint.
    """
    ctx.obj = Settings(url=url, token=token)

# Attach HTTP subcommands
app.add_typer(http.app, name="http", help="Manage HTTP routers, services, middlewares")

# This is the simple function that setup.py runs!
def main():
    app()

if __name__ == "__main__":
    main()
