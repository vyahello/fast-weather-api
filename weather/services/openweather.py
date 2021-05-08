from typing import Optional
import httpx

api_key: Optional[str] = None


async def get_report_async(
    city: str, state: Optional[str], country: str, units: str
) -> dict:
    query = (f'{city},{country}', f'{city},{state},{country}')[bool(state)]

    url = (
        f'https://api.openweathermap.org/data/2.5/weather?q={query}'
        f'&appid={api_key}&units={units}'
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

    data = response.json()
    forecast = data['main']
    return forecast
