from typing import Type, Callable

from fastapi import HTTPException
from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_all_objects(
    session: AsyncSession, model: Type[SQLModel], func: Callable) -> list[SQLModel]:
    """Get lists of database objects based on filters

    Args:
        session (AsyncSession): Async Database session.
        model (Type[SQLModel]): class of SQL model.

    Returns:
        list[SQLModel]: list of SQLModels instances.
    """
    
    stmt = select(model)
    if func:
        stmt = func(stmt)
    result = await session.exec(stmt)
    return result


async def get_object_404(
    model: Type[SQLModel], session: AsyncSession, **kwargs: any
) -> SQLModel:
    """Get object from database or raise 404 error.

    Args:
        model (Type[SQLModel]): A class of type SQLModel.
        session (AsyncSession): A instance of async session.

    Raises:
        HTTPException: Raise a 404, Object not found.

    Returns:
        SQLModel: An instance of SQLModel.
    """

    result = await get_all_objects(session=session, model=model)
    result = result.first()

    if result is None:
        raise HTTPException(
            status_code=404, detail=f"{model.__name__} Object does not exist"
        )
    return result
