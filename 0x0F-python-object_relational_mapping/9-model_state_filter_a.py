#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database"""


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
    first = session.query(State).filter(State.name.like('%a%'))
    for i in first:
        print("{}: {}".format(i.id, i.name))
    session.close()
