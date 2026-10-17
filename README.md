# LLM Engineering

A hands-on, educational repository for becoming an LLM engineer: working with LLMs through LangChain, building RAG systems, and fine-tuning models.

## Repository layout

```
.
├── notebooks/
│   ├── langchain/       # LangChain fundamentals (start here)
│   ├── rag/             # Retrieval-Augmented Generation
│   └── fine_tuning/     # Model fine-tuning (planned)
├── src/llm_engineering/ # Reusable helpers shared by the notebooks
├── tests/
├── .env.example         # Template for API keys
└── pyproject.toml
```

## Notebooks

| Notebook | Topics |
| --- | --- |
| [01_models_and_messages](notebooks/langchain/01_models_and_messages.ipynb) | Chat models, streaming, `init_chat_model`, message roles |
| [02_prompts_and_output_parsers](notebooks/langchain/02_prompts_and_output_parsers.ipynb) | Prompt templates, list/JSON/Pydantic parsers, structured output |
| [03_chains_and_routing](notebooks/langchain/03_chains_and_routing.ipynb) | LCEL chains, `RunnableLambda`, routing |
| [04_tools](notebooks/langchain/04_tools.ipynb) | Defining tools, tool binding, executing tool calls |
| [05_documents_and_vector_stores](notebooks/langchain/05_documents_and_vector_stores.ipynb) | Documents, embeddings, vector stores |
| [rag/01_tfidf_indexing_and_retrieval](notebooks/rag/01_tfidf_indexing_and_retrieval.ipynb) | RAG indexing and retrieval from scratch with TF-IDF and nearest neighbors |

## Getting started

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync                      # create .venv and install dependencies
cp .env.example .env         # then add your API keys
# then open the notebooks in VS Code (or any Jupyter frontend)
```

Select the `.venv` interpreter as the notebook kernel. Notebooks use `llm_engineering.get_llm()`, which reads `GROQ_API_KEY` from `.env` and defaults to `groq:openai/gpt-oss-120b`. Pass another `"<provider>:<model>"` string to switch models.

## Development

```bash
uv run pytest
```

Keep API keys in `.env` only; it is git-ignored.
