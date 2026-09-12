from enum import Enum

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Task(BaseModel):
    id: str
    title: str
    description: str
    status: TaskStatus


class CreateTaskRequest(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""
    status: TaskStatus = TaskStatus.TODO


class UpdateTaskRequest(BaseModel):
    title: str = Field(min_length=1)
    description: str
    status: TaskStatus


class MoveTaskRequest(BaseModel):
    status: TaskStatus
