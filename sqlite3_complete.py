#!/usr/bin/python
import sqlite3 as lite
import sys

def get_csv_headers(data):
    headers = ""
    for x in range (0, len(cur.description)):
        headers += cur.description[x][0] + ','
    return headers[:-1]

def to_csv(csv, data):
    for row in data:
        csv += '\n'
        for col in row:
            csv += str(col) + ','
        csv = csv[:-1]
    return csv

def get_meta_data(cur, table_name):
    cur.execute('PRAGMA table_info(' + table_name + ')')
    data = cur.fetchall()
    return to_csv("Metadata:", data)

def get_tables():
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    data = cur.fetchall()
    return to_csv("Tables:", data)

def connect(dbname):
    return lite.connect(dbname)

def test(cur):
    cur.execute("create table songs( id int(10), track_name varchar(100))")
    cur.execute("insert into songs values(1, 'Wrong')")
    cur.execute("insert into songs values(2, 'Blind')")
    cur.execute('select * from songs')
    data = cur.fetchall()
    headers = get_csv_headers(data)

    print "data: \n" + to_csv(headers, data)
    print get_meta_data(cur, 'songs')
    print get_tables()
    cur.execute("drop table songs")

if __name__ == "__main__":
    try:
        dbname = sys.argv[1]
    except:
        print "usage: command (dbname)"
        sys.exit(1)

    print(dbname)
    con = connect(dbname)
    cur = con.cursor()
    try:
        test(cur)
    finally:
        con.close() 
