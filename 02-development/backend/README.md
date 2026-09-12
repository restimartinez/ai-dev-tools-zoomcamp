# Flux backend

FastAPI API for the Flux Mini Kanban Board.

## Prerequisites

- [uv](https://docs.astral.sh/uv/)
- Python 3.13+ (managed via uv)

## Install dependencies

From this directory:

```bash
uv sync
```

## Run the API

```bash
uv run uvicorn app.main:app --reload
```

The server listens on [http://localhost:8000](http://localhost:8000).

Check that it is up:

- Health: [http://localhost:8000/health](http://localhost:8000/health)
- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

Task endpoints are not implemented yet; they will follow the contract in [`../openapi.yaml`](../openapi.yaml).
