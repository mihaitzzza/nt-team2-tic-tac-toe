import sys
import getpass
from access.check_engine import character_check, string_check, email_string_check
import os
import json
import hashlib
users_path = os.path.join('data', 'users')


def hash_password(word: str):
    """Returns the hashed version of a string
    """
    hash_tool = hashlib.sha1()
    encoded_pass = str(word).encode('utf-8')
    hash_tool.update(encoded_pass)
    return hash_tool.hexdigest()


def register():
    """creates folder username
    in folder data( can be used
    to store user activity and logging)
    and filename username.json
    with authentication credentials
    """
    print('To register please input:')
    print('-------------------------')
    first_name = ''
    while not character_check(first_name):
        first_name = input('First_name: ')
        first_name = first_name.strip()
        if character_check(first_name) is None:
            print('Characters not permitted')
    last_name = ''
    while not character_check(last_name):
        last_name = input('Last_name: ')
        last_name = last_name.strip()
        if character_check(last_name) is None:
            print('Characters not permitted ')
    print('user_name must be at least 6 char lower case letters, and at least 1 number')
    user_name = ''
    username_file = ''
    # check user_name format and user_name exist
    while not string_check(user_name) or username_file in os.listdir(users_path):
        user_name = input('User_name: ')
        user_name = user_name.strip()
        username_file = f'{user_name}.json'
        if string_check(user_name) is None:
            print('Wrong user_name! ')
        elif username_file in os.listdir(users_path):
            print('Username already used, try another! ')
    print('Clever choice for username!')
    email_address = ''
    while not email_string_check(email_address):
        email_address = input('Email_address: ')
        email_address = email_address.strip()
        if email_string_check(email_address) is None:
            print('Not valid email format ')
    print('password must be 6 char long, lower case, and at least 1 nr')
    password = ''
    password_confirmation = ''
    # check password format
    while not string_check(password) or password != password_confirmation:
        password = getpass.getpass('Password: ')
        password = password.strip()
        password_confirmation = getpass.getpass('Confirm_password: ')
        password_confirmation = password_confirmation.strip()
        if string_check(password) is None:
            print('Insecure password ')
        if password != password_confirmation:
            print('Password not confirmed')
    password = hash_password(password)
    user_data = {
        'first_name': first_name.strip(),
        'last_name': last_name.strip(),
        'user_name': user_name.strip(),
        'email_address': email_address.strip(),
        'password': password,
        'stats': {},

    }
    username_file_path = os.path.join(users_path, f'{user_name}.json')
    with open(username_file_path, 'w') as jason_file:
        json.dump(user_data, jason_file)
    print('Registration complete')


def menu_register():
    """display register or exit menu
    : param: player type string"""

    print("""\nPlease select option:
                        0 - EXIT
                        1 - REGISTER
                        """)
    sel = input("\nSelect option:\t")
    if sel == '1':
        register()
        sys.exit(0)
    elif sel != '1':
        sys.exit(0)
