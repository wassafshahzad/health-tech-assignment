from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    """Base User DTO."""

    name: str


class User(UserBase):
    """User Read DTO."""

    id: int

    class Config:
        orm_mode = True


class DoctorBase(BaseModel):
    """Base Doctor DTO."""

    user: User


class Doctor(DoctorBase):
    """Doctor Read DTO."""

    id: int

    class Config:
        orm_mode = True


class PatientBase(BaseModel):
    """Base Patient DTO."""

    user: User


class Patient(PatientBase):
    """Base Patient Read DTO."""

    id: int

    class Config:
        orm_mode = True


class InteractionBase(BaseModel):
    """Base Interaction DTO."""

    doctor_id: int
    patient_id: int
    diagnosis: str
    treatment: str
    outcome: str


class Interaction(InteractionBase):
    """Base Interaction Retrieve DTO."""

    id: int
    created_datetime: datetime

    class Config:
        orm_mode = True


class InteractionCreate(InteractionBase):
    """Base Interaction Create DTO."""

    class Config:
        orm_mode = True


class ReportDetail(InteractionBase):
    doctor: DoctorBase
    patient: PatientBase

    class Config:
        orm_mode = True
        fields = {
            "doctor_id": {"exclude": True},
            "patient_id": {"exclude": True},
        }
