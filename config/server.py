from base64 import b64encode
from os import getenv, urandom


class Config(object):
    PORT = getenv("SERVER_PORT") or "5000"
    SECRET_KEY = b64encode(urandom(64)).decode('utf-8')
    JSON_SORT_KEYS = False
