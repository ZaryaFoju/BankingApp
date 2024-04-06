import sqlite3

connection = sqlite3.connect('banksystem.db')
cursor = connection.cursor()

def create_account(username, email, password, balance):
  cursor.execute(
      '''INSERT INTO accounts (username, 
email, password, balance) VALUES (?, ?, ?, ?)''',
      (username, email, password, balance))
  connection.commit()


def fetch_all_accounts():
  cursor.execute('SELECT * FROM accounts')
  print(cursor.fetchall())





username = input('Type in the username for the account: ')

if username != cursor.execute('SELECT username FROM accounts WHERE username = ?', (username,)):
  print('Username is not in the database')
  createacc = input('Would you like to create an account? (y/n): ')
  if createacc == 'y':
    email = input('Type in the email for the account: ')
    password = input('Type in the password for the account: ')
    balance = float(input('Type in the inital balance for the account: '))
    create_account(username, email, password, balance)
    fetch_all_accounts()
  else:
    print('Have a good day. Goodbye.')

connection.close()