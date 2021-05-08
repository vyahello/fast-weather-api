"""Represents executable entrypoint for `weather` application."""
import json
from dataclasses import dataclass

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from weather import (
    SETTINGS_PATH,
    STATIC_FILES_PATH,
    WEATHER_HOST,
    WEATHER_PORT,
)
from weather.api import weather
from weather.services import openweather
from weather.views import home


weather_app = fastapi.FastAPI()


@dataclass
class WeatherEndpoint:
    host: str = WEATHER_HOST
    port: str = WEATHER_PORT


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


def easyrun(endpoint: WeatherEndpoint = WeatherEndpoint()) -> None:
    __configure_routing()
    __configure_api_keys()
    uvicorn.run(weather_app, host=endpoint.host, port=endpoint.port)


if __name__ == '__main__':
    easyrun()
