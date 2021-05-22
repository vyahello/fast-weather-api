import pytest

from tests.api.fastweather import FastWeather

pytestmark = pytest.mark.asyncio


async def test_weather_city(fastweather: FastWeather) -> None:
    weather = await fastweather.city(city='lviv', country='ua')
    for value in 'temp', 'temp_min', 'temp_max':
        assert value in weather


async def test_reports(fastweather: FastWeather) -> None:
    assert await fastweather.reports()
