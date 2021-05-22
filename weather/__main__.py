"""Represents executable entrypoint for `weather` application."""
from weather.endpoint import Address
from weather.main import easyrun


if __name__ == '__main__':
    easyrun(address=Address())
