from yrclient.yr_client import YrClient
import json


class YrFilter:
    def __init__(self):
        self.yr_client = YrClient()

    def get_current_temperature(self, latitude: float, longitude: float) -> float:
        binary_data = self.yr_client.compact_forecast(
            {"lat": latitude, "lon": longitude}
        )
        data = json.loads(binary_data.content.decode())
        properties = data["properties"]
        temperature = properties["timeseries"][0]["data"]["instant"]["details"][
            "air_temperature"
        ]

        return temperature

    def get_compact_forecast(self, latitude: float, longitude: float):
        binary_data = self.yr_client.compact_forecast(
            {"lat": latitude, "lon": longitude}
        )
        data = json.loads(binary_data.content.decode())

        pick = [0, 3, 6, 12]
        forecast = []
        for index in pick:
            entry = data["properties"]["timeseries"][index]
            forecast.append({entry["time"]: entry["data"]["instant"]})

        return forecast

    def get_compact_forecast_icon(self, latitude: float, longitude: float):
        binary_data = self.yr_client.compact_forecast(
            {"lat": latitude, "lon": longitude}
        )
        data = json.loads(binary_data.content.decode())

        pick = [0, 3, 6, 12]
        forecast = []
        for index in pick:
            entry = data["properties"]["timeseries"][index]
            forecast.append({entry["time"]: entry["data"]["next_1_hours"]["summary"]})

        return forecast
