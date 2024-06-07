from typing_extensions import Any, List
from typing import Union
from fastapi import FastAPI
import asyncio
from util.global_plastic import UtilsGlobalPlastic
from providers.global_plastic import ProviderGlobalPlastic
from providers.graphhopper import ProviderGraphhopper

app = FastAPI()

async def formatResponse(sites: List[Any]) -> List[Any]:
    tasks = [ProviderGraphhopper.geocoding(site["properties"]["place_name"]) for site in sites]
    geocodes = await asyncio.gather(*tasks)
    response = []
    for i, site in enumerate(sites):
        hit = geocodes[i]["hits"][0]
        response.append({
            "localizacao": {
                "country": hit.get("country", ""),
                "cep": hit.get("postcode", ""),
                "estado": hit.get("state", ""),
                "cidade": hit.get("city", ""),
                "logradouro": hit.get("name", ""),
            },
            "populacao_area": {
                "1km": site["properties"].get("Population - 1 km", ""),
                "5km": site["properties"].get("Population - 5 km", ""),
                "10km": site["properties"].get("Population - 10 km", "")
            },
            "area": {
                "geometry": {
                    "type": site["geometry"].get("type"),
                    "coordinates": [
                        site["geometry"]["coordinates"][0],
                        site["geometry"]["coordinates"][1]
                    ]
                }
            },
            "risco": site["properties"]["risk"]
        })
    return response

@app.get("/location/pollution/{country}")
async def locationPollution(country: str):
    try:
        sites = await ProviderGlobalPlastic.getSites()
        sitesByCountry = UtilsGlobalPlastic.filter_sites_by_country(sites, country)

        mapResponse = await formatResponse(sitesByCountry)
        return mapResponse
    except Exception as error:
        return {"error": str(error)}
