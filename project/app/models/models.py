from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship, Column, TIMESTAMP, text


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(default=None)
    doctor: Optional["Doctor"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False, "lazy": "selectin"},
    )
    patient: Optional["Patient"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False, "lazy": "selectin"},
    )


class Doctor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    user: User = Relationship(back_populates="doctor")
    interactions: List["Interaction"] = Relationship(
        back_populates="doctor", sa_relationship_kwargs={"lazy": "selectin"}
    )


class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    user: User = Relationship(back_populates="patient")
    interactions: List["Interaction"] = Relationship(
        back_populates="patient", sa_relationship_kwargs={"lazy": "selectin"}
    )


class Interaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    doctor_id: int = Field(foreign_key="doctor.id", nullable=False)
    patient_id: int = Field(foreign_key="patient.id", nullable=False)
    diagnosis: str
    treatment: str
    outcome: str
    doctor: Doctor = Relationship(
        back_populates="interactions", sa_relationship_kwargs={"lazy": "selectin"}
    )
    patient: Patient = Relationship(
        back_populates="interactions", sa_relationship_kwargs={"lazy": "selectin"}
    )
    created_datetime: Optional[datetime] = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        )
    )
