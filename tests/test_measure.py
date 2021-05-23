import asyncio
from asyncio import Task
from typing import Generator
import time

import pytest

from tests.api.fastweather import FastWeather

pytestmark = [
    pytest.mark.asyncio,
    pytest.mark.usefixtures('start_weather_server'),
]


async def __requests(
    fastweather: FastWeather, amount: int
) -> Generator[Task, None, None]:
    return (
        asyncio.get_event_loop().create_task(fastweather.reports())
        for _ in range(amount)
    )


async def test_measure_concurrent_requests(fastweather: FastWeather) -> None:
    threshold_secs = 1
    start_time_secs = time.time()
    for task in await __requests(fastweather, amount=100):  # type: Task
        await task
    end_time_secs = time.time()
    assert end_time_secs < start_time_secs + threshold_secs
