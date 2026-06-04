import sqlite3

conn = sqlite3.connect('student.db')

pikachu = conn.cursor()

pikachu.execute(''' SELECT name
FROM sqlite_master
WHERE type = 'table';''') # get the list of tables in the database
print(pikachu.fetchall())

pikachu.execute('''select * from students limit 5;''')
print(pikachu.fetchall()[1])

pikachu.execute("PRAGMA table_info('students');") # Get the columns names in the table
print(pikachu.fetchall())

pikachu.execute('''select concat(first_name, ' ', last_name) as full_name from students limit 5;''')
print(pikachu.fetchall())

conn.close()