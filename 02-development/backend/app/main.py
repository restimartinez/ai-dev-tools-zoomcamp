"""Flux FastAPI application entry point."""

from fastapi import FastAPI

app = FastAPI(
    title="Flux API",
    version="1.0.0",
    description="Mini Kanban Board API for DataTalksClub AI Dev Tools Zoomcamp Homework 2.",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Simple health check to verify the server is running."""
    return {"status": "ok"}
