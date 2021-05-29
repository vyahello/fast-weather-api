import os
import sys
import time

import pytest

from tests.api.fastweather import FastWeather
from weather.address import Address


def wait_for_socket(
    address: Address, ready: bool, timeout_secs: int = 5, poll_secs: int = 1
) -> None:
    """Waits for connection to be down."""
    end_time = time.time() + timeout_secs
    while end_time > time.time():
        curl_socket = (
            os.popen(f'curl {address.with_protocol()}').read().strip()
        )
        if ready:
            if curl_socket:
                break
            time.sleep(poll_secs)
        else:
            if not curl_socket:
                break
            time.sleep(poll_secs)
    else:
        raise TimeoutError(
            f'Unable to start communication with {address} '
            f'after {timeout_secs} seconds'
        )


def run_background_process(command: str) -> None:
    os.system(f'{command} /dev/null 2>&1 &')


def kill_process_pattern(pattern: str) -> None:
    os.system(f'kill -9 {int(os.popen(f"pgrep -f {pattern}").read().strip())}')


def kill_process(name: str, case_sensitive: bool) -> None:
    command = f'pkill {("", "-i")[case_sensitive]} {name}'
    os.system(command)


@pytest.fixture()
def address() -> Address:
    return Address()


@pytest.fixture()
def fastweather(address: Address) -> FastWeather:
    return FastWeather(address)


@pytest.fixture()
def start_weather_server(address: Address) -> None:
    run_background_process(command='python -m weather')
    wait_for_socket(address, ready=True)
    yield
    kill_process('python', case_sensitive=sys.platform == 'darwin')
    wait_for_socket(address, ready=False)
