#!/usr/bin/python3
"""
prints all City objects from
the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
