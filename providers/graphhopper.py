from typing_extensions import Any
import httpx
from config.env import env

class ProviderGraphhopper:
    @staticmethod
    async def geocoding(query: str) -> Any:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f'{env["providers"]["graphhopper"]["graphhopper_url"]}/geocode', params=[('key', env["providers"]["graphhopper"]["graphhopper_api_key"]), ('q', query)])
                if response.status_code == 200:
                    return response.json()
                return {"mensagem": "Erro ao efetuar chamada graphhopper.", "status_code": response.status_code}
        except Exception as error:
            return {"error": str(error)}
