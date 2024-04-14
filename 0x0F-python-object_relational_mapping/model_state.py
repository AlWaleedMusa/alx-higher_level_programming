#!/usr/bin/python3
"""Start link class to table in database"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """
        State class inherits from base
    """
    __tablename__ = "states"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
