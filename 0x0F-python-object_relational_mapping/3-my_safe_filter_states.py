#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But this time, write one that
is safe from MySQL injections!
"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    # Connect to the database server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    wanted_state = argv[4]
    # Create a cursor
    cursor = db.cursor()
    # Using parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (wanted_state,))
    # Fetch all the rows
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
