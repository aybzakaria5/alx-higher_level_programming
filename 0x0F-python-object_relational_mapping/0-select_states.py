#!/usr/bin/python3
"""List all the states from the database using MySQLdb."""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Connect to the database server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # Create a cursor
    cursor = db.cursor()

    # Define the query
    query = "SELECT * FROM states ORDER BY id ASC"

    # Execute the query
    cursor.execute(query)

    # Print the rows
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
