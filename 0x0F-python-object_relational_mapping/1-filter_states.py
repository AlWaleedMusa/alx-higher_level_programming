#!/usr/bin/python3
"""
lists all states starting with (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )

    crs = db.cursor()
    crs.execute(
        "SELECT * FROM states WHERE BINARY name\
            LIKE 'N%' ORDER BY states.id"
        )
    data = crs.fetchall()

    for row in data:
        print(row)
    crs.close()
    db.close()
