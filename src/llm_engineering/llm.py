"""Factory for chat models, so notebooks do not depend on a specific provider."""

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from llm_engineering.config import require_env

# Format: "<provider>:<model name>"
DEFAULT_MODEL = "groq:openai/gpt-oss-120b"

_API_KEY_VARS = {
    "groq": "GROQ_API_KEY",
    "openai": "OPENAI_API_KEY",
}


def get_llm(model: str = DEFAULT_MODEL, **kwargs) -> BaseChatModel:
    """Create a chat model from a "<provider>:<model>" string.

    The API key is validated up front so a missing key fails with a clear
    message instead of a provider-specific error on the first request.
    Extra keyword arguments (e.g. `temperature`) are passed to the model.
    """
    provider = model.split(":", 1)[0]
    if provider in _API_KEY_VARS:
        require_env(_API_KEY_VARS[provider])
    return init_chat_model(model, **kwargs)
