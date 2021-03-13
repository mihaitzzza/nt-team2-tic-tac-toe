import json
import os
import getpass
from access.register_engine import hash_password
from access.check_engine import string_check
from access.register_engine import users_path, menu_register


def get_user_data(username: str):
    """loads user data from file type
    user.json
    : param : username type string
    : returns: user_data type dict"""
    try:
        with open(os.path.join(users_path, f'{username}.json')) as json_file:
            user_data = json.load(json_file)
    except IOError:
        print("Warning: auth file not found")
    return user_data


def check_password(word):
    """ checks if word is correct password
    : param : word type string
    : returns: boolean"""
    password = None
    iterations = 0
    while iterations < 3:
        print('you have %s remaining tries' % (3 - iterations))
        password = getpass.getpass('password:')
        hashed_password = hash_password(password)
        if hashed_password == word:
            break
        password = None
        iterations += 1
    if password:
        print('Nice to have you back Sir!')
        return True


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
            if check_password(user_data['password']):
                return user_data['first_name']
    else:
        print('Player not registered')


def login_player(player_id):
    """perform login for player
    : param: player_id type string can be player_1 or player_2
    : return: player name type string"""
    player = None
    for counter in range(0, 2):
        print(player_id)
        player = login()
        counter += 1
        if player:
            break
    if not player:
        menu_register()
    return player


def player_auth():
    """performs auth for player 1 and 2
    :returns; player_1 first_name
    and players_2 first_name"""
    player_1 = login_player('Player_1')
    player_2 = login_player('Player_2')
    return player_1, player_2


def change_password():
    """getting username from keyboard and transfer to
    change_pass() function"""
    user = input('Type username: ')
    if f'{user}.json' in os.listdir(users_path):
        change_pass(user)
    else:
        print('username does not exist')
        print('Please register')


def change_pass(username: str):
    """allows user to change password
    : param user: string user_name to change
    password"""
    user_data = get_user_data(username)
    if user_data:
        if check_password(user_data['password']):
            new_password = ''
            while not new_password or not string_check(new_password):
                new_password = getpass.getpass('new password: ')
                new_password_confirmation = getpass.getpass('confirm new password: ')
                if new_password != new_password_confirmation:
                    print('Password not confirmed!')
                    new_password = ''
                if hash_password(new_password) == user_data['password']:
                    print('Password must be different from old one')
                    new_password = ''
            user_data['password'] = hash_password(new_password)
            try:
                with open(os.path.join(users_path, f'{username}.json'), 'w') as json_file_w:
                    json_object = json.dumps(user_data)
                    json_file_w.write(json_object)
                    print('Password successfully changed')
            except IOError:
                print("Warning: auth file not found")
