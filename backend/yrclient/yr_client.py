import requests
import os

_WEATHER_FORECAST_ENDPOINT = "https://api.met.no/weatherapi/locationforecast/2.0/"

class YrClient:
    """
    Simple thin client for retrieving data from the YR end points.
    Returns the request response objects in full
    """
    def __init__(self):
        pass

    def compact_forecast(self, payload):
        endpoint = os.path.join(_WEATHER_FORECAST_ENDPOINT, "compact")
        res = requests.get(endpoint, params=payload)
        return res

    def ping(self):
        endpoint = os.path.join(_WEATHER_FORECAST_ENDPOINT, "status")
        res = requests.get(endpoint)
        return res
