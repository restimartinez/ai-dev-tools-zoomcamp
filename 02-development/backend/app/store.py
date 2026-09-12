"""Temporary in-memory task store.

Replace this module with a database-backed repository later
(SQLite + SQLAlchemy) without changing the API layer much.
"""

from uuid import uuid4

from app.models import CreateTaskRequest, Task, TaskStatus, UpdateTaskRequest

_tasks: dict[str, Task] = {}


def list_tasks() -> list[Task]:
    return list(_tasks.values())


def get_task(task_id: str) -> Task | None:
    return _tasks.get(task_id)


def create_task(payload: CreateTaskRequest) -> Task:
    task = Task(
        id=str(uuid4()),
        title=payload.title,
        description=payload.description,
        status=payload.status,
    )
    _tasks[task.id] = task
    return task


def update_task(task_id: str, payload: UpdateTaskRequest) -> Task | None:
    existing = _tasks.get(task_id)
    if existing is None:
        return None

    updated = Task(
        id=existing.id,
        title=payload.title,
        description=payload.description,
        status=payload.status,
    )
    _tasks[task_id] = updated
    return updated


def move_task(task_id: str, status: TaskStatus) -> Task | None:
    existing = _tasks.get(task_id)
    if existing is None:
        return None

    updated = existing.model_copy(update={"status": status})
    _tasks[task_id] = updated
    return updated


def delete_task(task_id: str) -> bool:
    if task_id not in _tasks:
        return False
    del _tasks[task_id]
    return True
