from flask import Flask
from flask_restx import Api
from backend.apis.example_namespace import api as example_api


def create_app():
    api = Api(
        title="Persephone API",
        version="0.1",
        description="Persephone backend API for SI Challenge 2020.4",
    )

    app = Flask(__name__)
    api.init_app(app)

    api.add_namespace(example_api)

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(debug=True, host="0.0.0.0", port=8000)
