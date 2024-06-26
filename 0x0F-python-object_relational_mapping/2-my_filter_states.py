#!/usr/bin/python3
"""
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
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

    search = sys.argv[4]

    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE Binary name="{}"'.format(search))
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
