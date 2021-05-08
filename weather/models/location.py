"""Module contains city/country location API."""
from pydantic import BaseModel


class Location(BaseModel):
    city: str
    country: str = 'US'
