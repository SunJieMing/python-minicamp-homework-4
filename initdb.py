import sqlite3

connection = sqlite3.connect('movies.db')
print('Opened database successfully');

connection.execute('CREATE TABLE movies (title TEXT, year TEXT, lead_actor TEXT)')
print('Table created successfully');

connection.close()
