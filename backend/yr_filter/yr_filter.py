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
