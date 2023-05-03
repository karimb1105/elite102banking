# Users need to have an account number and PIN to identify themselves as owners of an account.
# Once users get into the system they will have standard options: check balance, deposit, and withdraw. 
# Additionally, a new user or bank administrator can also create a new account, close account, 
# and modify an account (such as edit name, PIN, or any other personal identification required to open an account).

import random

# dictionary
accounts = {}

def create_account():
    """Create a new account for a user."""
    account_number = str(random.randint(10000, 99999))
    pin = str(random.randint(1000, 9999))
    accounts[account_number] = {'pin': pin, 'balance': 0}
    print(f'Account created successfully!\nAccount number: {account_number}\nPIN: {pin}')

def close_account(account_number, pin):
    """Close an existing account."""
    if account_number in accounts and accounts[account_number]['pin'] == pin:
        del accounts[account_number]
        print('Account closed successfully!')
    else:
        print('Invalid account number or PIN.')

def check_balance(account_number, pin):
    """Check the balance of an existing account."""
    if account_number in accounts and accounts[account_number]['pin'] == pin:
        balance = accounts[account_number]['balance']
        print(f'Your balance is: {balance}')
    else:
        print('Invalid account number or PIN.')

def deposit(account_number, pin, amount):
    """Deposit money into an existing account."""
    if account_number in accounts and accounts[account_number]['pin'] == pin:
        accounts[account_number]['balance'] += amount
        print(f'Deposit of {amount} successful!\nYour balance is now: {accounts[account_number]["balance"]}')
    else:
        print('Invalid account number or PIN.')

def withdraw(account_number, pin, amount):
    """Withdraw money from an existing account."""
    if account_number in accounts and accounts[account_number]['pin'] == pin:
        if accounts[account_number]['balance'] < amount:
            print('Insufficient balance!')
        else:
            accounts[account_number]['balance'] -= amount
            print(f'Withdrawal of {amount} successful!\nYour balance is now: {accounts[account_number]["balance"]}')
    else:
        print('Invalid account number or PIN.')

def modify_account(account_number, pin, name=None, new_pin=None):
    """Modify an existing account."""
    if account_number in accounts and accounts[account_number]['pin'] == pin:
        if name:
            accounts[account_number]['name'] = name
        if new_pin:
            accounts[account_number]['pin'] = new_pin
        print('Account modified successfully!')
    else:
        print('Invalid account number or PIN.')

