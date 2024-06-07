from typing_extensions import Any
import httpx
from config.env import env

class ProviderGlobalPlastic:
    @staticmethod
    async def getSites() -> Any:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f'{env["providers"]["global_plastic"]["global_plastic_url"]}/sites', params=[('apikey', env["providers"]["global_plastic"]["global_plastic_api_key"])])
                if response.status_code == 200:
                    return response.json()
                return {"mensagem": "Erro ao efetuar chamada global plastic.", "status_code": response.status_code}
        except Exception as error:
            return {"error": str(error)}
