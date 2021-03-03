import json
import os
import sys
import getpass
from access.register_engine import hash_password
from access.check_engine import string_check
from access.register_engine import users_path


def get_user_data(username: str):
    try:
        with open(os.path.join(users_path, f'{username}.json')) as json_file:
            user_data = json.load(json_file)
    except IOError:
        print("Warning: auth file not found")
    return user_data


def login():
    """ logging dialog and routine
    : returns: users first_name"""
    print('Login now')
    username = input('username: ')
    username = username.strip()
    username_file = f'{username}.json'
    # check if user exists
    if username_file in os.listdir(users_path):
        user_data = get_user_data(username)
        if user_data:
            password = None
            iterations = 0
            while iterations < 3:
                print('you have %s remaining tries' % (3 - iterations))
                password = getpass.getpass('password:')
                hashed_password = hash_password(password)

                if hashed_password == user_data['password']:
                    break

                password = None
                iterations += 1
            if password:
                print('Nice to have you back Sir!')
                return user_data['first_name']
    else:
        print('Player not registered')


def player_auth():
    """performs auth for player 1 and 2
    :returns; player_1 first_name
    and players_2 first_name"""

    print('Player_1')
    player_1 = login()
    if not player_1:
        sys.exit(0)
    print('Player 2')
    player_2 = login()
    if not player_2:
        sys.exit(0)
    return player_1, player_2


def change_pass(username: str):
    """allows user to change password
    : param user: string user_name to change
    password"""
    user_data = get_user_data(username)
    if user_data:
        password = None
        iterations = 0
        while iterations < 3:
            print('you have %s remaining tries' % (3 - iterations))
            password = getpass.getpass('password:')
            hashed_password = hash_password(password)

            if hashed_password == user_data['password']:
                break

            password = None
            iterations += 1
        if password:
            new_password = None
            while not new_password or not string_check(new_password):
                new_password = getpass.getpass('new password: ')
                new_password_confirmation = getpass.getpass('confirm new password: ')
                if new_password != new_password_confirmation:
                    print('password not confirmed. Please try again')
                    new_password = None
                    continue
                if new_password == password:
                    print('New password must be different then old password!')
                    new_password = None
            user_data['password'] = hash_password(new_password)
            try:
                with open(os.path.join(users_path, f'{username}.json'), 'w') as json_file_w:
                    json_object = json.dumps(user_data)
                    json_file_w.write(json_object)
                    print('Password successfully changed')
            except IOError:
                print("Warning: auth file not found")
