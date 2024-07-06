"""Base filter class"""

from abc import ABC, abstractmethod
from sqlalchemy.orm import Query
from pydantic import BaseModel
from typing import Optional

from app.models import Interaction

class BaseFilter(ABC):

    @abstractmethod
    async def apply(self,Query):
        pass



class InteractionFilter(BaseModel, BaseFilter):

    diagnosis_contains : Optional[str] = None
    treatment_contains : Optional[str] = None
    outcome_contains   : Optional[str] = None
    doctor_id          : Optional[int] = None
    patient_id         : Optional[int] = None

    def apply(self, query: Query) -> Query:
        """Apply filter function.

        Args:
            query (Query): Query object for filtering.

        Returns:
            Query: Return filtered query.
        """

        if self.diagnosis_contains:
            query = query.filter(Interaction.diagnosis.contains(self.diagnosis_contains))
        if self.treatment_contains:
            query = query.filter(Interaction.treatment.contains(self.treatment_contains))
        if self.outcome_contains:
            query = query.filter(Interaction.outcome.contains(self.outcome_contains))
        if self.doctor_id:
            query = query.filter(Interaction.doctor_id == self.doctor_id)
        if self.patient_id:
            query = query.filter(Interaction.patient_id == self.patient_id)      
        
        return query
