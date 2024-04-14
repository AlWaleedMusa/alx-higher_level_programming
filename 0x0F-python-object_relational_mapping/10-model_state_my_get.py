#!/usr/bin/python3
"""
Script that lists all State
objects that contain "a" from the
database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database)
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=state_name)[0]

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Not found")