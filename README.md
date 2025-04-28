# Traefik CLI

Traefik CLI is a lightweight command-line interface for interacting with a running Traefik instance over its HTTP API.  
It supports listing routers, services, middlewares, and more, with output available in JSON or human-readable table formats.  
Designed for self-hosters, DevOps engineers, and anyone who manages Traefik deployments.

---

## Major Libraries Used

- [Typer](https://typer.tiangolo.com/) — CLI building
- [Requests](https://docs.python-requests.org/en/latest/) — HTTP API communication
- [Rich](https://rich.readthedocs.io/en/stable/) — Pretty printing tables and output

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/scandora/traefik-cli.git
cd traefik-cli
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

---

## Usage

Make sure you have your Traefik API accessible (usually on port 8080 or 8081 depending on configuration).

You can pass the Traefik API URL at runtime:

```bash
traefik-cli --url http://localhost:8081 http list-routers
```

Or set the environment variable:

```bash
export TRAEFIK_API_URL=http://localhost:8081
traefik-cli http list-routers
```

---

## Output Formats

You can choose between:

- JSON (`--output json`)
- Table (`--output table`)

Example:

```bash
traefik-cli --url http://localhost:8081 http list-routers --output table
```

---

## License

MIT License
