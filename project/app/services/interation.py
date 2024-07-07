from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import Query, selectinload

from app.models import schemas, models, get_object_404, get_all_objects
from app.filters.filters import BaseFilter

async def create_interaction(
    session: AsyncSession, interaction: schemas.InteractionCreate
):

    _ = await get_object_404(models.Doctor, session, id=interaction.doctor_id)
    _ = await get_object_404(models.Patient, session, id=interaction.patient_id)

    db_interaction = models.Interaction(
        doctor_id=interaction.doctor_id,
        patient_id=interaction.patient_id,
        diagnosis=interaction.diagnosis,
        treatment=interaction.treatment,
        outcome=interaction.outcome,
    )

    session.add(db_interaction)
    await session.commit()
    await session.refresh(db_interaction)
    return db_interaction


async def get_interactions_by_filter_class(
    session: AsyncSession, filter : BaseFilter
) -> list[models.Interaction]:
    """Get Interaction objects by filters.

    Args:
        session (AsyncSession): Session of AsyncEngine.

    Returns:
        list[models.Interaction]: List of Interaction objects.
    """
    return await get_all_objects(model= models.Interaction, session=session, func=filter.apply)

async def get_reports(session: AsyncSession, filter: BaseFilter) -> Query:
    stmt = await get_all_objects(
        model=models.Interaction, session=session, func=filter.apply,exec=False
    )
    stmt = stmt.options(selectinload(models.Interaction.doctor).selectinload(models.Doctor.user), selectinload(models.Interaction.patient).selectinload(models.Patient.user))
    stmt = stmt.order_by(models.Interaction.created_datetime.desc())
    result = await session.exec(stmt)
    return result
