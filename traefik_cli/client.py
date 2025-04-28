### traefik_cli/client.py
import os
import requests

class TraefikClient:
    def __init__(self, base_url=None, token=None):
        self.base_url = base_url or os.getenv("TRAEFIK_API_URL", "http://localhost:8080")
        self.token = token or os.getenv("TRAEFIK_API_TOKEN")

    def get(self, path):
        url = self.base_url.rstrip("/") + path
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise Exception(f"HTTP {response.status_code}: {response.text}")
        return response.json()
