### setup.py
# (optional but nice for local installs)
from setuptools import setup, find_packages

setup(
    name="traefik-cli",
    version="0.1",
    packages=find_packages(),  # <-- use packages, NOT py_modules
    install_requires=[
        "typer[all]",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "traefik-cli=traefik_cli.main:main",
        ],
    },
)

