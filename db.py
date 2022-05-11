import sqlite3

conn = sqlite3.connect('database.db')
print('Create & Connect database')

conn.execute(
create table menus (menu text)
)

conn.close()



