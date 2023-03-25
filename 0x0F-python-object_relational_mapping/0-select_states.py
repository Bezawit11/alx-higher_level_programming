#!/usr/bin/python3


import MySQLdb
from sys import argv

'''a script that lists all states from 
a database
'''
if __name__ == "__main__":
    db_connection= MySQLdb.connect((host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1])
    cursor.close()
    db_connection.close()

