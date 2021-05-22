"""Represents executable entrypoint for `weather` application."""
from weather.endpoint import WeatherEndpoint
from weather.main import easyrun


if __name__ == '__main__':
    easyrun(endpoint=WeatherEndpoint())
