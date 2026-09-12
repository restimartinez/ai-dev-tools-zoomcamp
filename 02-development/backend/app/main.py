"""Flux FastAPI application entry point."""

from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app import store
from app.database import Base, SessionLocal, engine
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

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Content-Type"],
)

def get_db() -> Session:
    testing_session_factory = getattr(
        app.state,
        "testing_session_factory",
        None,
    )

    if testing_session_factory is not None:
        return testing_session_factory()

    return SessionLocal()

@app.get("/health")
def health() -> dict[str, str]:
    """Simple health check to verify the server is running."""
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    db = get_db()
    try:
        return store.list_tasks(db)
    finally:
        db.close()

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: CreateTaskRequest) -> Task:
    db = get_db()
    try:
        return store.create_task(db, payload)
    finally:
        db.close()


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str) -> Task:
    db = get_db()
    try:
        task = store.get_task(db, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    finally:
        db.close()


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, payload: UpdateTaskRequest) -> Task:
    db = get_db()
    try:
        task = store.update_task(db, task_id, payload)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    finally:
        db.close()


@app.patch("/tasks/{task_id}/status", response_model=Task)
def move_task(task_id: str, payload: MoveTaskRequest) -> Task:
    db = get_db()
    try:
        task = store.move_task(db, task_id, payload.status)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    finally:
        db.close()


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: str) -> Response:
    db = get_db()
    try:
        deleted = store.delete_task(db, task_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Task not found")
        return Response(status_code=204)
    finally:
        db.close()