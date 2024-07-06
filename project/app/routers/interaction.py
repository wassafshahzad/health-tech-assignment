from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession


from app.models import schemas
from app.database.db import get_session
from app.services import interation as service
from app.filters.filters import InteractionFilter

router = APIRouter()


@router.post("/interactions/", response_model=schemas.Interaction)
async def create_interaction(
    interaction: schemas.InteractionCreate, session: AsyncSession = Depends(get_session)
):
    return await service.create_interaction(session, interaction)


@router.get("/interactions/", response_model=list[schemas.Interaction | None])
async def get_list_interactions(filters: InteractionFilter = Depends(), session: AsyncSession = Depends(get_session)):
    result = await service.get_interactions_by_filter_class(session, filters)
    return result.all()