from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload


from app.models import schemas, utils, models
from app.database.db import get_session


router = APIRouter()


@router.get("/patient/", response_model=list[schemas.Patient | None])
async def get_list_interactions(session: AsyncSession = Depends(get_session)):
    result = await utils.get_all_objects(session, model= models.Patient, exec=False)
    result = result.options(selectinload(models.Patient.user))
    result = await session.exec(result)
    return result.all()
    