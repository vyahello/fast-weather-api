import time
import os

import pytest

from tests.api.fastweather import FastWeather
from weather.address import Address


def __run_in_background(command: str, startup_delay: int = 2) -> None:
    os.system(f'{command} /dev/null 2>&1 &')
    time.sleep(startup_delay)


def __kill_process(name: str, case_sensitive: bool = True) -> None:
    command = 'pkill'
    if case_sensitive:
        command += ' -i '
    os.system(f'{command} {name}')


@pytest.fixture()
def fastweather() -> FastWeather:
    return FastWeather(address=Address())


@pytest.fixture(scope='session')
def start_weather_server() -> None:
    __run_in_background(command='python -m weather')
    yield
    __kill_process(name='python')
