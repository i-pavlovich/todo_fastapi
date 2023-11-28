from typing import Annotated, Optional

from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession


import src.todo.services as services
from src.database import get_session
from src.todo.schemas import TaskCreationSchema, TaskSchema

router = APIRouter(
    prefix="/tasks",
    tags=[
        "tasks",
    ],
)


@router.get("/")
async def get_all_tasks(
    session: Annotated[AsyncSession, Depends(get_session)],
):
    tasks = await services.get_all_tasks(session)
    return tasks


@router.get("/{task_id}")
async def get_task_by_id(
    task_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> Optional[TaskSchema]:
    task = await services.get_task_by_id(task_id, session)
    return task


@router.post("/")
async def create_task(
    task: Annotated[TaskCreationSchema, Body()],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> Optional[TaskSchema]:
    new_task = await services.create_task(task, session)
    return new_task


@router.put("/")
async def update_task(
    task: Annotated[TaskSchema, Body()],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> Optional[TaskSchema]:
    updated_task = await services.update_task(task, session)
    return updated_task


@router.delete("/{task_id}")
async def delete_task_by_id(
    task_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> Optional[TaskSchema]:
    deleted_task = await services.delete_task_by_id(task_id, session)
    return deleted_task
