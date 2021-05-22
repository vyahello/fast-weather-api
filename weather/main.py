"""Represents executable weather API."""
import asyncio
import json

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from weather import SETTINGS_PATH, STATIC_FILES_PATH
from weather.api import weather
from weather.endpoint import Address
from weather.models.location import Location
from weather.services import openweather, report
from weather.views import home


weather_app = fastapi.FastAPI()


def __configure_api_keys() -> None:
    if not SETTINGS_PATH.exists():
        raise FileNotFoundError(
            f'"{SETTINGS_PATH}" file not found, you cannot continue!'
        )
    with SETTINGS_PATH.open() as settings_stream:
        openweather.api_key = json.load(settings_stream).get('api_key')


def __configure_routing() -> None:
    weather_app.mount(
        path='/static',
        app=StaticFiles(directory=STATIC_FILES_PATH),
        name='static',
    )
    weather_app.include_router(home.router)
    weather_app.include_router(weather.router)


def __configure_fake_data() -> None:
    """

    This was added to make it easier to test the weather event reporting
    We have /api/reports but until you submit new data each run, it's missing
    So this will give us something to start from.
    """
    asyncio.run(
        report.add_report(
            'Misty sunrise today, beautiful!',
            Location(city='Lviv', country='UA'),
        )
    )
    asyncio.run(
        report.add_report(
            'Clouds over downtown.', Location(city='Kyiv', country='UA')
        )
    )


def easyrun(address: Address) -> None:
    __configure_routing()
    __configure_api_keys()
    __configure_fake_data()
    uvicorn.run(weather_app, host=address.host, port=address.port)
