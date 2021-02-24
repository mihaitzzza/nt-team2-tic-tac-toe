import sys
import getpass
from access.check_engine import character_check, string_check, email_string_check
import os
import json
import hashlib


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
    first_name = input('First_name: ')
    while character_check(first_name) is None:
        print('Characters not permitted')
        first_name = input('First_name: ')
        first_name = first_name.strip()

    last_name = input('Last_name: ')
    while character_check(last_name) is None:
        print('Characters not permitted ')
        last_name = input('Last_name: ')
        last_name = last_name.strip()

    print('user_name must be at least 6 char lower case letters, and at least 1 number')
    user_name = input('User_name: ')
    user_name = user_name.strip()

    # check user_name format and user_name exist
    while string_check(user_name) is None or user_name in os.listdir(os.path.join('data', 'users')):
        if string_check(user_name) is None:
            print('Wrong user_name! ')
        else:
            print('Username already used, try another! ')
        user_name = input('User_name: ')
        user_name = user_name.strip()

    print('Clever choice for username!')

    email_address = input('Email_address: ')
    while email_string_check(email_address) is None:
        print('Not valid email format ')
        email_address = input('Email_address: ')
        email_address = email_address.strip()

    print('password must be 6 char long, lower case, and at least 1 nr')
    password = getpass.getpass('Password: ')
    password = password.strip()

    password_confirmation = getpass.getpass('Confirm_password: ')
    password_confirmation = password_confirmation.strip()

    # check password format
    while string_check(password) is None or password != password_confirmation:
        if string_check(password) is None:
            print('Insecure password ')
        else:
            print('Password not confirmed')

        password = getpass.getpass('Password:  ')
        password = password.strip()
        password_confirmation = getpass.getpass('Confirm_password: ')
        password_confirmation = password_confirmation.strip()

    password = hash_password(password)
    password_confirmation = hash_password(password_confirmation)

    while password != password_confirmation:  # check password confirmation
        print('Password not confirmed')
        password = getpass.getpass('Password:')
        password_confirmation = getpass.getpass('Confirm_password:')
        password = hash_password(password.strip())
        password_confirmation = hash_password(password_confirmation.strip())

    user_data = {
        'first_name': first_name.strip(),
        'last_name': last_name.strip(),
        'user_name': user_name.strip(),
        'email_address': email_address.strip(),
        'password': password,
        'stats': {},

    }
    with open(os.path.join('data', 'users', f'{user_name}.json'), 'w') as jason_file:
        json.dump(user_data, jason_file)
    print('Registration complete')


def menu_register(player: str):
    """display register or exit menu
    : param: player type string"""

    print('------------------------')
    print(f'{player} not registered!')
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
