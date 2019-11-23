from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import get_sqlite_uri

db_uri = get_sqlite_uri(
    folder='database',
    file='db.sqlite')

engine = create_engine(db_uri)

session_factory = sessionmaker(bind=engine)
