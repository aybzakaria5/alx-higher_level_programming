#!/usr/bin/python3
"""using inner join to  lists all cities from the database """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    # create a cursor
    cur = db.cursor()
    # define and excute the query
    cur.execute("""SELECT cities.id, cities.name, states.name
              FROM cities
              INNER JOIN states ON states.id=cities.state_id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
