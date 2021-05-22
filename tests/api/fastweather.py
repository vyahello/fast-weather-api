from typing import Dict, List, Union

from aiohttp import ClientSession

from weather.address import Address


class FastWeather:
    def __init__(self, address: Address) -> None:
        self._address = address

    async def city(self, city: str, country: str) -> Dict:
        return await self.__get(
            endpoint_path=f'/api/weather/{city}?country={country}'
        )

    async def reports(self) -> List[Dict]:
        return await self.__get(endpoint_path='/api/reports')

    async def __get(self, endpoint_path: str) -> Union[List, Dict]:
        async with ClientSession(
            raise_for_status=True
        ) as client:  # type: ClientSession
            async with client.get(
                f'{self._address.with_protocol()}{endpoint_path}'
            ) as response:
                return await response.json()
