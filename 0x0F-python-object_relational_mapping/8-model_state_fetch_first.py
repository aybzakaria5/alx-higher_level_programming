#!/usr/bin/python3
"""Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the engine and bind it to the metadata of the Base class
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Check if a state is found
    if first_state:
        # Print the result
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        # If the table is empty, print "Nothing"
        print("Nothing")

    # Close the session
    session.close()
