from flask_restx import Namespace, Resource, fields

api = Namespace(
    "example_namespace",
    description="An example to demonstrate flask-restx functionality",
)

hello_world_model = api.model(
    "hello_world", {"value": fields.String(example="Hello World")}
)


@api.route("/hello-world", doc={"description": "Ask the API to say hello to the world"})
class HelloWorld(Resource):
    @api.response(200, "Success", hello_world_model)
    def get(self):
        return {"value": "Hello World"}
