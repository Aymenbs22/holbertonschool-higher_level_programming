#!/usr/bin/python3
"""prints the State object with the name passed as
argument from the database"""


import sqlalchemy
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    first = session.query(State).filter(State.name.like(argv[4]))
    i = 0
    for state in first:
        print("{}".format(state.id))
        i = 1
    if (i == 0):
        print("Not found")
    session.close()
