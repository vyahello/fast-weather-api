from typing import Optional

import fastapi
from fastapi import Depends

from weather.models.location import Location
from weather.services import openweather

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(
    location: Location = Depends(), units: Optional[str] = 'metric'
):
    return await openweather.get_report_async(
        location.city, location.state, location.country, units
    )
