import json
import os
from access.check_engine import character_check, string_check, email_string_check
import os.path
from access.register_engine import hash_password, menu_register
import getpass
import sys


def login():
    """ logging dialog and routine
    : returns: users first_name"""
    print('login now')
    username = input('username: ')
    username = username.strip()
    users_path = os.path.join('data', 'users')
    username_file_path = os.path.join(users_path, f'{username}.json')
    username_file = f'{username}.json'
    # check if user exists
    if username_file in os.listdir(users_path):
        password = getpass.getpass('password: ')
        password = password.strip()
        try:
            with open(username_file_path) as json_file:
                credentials_f = json.load(json_file)
                credentials_f = dict(credentials_f)
                #  check password
                while hash_password(password) != credentials_f['password']:
                    print('Wrong password')
                    password = getpass.getpass('password: ')
                    password = password.strip()
                else:
                    print('Nice to have you back Sir!')
                    return str(credentials_f['first_name'])
        except IOError:
            print("Warning: auth file not found")

    else:
        print('username does not exist')
        return None


def player_auth():
    """performs auth for player 1 and 2
    :returns; player_1 first_name
    and players_2 first_name"""

    print('Player_1')
    player_1 = login()
    while player_1 is None:
        menu_register('Player_1')
    print('Player 2')
    player_2 = login()
    while player_2 is None:
        menu_register('Player_2')
    return player_1, player_2


def change_pass(user: str):
    """allows user to change password
    : param user: string user_name to change
    password"""
    users_path = os.path.join('data', 'users')
    username_file_path = os.path.join(users_path, f'{user}.json')
    username_file = f'{user}.json'
    if username_file in os.listdir(users_path):
        password = getpass.getpass('password: ')
        password = password.strip()
        try:
            with open(username_file_path) as json_file:
                credentials_f = json.load(json_file)
                credentials_f = dict(credentials_f)
                #  check password
                while hash_password(password) == credentials_f['password']:
                    print('password must be 6 char long, lower case, and at least 1 nr')
                    new_pass = getpass.getpass('Type new password: ')
                    new_pass = new_pass.strip()
                    password_confirmation = getpass.getpass('Confirm new_password: ')
                    password_confirmation = password_confirmation.strip()
                    while string_check(new_pass) is None or new_pass != password_confirmation:
                        if string_check(new_pass) is None:
                            print('Insecure password ')
                        else:
                            print('Password not confirmed')
                        new_pass = getpass.getpass('Type new password: ')
                        new_pass = new_pass.strip()
                        password_confirmation = getpass.getpass('Confirm new_password: ')
                        password_confirmation = password_confirmation.strip()
                    else:
                        print('pass is good')
                        credentials_f['password'] = hash_password(new_pass)
                    with open(os.path.join('data', 'users', f'{user}.json'), 'w') as json_file_w:
                        json_object = json.dumps(credentials_f)
                        json_file_w.write(json_object)
                        print('Password successfully changed')
                else:
                    print('Wrong password')
                    sys.exit(0)
        except IOError:
            print("Warning: auth file not found")
