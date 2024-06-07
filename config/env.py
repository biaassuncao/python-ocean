from dotenv import load_dotenv, dotenv_values

load_dotenv()
_config = dotenv_values(".env")
env = {
    "providers": {
        "global_plastic": {
            "global_plastic_url": _config["URL_GLOBAL_PLASTIC"],
            "global_plastic_api_key": _config["URL_GLOBAL_PLASTIC_API_KEY"],
        },
        "graphhopper": {
            "graphhopper_url": _config["URL_GRAPHHOPPER"],
            "graphhopper_api_key": _config["URL_GRAPHHOPPER_API_KEY"],
        },
    },
}