from typing import Optional

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.todo.models import Task
from src.todo.schemas import TaskCreationSchema, TaskSchema


async def create_task(
    task: TaskCreationSchema,
    session: AsyncSession,
) -> Optional[TaskSchema]:
    insert_data = task.model_dump()

    stmt = insert(Task).values(**insert_data).returning(Task)
    result = await session.execute(stmt)
    await session.commit()

    result = result.scalars().first()
    if result:
        return TaskSchema.model_validate(result)
    return result


async def delete_task_by_id(
    task_id: int,
    session: AsyncSession,
) -> Optional[TaskSchema]:
    stmt = delete(Task).where(Task.id == task_id).returning(Task)
    result = await session.execute(stmt)
    await session.commit()

    result = result.scalars().first()
    if result:
        return TaskSchema.model_validate(result)
    return result


async def update_task(
    task: TaskSchema,
    session: AsyncSession,
) -> Optional[TaskSchema]:
    insert_data = task.model_dump()

    stmt = update(Task).where(Task.id == task.id).values(**insert_data).returning(Task)
    result = await session.execute(stmt)
    await session.commit()

    result = result.scalars().first()
    if result:
        return TaskSchema.model_validate(result)
    return result


async def get_all_tasks(
    session: AsyncSession,
) -> list[TaskSchema]:
    stmt = select(Task)
    result = await session.execute(stmt)

    result = result.scalars().all()
    result = [TaskSchema.model_validate(task) for task in result]
    return result


async def get_task_by_id(
    task_id: int,
    session: AsyncSession,
) -> Optional[TaskSchema]:
    stmt = select(Task).where(Task.id == task_id)
    result = await session.execute(stmt)

    result = result.scalars().first()
    if result:
        return TaskSchema.model_validate(result)
    return result
