from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from os import path


def root_dir():
    return path.dirname(path.dirname(__file__))


def strip_slash(text):
    firstChar = text[0].strip("/")
    moreChars = text[1:]
    return firstChar + moreChars


database_path = path.join(root_dir(), 'database', 'db.sqlite')

database_uri = 'sqlite:////' + strip_slash(database_path)

engine = create_engine(database_uri)

session_factory = sessionmaker(bind=engine)
