import pytest

from tests.api.fastweather import FastWeather
from weather.address import Address


@pytest.fixture()
async def fastweather() -> FastWeather:
    return FastWeather(address=Address())
