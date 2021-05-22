import pytest

from weather.address import Address


@pytest.fixture()
def address() -> Address:
    return Address()


def test_host(address: Address) -> None:
    assert address.host == '0.0.0.0'


def test_port(address: Address) -> None:
    assert address.port == 4444


def test_address_as_str(address: Address) -> None:
    assert str(address) == '0.0.0.0:4444'


def test_address_with_protocol(address: Address) -> None:
    assert address.with_protocol(protocol='https') == 'https://0.0.0.0:4444'
