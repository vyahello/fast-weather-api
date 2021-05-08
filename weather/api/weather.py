import http
from typing import Any, Dict, Optional, Union

import fastapi
from fastapi import Depends

from weather.models.location import Location
from weather.models.validation import ValidationError
from weather.services import openweather

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
