from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import Unauthorized, Forbidden


class AuthMiddleware:
    def __init__(self, app, auth):
        self.app = app
        self.auth = auth

    def __call__(self, environ, start_response):
        request = Request(environ)
        try:
            self.auth.authorize(request)
        except Unauthorized as e:
            response = Response("Authorization failed", status=401)
            return response(environ, start_response)

        except Forbidden as e:
            response = Response(
                "Your role does not grant access to this functionality", status=403
            )
            return response(environ, start_response)

        except Exception as e:
            response = Response("Authorization failed", status=401)
            return response(environ, start_response)

        return self.app(environ, start_response)
