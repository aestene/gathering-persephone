from flask_restx import Namespace, Resource
from flask import request
from yr_filter.yr_filter import YrFilter

api = Namespace(
    "Weather",
    description="Retrieve weather data from Yr",
)


@api.route(
    "/current-temperature", doc={"description": "provides the current temperature"}
)
@api.doc(
    params={
        "longitude": "Longitude location coordinate",
        "latitude": "Latitude location coordinate",
    }
)
class CurrentTemperature(Resource):
    @api.response(200, "Success")
    def get(self):
        longitude: float = request.args.get("longitude")
        latitude: float = request.args.get("latitude")

        yr_filter = YrFilter()
        temperature = yr_filter.get_current_temperature(longitude, latitude)
        return temperature


@api.route(
    "/compact-forecast",
    doc={"description": "Returns a compact weather forecast for four timepoints"},
)
@api.doc(
    params={
        "longitude": "Longitude location coordinate",
        "latitude": "Latitude location coordinate",
    }
)
class CompactForecast(Resource):
    @api.response(200, "Success")
    def get(self):
        longitude: float = request.args.get("longitude")
        latitude: float = request.args.get("latitude")

        yr_filter = YrFilter()
        compact_forecast = yr_filter.get_compact_forecast(longitude, latitude)
        return compact_forecast


@api.route(
    "/compact-forecast_icon",
    doc={"description": "Returns a compact weather forecast icons for four timepoints"},
)
@api.doc(
    params={
        "longitude": "Longitude location coordinate",
        "latitude": "Latitude location coordinate",
    }
)
class CompactForecast(Resource):
    @api.response(200, "Success")
    def get(self):
        longitude: float = request.args.get("longitude")
        latitude: float = request.args.get("latitude")

        yr_filter = YrFilter()
        compact_forecast = yr_filter.get_compact_forecast_icon(longitude, latitude)
        return compact_forecast
