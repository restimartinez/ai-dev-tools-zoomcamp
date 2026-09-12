"""Flux FastAPI application entry point."""

from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware

from app import store
from app.models import (
    CreateTaskRequest,
    MoveTaskRequest,
    Task,
    UpdateTaskRequest,
)

app = FastAPI(
    title="Flux API",
    version="1.0.0",
    description="Mini Kanban Board API for DataTalksClub AI Dev Tools Zoomcamp Homework 2.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Content-Type"],
)


@app.get("/health")
def health() -> dict[str, str]:
    """Simple health check to verify the server is running."""
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return store.list_tasks()


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: CreateTaskRequest) -> Task:
    return store.create_task(payload)


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str) -> Task:
    task = store.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, payload: UpdateTaskRequest) -> Task:
    task = store.update_task(task_id, payload)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}/status", response_model=Task)
def move_task(task_id: str, payload: MoveTaskRequest) -> Task:
    task = store.move_task(task_id, payload.status)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: str) -> Response:
    deleted = store.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return Response(status_code=204)
