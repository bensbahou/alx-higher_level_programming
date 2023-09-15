#!/usr/bin/python3
"""  list all states with a name matching the argument """
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
    cur = db.cursor()
    cur.execute(
        """SELECT * FROM states WHERE name
        LIKE BINARY '{}'""".format(
            sys.argv[4]
        )
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()