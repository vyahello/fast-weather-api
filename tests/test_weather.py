import pytest

from tests.api.fastweather import FastWeather

pytestmark = pytest.mark.asyncio


async def test_reports(fastweather: FastWeather) -> None:
    assert await fastweather.reports()
