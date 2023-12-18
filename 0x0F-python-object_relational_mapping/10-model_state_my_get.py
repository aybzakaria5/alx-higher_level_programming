#!/usr/bin/python3
"""Script that prints the State object with the name passed as an argument
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

    # Query State object with the specified name
    search_stateBy_name = sys.argv[4]
    state = session.query(State).filter(
        State.name == search_stateBy_name).first()

    # Check if a state is found
    if state:
        # Print the result
        print(state.id)
    else:
        # If no state is found, print "Not found"
        print("Not found")

    # Close the session
    session.close()
