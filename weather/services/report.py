import uuid
from datetime import datetime
from typing import List

from weather.models.location import Location
from weather.models.reports import Report

__reports: List[Report] = []


async def reports() -> List[Report]:
    return list(__reports)


async def add_report(description: str, location: Location) -> Report:
    """Simulate saving to DB."""
    report = Report(
        id_=str(uuid.uuid4()),
        description=description,
        location=location,
        created_date=datetime.now(),
    )

    __reports.append(report)
    __reports.sort(
        key=lambda report_: report_.created_date, reverse=True  # type: ignore
    )
    return report
