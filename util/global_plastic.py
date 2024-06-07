from typing_extensions import Any, List


class UtilsGlobalPlastic:
    @staticmethod
    def filter_sites_by_country(sites: Any, country: str = 'Brazil') -> List[Any]:
        return list(filter(lambda site: site["properties"]["country"] == country, sites["features"]))
