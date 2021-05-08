"""Module contains weather reports API."""
from datetime import datetime
from typing import Optional

from pydantic.main import BaseModel

from weather.models.location import Location


class ReportSubmittal(BaseModel):
    description: str
    location: Location


class Report(ReportSubmittal):
    id_: str
    created_date: Optional[datetime]
