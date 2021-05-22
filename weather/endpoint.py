"""Represents weather API entrypoint."""
from dataclasses import dataclass


@dataclass
class WeatherEndpoint:
    host: str = '0.0.0.0'
    port: int = 4444
