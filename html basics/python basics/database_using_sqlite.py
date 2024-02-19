import sqlite3

conn = sqlite3.connect('databases_examples')
cursor=conn.cursor()
print(cursor)
cursor.execute("create table test (name text, count integer)")
cursor.execute("insert into test (name, count) values ('Bob', 1)")
cursor.execute("insert into test (name, count) values (?, ?)",("Jill", 15))
result = cursor.execute("select * from test")
print(result.fetchall())