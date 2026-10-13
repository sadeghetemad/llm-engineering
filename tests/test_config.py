import pytest

from llm_engineering.config import require_env
from llm_engineering.llm import get_llm


def test_require_env_returns_value(monkeypatch):
    monkeypatch.setenv("SOME_KEY", "secret")
    assert require_env("SOME_KEY") == "secret"


def test_require_env_raises_when_missing(monkeypatch):
    monkeypatch.delenv("SOME_KEY", raising=False)
    with pytest.raises(RuntimeError, match="SOME_KEY"):
        require_env("SOME_KEY")


def test_get_llm_fails_fast_without_api_key(monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="GROQ_API_KEY"):
        get_llm("groq:openai/gpt-oss-120b")
