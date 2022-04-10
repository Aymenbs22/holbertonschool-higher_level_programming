#!/usr/bin/python3
"""script that adds the State object “Louisiana” to
the database hbtn_0e_6_usa"""


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
    newstate = State(name='Louisiana')
    session.add(newstate)
    session.commit()
    print(newstate.id)
    state = session.query(State).order_by(State.id)
    session.close()
