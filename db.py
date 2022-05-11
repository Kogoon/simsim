import sqlite3

conn = sqlite3.connect('database.db')
print('Create & Connect Database')

conn.execute('create table menus (id num, menu text)')
print('Create Table')

conn.close()



