from flask import Flask
from flask_restx import Api
from apis.weather import api as weather_api


def create_app():
    api = Api(
        title="Persephone API",
        version="0.1",
        description="Persephone backend API for SI Challenge 2020.4",
    )

    app = Flask(__name__)
    api.init_app(app)

    api.add_namespace(weather_api, path="/persephone/weather")

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(debug=True, host="0.0.0.0", port=8000)
