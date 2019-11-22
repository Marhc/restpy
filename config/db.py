from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import get_db_uri

db_provider = 'sqlite:////'
db_folder = 'database'
db_file = 'db.sqlite'

db_uri = get_db_uri(db_provider, db_folder, db_file)

engine = create_engine(db_uri)

session_factory = sessionmaker(bind=engine)
