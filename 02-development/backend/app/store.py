from uuid import uuid4

from sqlalchemy.orm import Session

from app.db_models import TaskModel
from app.models import CreateTaskRequest, Task, TaskStatus, UpdateTaskRequest


def _to_task(task_model: TaskModel) -> Task:
    return Task(
        id=task_model.id,
        title=task_model.title,
        description=task_model.description,
        status=TaskStatus(task_model.status),
    )


def list_tasks(session: Session) -> list[Task]:
    tasks = session.query(TaskModel).all()
    return [_to_task(task) for task in tasks]


def get_task(session: Session, task_id: str) -> Task | None:
    task = session.get(TaskModel, task_id)
    if task is None:
        return None
    return _to_task(task)


def create_task(session: Session, payload: CreateTaskRequest) -> Task:
    task = TaskModel(
        id=str(uuid4()),
        title=payload.title,
        description=payload.description,
        status=payload.status.value,
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    return _to_task(task)


def update_task(
    session: Session,
    task_id: str,
    payload: UpdateTaskRequest,
) -> Task | None:
    task = session.get(TaskModel, task_id)

    if task is None:
        return None

    task.title = payload.title
    task.description = payload.description
    task.status = payload.status.value

    session.commit()
    session.refresh(task)

    return _to_task(task)


def move_task(
    session: Session,
    task_id: str,
    status: TaskStatus,
) -> Task | None:
    task = session.get(TaskModel, task_id)

    if task is None:
        return None

    task.status = status.value

    session.commit()
    session.refresh(task)

    return _to_task(task)


def delete_task(session: Session, task_id: str) -> bool:
    task = session.get(TaskModel, task_id)

    if task is None:
        return False

    session.delete(task)
    session.commit()

    return True