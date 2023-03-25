#!/usr/bin/python3
'''a script that lists all states from a database hbtn_0e_0_usa '''

import MySQLdb
from sys import argv
def mysqlconnect():
    '''   '''
    db_connection= MySQLdb.connect((host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1])
    cursor.close()
    db_connection.close()

if __name__ == '__main__':
    mysqlconnect()
