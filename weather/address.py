"""Represents weather API address."""
from dataclasses import dataclass


@dataclass
class Address:
    host: str = '0.0.0.0'
    port: int = 4444

    def with_protocol(self, protocol: str = 'http') -> str:
        return f'{protocol}://{self}'

    def __str__(self) -> str:
        return f'{self.host}:{self.port}'
