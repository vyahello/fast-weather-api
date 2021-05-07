"""Represents executable entrypoint for `weather` application."""
import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from weather import (
    SETTINGS_PATH,
    STATIC_FILES_PATH,
    WEATHER_HOST,
    WEATHER_PORT,
)
from weather.views import home

weather_app = fastapi.FastAPI()


def __configure_api_keys() -> None:
    if not SETTINGS_PATH.exists():
        raise FileNotFoundError(
            f'"{SETTINGS_PATH}" file not found, you cannot continue!'
        )


def __configure_routing() -> None:
    weather_app.mount(
        path='/static',
        app=StaticFiles(directory=STATIC_FILES_PATH),
        name='static',
    )
    weather_app.include_router(home.router)


def easyrun(host: str = WEATHER_HOST, port: int = WEATHER_PORT) -> None:
    __configure_routing()
    __configure_api_keys()
    uvicorn.run(weather_app, host=host, port=port)


if __name__ == '__main__':
    easyrun()
