"""Module contains caching API."""
import datetime
from typing import Optional, Tuple

__cache = {}
lifetime_in_hours: float = 1.0


def get_weather(city: str, country: str, units: str) -> Optional[dict]:
    key: tuple = __create_key(city, country, units)
    data: dict = __cache.get(key)
    if not data:
        return None

    last = data['time']
    date = datetime.datetime.now() - last
    if date / datetime.timedelta(minutes=60) < lifetime_in_hours:
        return data['value']

    del __cache[key]
    return None


def set_weather(city: str, country: str, units: str, value: dict) -> None:
    key = __create_key(city, country, units)
    data = {
        'time': datetime.datetime.now(),
        'value': value
    }
    __cache[key] = data
    __clean_out_of_date()


def __create_key(
        city: str, country: str, units: str) -> Tuple[str, str, str]:
    if not city or not country or not units:
        raise Exception("City, country, and units are required")

    return city.strip().lower(), country.strip().lower(), units.strip().lower()


def __clean_out_of_date() -> None:
    for key, data in list(__cache.items()):
        date = datetime.datetime.now() - data.get('time')
        if date / datetime.timedelta(minutes=60) > lifetime_in_hours:
            del __cache[key]
