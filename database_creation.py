import sqlite3

conn = sqlite3.connect(
  'banksystem.db'
) 
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE accounts
(id integer primary key, username text, 
email text, password text, balance real)''')
conn.commit()
conn.close()

