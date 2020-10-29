import traceback
import jwt
import os
import requests
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from flask import Flask
from werkzeug.exceptions import Unauthorized

import logging


class Auth:
    def __init__(self, app: Flask):
        self.app = app
        self.audience = "api://900c0f30-448f-4276-82ff-d3ff88deffaa/persephone"
        self.azure_key_url = "https://login.microsoftonline.com/3aa4a235-b6e2-48d5-9195-7fcf05b459b0/discovery/v2.0/keys"
        self.key_cache = {}

    def authorize(self, request):
        try:
            authorization_header = request.headers["Authorization"]
        except KeyError as e:
            logging.error(traceback.format_exc())
            raise Unauthorized

        try:
            decoded_token = self.validate_token(authorization_header)
        except Exception as e:
            logging.error(traceback.format_exc())
            raise Unauthorized

    def validate_token(self, auth_header):
        """
        Extract bearer token from header and validate it with jwt.decode
        :param auth_header: Contains the Authorization header from the request
        :return: The decoded token
        """
        token = auth_header.split()[1]

        public_key = self.get_public_key(token)
        try:
            decoded_token = jwt.decode(
                token, public_key, algorithms=["RS256"], audience=self.audience
            )
        except Exception as e:
            logging.error(traceback.format_exc())
            raise Unauthorized
        return decoded_token

    def get_azure_key(self, kid):
        """
        Retrieve the relevant x5c key from Azure AD given the kid
        :param kid: Kid key from JWT header
        :return: x5c key from Azure AD
        """
        if kid not in self.key_cache:
            keys = requests.get(self.azure_key_url).json()["keys"]
            for key in keys:
                self.key_cache[key["kid"]] = key
                if key["kid"] == kid:
                    return key["x5c"][0]
        if kid not in self.key_cache:
            raise LookupError("The key list in azure contains no key with kid: " + kid)
        key = self.key_cache[kid]
        return key["x5c"][0]

    def get_public_key(self, token):
        """
        Retrieve the used "kid" from token header and retrieve corresponding certificate from Microsoft
        :param token: Bearer token
        :return: Public key certificate
        """
        token_header = jwt.get_unverified_header(token)
        key = self.get_azure_key(token_header["kid"])

        pem_start = "-----BEGIN CERTIFICATE-----\n"
        pem_end = "\n-----END CERTIFICATE-----\n"

        cert_str = pem_start + key + pem_end
        cert_obj = load_pem_x509_certificate(cert_str.encode("utf8"), default_backend())
        public_key = cert_obj.public_key()

        return public_key
