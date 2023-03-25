#!/usr/bin/python3
'''a script that lists all states from 
a database
'''

import MySQLdb
from sys import argv
import re
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], password=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC WHERE name=argv[4]")
    rows = cursor.fetchall()
    for row in rows:
        if row[1].startswith('N'):
            print(row)
    cursor.close()
    db.close()
