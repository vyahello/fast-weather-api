from typing import Dict, List, Union

from aiohttp import ClientSession

from weather.address import Address


class FastWeather:
    def __init__(self, address: Address) -> None:
        self._address = address.with_protocol()

    async def reports(self) -> List[Dict]:
        return await self.__get(endpoint_path='/api/reports')

    async def __get(self, endpoint_path: str) -> Union[List, Dict]:
        async with ClientSession(
            raise_for_status=True
        ) as client:  # type: ClientSession
            async with client.get(
                f'{self._address}{endpoint_path}'
            ) as response:
                return await response.json()
