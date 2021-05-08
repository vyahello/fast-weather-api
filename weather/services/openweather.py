import http
from typing import Any, Dict, Optional, Tuple

import httpx
from httpx import Response

from weather.support import cache
from weather.models.validation import ValidationError

api_key: Optional[str] = None


def _report_url(query: str, api_key_: Optional[str], units: str) -> str:
    return (
        f'https://api.openweathermap.org/data'
        f'/2.5/weather?q={query}&appid={api_key_}&units={units}'
    )


async def report(
    city: str, country: str, units: str
) -> Optional[Dict[str, Any]]:
    city, country, units = validate_units(city, country, units)
    if forecast := cache.get_weather(city, country, units):
        return forecast
    query = f'{city},{country}'
    async with httpx.AsyncClient() as client:
        response: Response = await client.get(
            url=_report_url(query, api_key, units)
        )
        if http.HTTPStatus(response.status_code) != http.HTTPStatus.OK:
            raise ValidationError(response.text, response.status_code)
    forecast = response.json()['main']
    cache.set_weather(city, country, units, forecast)
    return forecast


def validate_units(
    city: str, country: Optional[str], units: str
) -> Tuple[str, str, str]:
    city = city.lower().strip()
    if not country:
        country = 'us'
    else:
        country = country.lower().strip()

    if len(country) != 2:
        error = (
            f'Invalid country: {country}. '
            f'It must be a two letter abbreviation such as US or GB.'
        )
        raise ValidationError(
            status_code=int(http.HTTPStatus.BAD_REQUEST), error_message=error
        )
    if units:
        units = units.strip().lower()
    valid_units = {'standard', 'metric', 'imperial'}
    if units not in valid_units:
        error = f'Invalid units "{units}", it must be one of {valid_units}.'
        raise ValidationError(
            status_code=int(http.HTTPStatus.BAD_REQUEST), error_message=error
        )
    return city, country, units
