#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[2],
        port=3306,
    )

    cur = db.cursor()
    cur.execute(
        """SELECT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states WHERE cities.state_id = state.id \
            ORDER BY cities.id ASC"""
    )
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
