from pydantic import BaseModel


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

    user_id: int


class Doctor(DoctorBase):
    """Doctor Read DTO."""

    id: int
    user: User

    class Config:
        orm_mode = True


class PatientBase(BaseModel):
    """Base Patient DTO."""

    user_id: int


class Patient(PatientBase):
    """Base Patient Read DTO."""

    id: int
    user: User

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

    class Config:
        orm_mode = True


class InteractionCreate(InteractionBase):
    """Base Interaction Create DTO."""

    class Config:
        orm_mode = True
