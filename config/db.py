from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from os import path, makedirs


def root_dir():
    return path.dirname(path.dirname(__file__))


def check_path(directory):
    if not path.exists(directory):
        makedirs(directory)


def strip_slash(text):
    firstChar = text[0].strip("/")
    moreChars = text[1:]
    return firstChar + moreChars


db_provider = 'sqlite:////'
db_folder = 'database'
db_file = 'db.sqlite'

db_dir = path.join(root_dir(), db_folder)

check_path(db_dir)

db_path = path.join(db_dir, db_file)

db_uri = db_provider + strip_slash(db_path)

engine = create_engine(db_uri)

session_factory = sessionmaker(bind=engine)
