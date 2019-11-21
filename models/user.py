from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from config.db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


Base.metadata.create_all(engine)
