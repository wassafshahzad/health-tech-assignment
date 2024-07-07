import pytest

from sqlmodel.ext.asyncio.session import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel, create_engine

from app.main import app  
from app.database import db
from app.models import models


SQLITE_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = AsyncEngine(create_engine(
    SQLITE_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    echo=True
))


TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)


@pytest.fixture(scope="function")
async def async_session():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    async_session = TestingSessionLocal
    try:
        yield async_session
    finally:
        async with async_session() as session:
            await session.close()
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)


@pytest.fixture(scope="function")
def override_get_session(async_session):
    async def _override_get_session():
        async with async_session() as session:
            yield session

    return _override_get_session


@pytest.fixture(scope="function")
def test_app(override_get_session):
    app.dependency_overrides[db.get_session] = override_get_session
    yield app
    app.dependency_overrides.clear()  # Clean up dependency overrides


@pytest.fixture(scope="function")
async def init_data(async_session):
    async with async_session() as session:
        for i in range(1, 6):
            user_doctor = models.User(name=f"Doctor {i}")
            session.add(user_doctor)
            await session.flush()  # to get the user ID
            doctor = models.Doctor(user_id=user_doctor.id)
            session.add(doctor)
            user_patient = models.User(name=f"Patient {i}")
            session.add(user_patient)
            await session.flush()  # to get the user ID
            patient = models.Patient(user_id=user_patient.id)
            session.add(patient)
            await session.commit()


@pytest.fixture(scope="function")
def interaction_payload():
    # Example interaction payload for testing
    return {
        "doctor_id": 1,
        "patient_id": 1,
        "diagnosis": "Headache",
        "treatment": "Rest and painkillers",
        "outcome": "Expected recovery in a few days"
    }

