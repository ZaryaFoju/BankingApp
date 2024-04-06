import sqlite3

connection = sqlite3.connect('banksystem.db')
cursor = connection.cursor()

def display_menu(username):
    print('Welcome,', username)
    print('')
    print('========================')
    print('Menu: Banking Account')
    print('1. Delete Account')
    print('2. Check Balance')
    print('3. Deposit')
    print('4. Withdraw')
    print('5. Modify Account')
    print('========================')

def create_account(username, email, password, balance):
    cursor.execute('''INSERT INTO accounts (username, email, password, balance) VALUES (?, ?, ?, ?)''',
                   (username, email, password, balance))
    connection.commit()

def delete_account(username):
    cursor.execute('''DELETE FROM accounts WHERE username = ?''', (username,))
    connection.commit()

def check_balance():
    password = input('Type in the password for your account: ')
    cursor.execute('''SELECT password, balance FROM accounts WHERE username = ?''', (username,))
    result = cursor.fetchone()
    if result and result[0] == password:
        print('Your balance:', result[1])
    else:
        print('Incorrect password, try again or select another option')

def deposit(username):
    amount = float(input('Enter the amount you want to deposit: '))
    cursor.execute('''SELECT balance FROM accounts WHERE username = ?''', (username,))
    balance = cursor.fetchone()[0]
    new_balance = balance + amount
    cursor.execute('''UPDATE accounts SET balance = ? WHERE username = ?''', (new_balance, username))
    connection.commit()
    print('Deposit successful. New balance:', new_balance)

def withdraw(username):
  amount = float(input('Enter the amount you want to withdraw: '))
  cursor.execute('''SELECT balance FROM accounts WHERE username = ?''', (username,))
  balance = cursor.fetchone()[0]
  new_balance = balance - amount
  cursor.execute('''UPDATE accounts SET balance = ? WHERE username = ?''', (new_balance, username))
  connection.commit()
  print('Withdraw successful. New balance:', new_balance)

def modify_account(username):
  modifyAcc = input('Enter what you want to modify in the account: ')
  replace = input('Enter value to replace it: ')
  cursor.execute("PRAGMA table_info(accounts)")
  columns = [col[1] for col in cursor.fetchall()]
  if modifyAcc not in columns:
      print("Invalid column name. Please enter a valid column name.")
      return
  query = f'''UPDATE accounts SET {modifyAcc} = ? WHERE username = ?'''
  cursor.execute(query, (replace, username))
  connection.commit()
  print('Data has been modified.')

def fetch_all_accounts():
    cursor.execute('SELECT * FROM accounts')
    print(cursor.fetchall())


username = input('Type in the username for the account: ')
cursor.execute('SELECT username FROM accounts WHERE username = ?', (username,))
usernames = cursor.fetchall()

hasAcc = False
for user in usernames:
    if user[0] == username:
        hasAcc = True
        break

if not hasAcc:
    print('Username is not in the database')
    createacc = input('Would you like to create an account? (y/n): ')
    if createacc.lower() in ['y', 'yes']:
        email = input('Type in the email for the account: ')
        password = input('Type in the password for the account: ')
        balance = float(input('Type in the initial balance for the account: '))
        create_account(username, email, password, balance)
        fetch_all_accounts()
    else:
        print('Thank you for using our bank!')
        print('Goodbye!')
        exit()

display_menu(username)
menu_option = int(input('Please select one of the options for your account: '))

while menu_option < 6 and menu_option > 0:
    if menu_option == 1:
        delete_account(username)
    elif menu_option == 2:
        check_balance()
    elif menu_option == 3:
        deposit(username)
    elif menu_option == 4:
        withdraw(username)
    elif menu_option == 5:
      modify_account(username)
        
    menu_option = int(input('Please select another option for your account or exit: '))

connection.close()
print('Thank you for using our bank!')
print('Goodbye!')