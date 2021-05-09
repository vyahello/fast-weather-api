import http
from typing import Any, Dict, List, Optional, Union

import fastapi
from fastapi import Depends

from weather.models.location import Location
from weather.models.reports import Report
from weather.models.validation import ValidationError
from weather.services import openweather
from weather.services.report import reports

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(
    location: Location = Depends(), units: str = 'metric'
) -> Union[Optional[Dict[str, Any]], fastapi.Response]:
    """Returns a city weather route."""
    try:
        return await openweather.report(location.city, location.country, units)
    except ValidationError as flaw:
        return fastapi.Response(
            content=flaw.error_message, status_code=flaw.status_code
        )
    except Exception as flaw:
        return fastapi.Response(
            content=str(flaw),
            status_code=int(http.HTTPStatus.INTERNAL_SERVER_ERROR),
        )


@router.get('/api/reports', name='reports', response_model=List[Report])
async def all_reports() -> List[Report]:
    """Returns all weather reports."""
    return await reports()
