# flake8: noqa
import pytest
from tests.markers import unit

pytestmark = unit


def test_me() -> None:
    assert True
