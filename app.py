from flask import Flask
from flask_sqlalchemy_session import flask_scoped_session

from config.api import api
from config.db import session_factory
from config.server import Config

app = Flask(__name__)

app.config.from_object(Config)

api.init_app(app)

session = flask_scoped_session(session_factory, app)

if __name__ == "__main__":
    app.run(
        port=app.config["PORT"],
        load_dotenv=False
    )
