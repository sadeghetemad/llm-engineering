"""Environment configuration.

API keys are read from environment variables, optionally loaded from a local
`.env` file (see `.env.example`). Never hard-code keys in code or notebooks.
"""

import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(usecwd=True))


def require_env(name: str) -> str:
    """Return the value of an environment variable or raise a helpful error."""
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(
            f"Environment variable {name} is not set. "
            "Copy .env.example to .env and fill it in."
        )
    return value
