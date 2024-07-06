"""populate data

Revision ID: 60315e42ffb6
Revises: ac03b2973e86
Create Date: 2024-07-04 22:33:10.518827

"""
import os

from alembic import op
from sqlmodel import Session


from app.models import Doctor, User, Patient

# revision identifiers, used by Alembic.
revision = '60315e42ffb6'
down_revision = 'ac03b2973e86'
branch_labels = None
depends_on = None



DATABASE_URL = os.environ.get("DATABASE_URL")



def upgrade():
    bind = op.get_bind()
    session = Session(bind=bind)

    # Create 5 doctors and 5 patients with random data
    for i in range(1, 6):
        user_doctor = User(name=f"Doctor {i}")
        session.add(user_doctor)
        session.flush()  # to get the user ID
        doctor = Doctor(user_id=user_doctor.id)
        session.add(doctor)

        user_patient = User(name=f"Patient {i}")
        session.add(user_patient)
        session.flush()  # to get the user ID
        patient = Patient(user_id=user_patient.id)
        session.add(patient)

    session.commit()

def downgrade():
    bind = op.get_bind()
    session = Session(bind=bind)

    # Remove all doctors and patients
    session.exec('DELETE FROM doctor')
    session.exec('DELETE FROM patient')
    session.exec('DELETE FROM user WHERE name LIKE "Doctor %"')
    session.exec('DELETE FROM user WHERE name LIKE "Patient %"')

    session.commit()