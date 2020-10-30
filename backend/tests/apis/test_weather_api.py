class TestWeather:
    def test_weather_endpoint(self, test_client):
        response = test_client.get(
            "/persephone/weather/current-temperature",
            query_string={"latitude": 10, "longitude": 10.1},
        )
        assert isinstance(response.json, float)
