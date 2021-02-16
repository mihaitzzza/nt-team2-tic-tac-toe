import json
import os
import os.path
import hashlib
import getpass


def hash_password(p):
    """Returns the hashed version of a string
    """
    m = hashlib.sha1()
    pas = str(p).encode('utf-8')
    m.update(pas)
    return m.hexdigest()


def register():
    """creates folder username
    in folder data( can be used
    to store user activity and loggins)
    and filename username.json
    with authentication credentials
    """
    # check if folder data exists if not it wil be created
    if 'data' not in os.listdir('game'):
        os.mkdir(os.path.join('game', 'data'))

    print('To register please input:')
    first_name = input('First_name: ')
    last_name = input('Last_name: ')

    print('user_name must be at least 6 char lower case letters, and at least 1 nr')
    user_name = input('User_name: ')
    user_name = user_name.strip()
    # check user_name format
    while not (len(user_name) >= 6 and user_name.isalnum() and not (user_name.isalpha() or user_name.isnumeric())):
        print('Wrong user_name ')
        user_name = input('User_name: ')
        user_name = user_name.strip()

    else:
        print('user_name is good')
    # check user_name exist
    while user_name in os.listdir(os.path.join('game', 'data')):  # check if already exists
        print('Username already used, try another')
        user_name = input('User_name: ')

    email_address = input('Email_address: ')

    print('password must be 6 char long, lower case, and at least 1 nr')
    password = getpass.getpass('Password: ')
    password = password.strip()

    # check password format
    while not (len(password) >= 6 and password.isalnum() and not (password.isalpha() or password.isnumeric())):
        print('Insecure password ')
        password = getpass.getpass('Password:  ')
        password = password.strip()

    else:
        print('pass is good')

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

    else:
        # create user auth file
        os.mkdir(os.path.join('game', 'data', str(user_name)))
        user_data = {
            'first_name': first_name.strip(),
            'last_name': last_name.strip(),
            'user_name': user_name.strip(),
            'email_address': email_address.strip(),
            'password': password,

        }
        with open(os.path.join('game', 'data', str(user_name), f'{user_name}.json'), 'w') as jason_file:
            json.dump(user_data, jason_file)


def loggin():
    """ logging dialog and routine
    : returns: users first_name"""
    print('login now')
    user = input('username: ')
    user = user.strip()
    user = str(user)

    # check if user exists
    if user in os.listdir(os.path.join('game', 'data')):
        pasw = getpass.getpass('password: ')
        pasw = pasw.strip()
        try:
            with open(os.path.join('game', 'data', str(user), f'{user}.json')) as json_file:
                credentials_f = json.load(json_file)
                credentials_f = dict(credentials_f)

                #  check password
                if hash_password(pasw) == credentials_f['password']:
                    print('Nice to have you back Sir!')
                    return str(credentials_f['first_name'])
                else:
                    print('Wrong password')
                    while True:
                        print("""\n Select:
                                               0 - EXIT
                                               1 - TRY AGAIN 
                                               """)
                        s = input()
                        if s == '1':
                            return loggin()
                        else:
                            exit(0)

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
    player_1 = loggin()
    if player_1 is not None:
        print('Player_2')
        player_2 = loggin()
        if player_2 is not None:
            return player_1, player_2
        else:
            print("""\nPlease select option:
            0 - EXIT
            1 - REGISTER
            """)
            sel = input("\nSelect option:\t")
            if sel == '1':
                register()
            elif sel != 1:
                exit(0)
            print('Player 2')
            player_2 = loggin()
        return player_1, player_2
    else:
        print("""\nPlease select option:
                    0 - EXIT
                    1 - REGISTER
                    """)
        sel = input("\nSelect option:\t")
        if sel == '1':
            register()
        elif sel != 1:
            exit(0)
        print('Player 1')
        player_1 = loggin()
        print('Player_2')
        player_2 = loggin()
        if player_2 is not None:
            return player_1, player_2
        else:
            print("""\nPlease select option:
                    0 - EXIT
                    1 - REGISTER
                    """)
            sel = input("\nSelect option:\t")
            if sel == '1':
                register()
            elif sel != 1:
                exit(0)
            print('Player 2')
            player_2 = loggin()
        return player_1, player_2


def chg_pass(user):
    """allows user to change password
    : param user: string user_name to change
    password"""
    if str(user) in os.listdir(os.path.join('game', 'data')):
        pasw = getpass.getpass('password: ')
        pasw = pasw.strip()
        try:
            with open(os.path.join('game', 'data', str(user), f'{user}.json')) as json_file:
                credentials_f = json.load(json_file)
                credentials_f = dict(credentials_f)

                #  check password
                if hash_password(pasw) == credentials_f['password']:
                    print('password must be 6 char long, lower case, and at least 1 nr')
                    new_pasw = getpass.getpass('Type new password: ')
                    new_pasw = new_pasw.strip()
                    while not (len(new_pasw) >= 6 and new_pasw.isalnum() and not (
                            new_pasw.isalpha() or new_pasw.isnumeric())):
                        print('Insecure password ')
                        new_pasw = getpass.getpass('Type new password: ')
                        new_pasw = new_pasw.strip()

                        password_confirmation = getpass.getpass('Confirm new_password: ')
                        password_confirmation = password_confirmation.strip()

                        while new_pasw != password_confirmation:  # check password confirmation
                            print('Password not confirmed')
                            new_pasw = getpass.getpass('Type new password: ')
                            new_pasw = new_pasw.strip()
                            while not (len(new_pasw) >= 6 and new_pasw.isalnum() and not (
                                    new_pasw.isalpha() or new_pasw.isnumeric())):
                                print('Insecure password ')
                                new_pasw = getpass.getpass('Type new password: ')
                                new_pasw = new_pasw.strip()

                                password_confirmation = getpass.getpass('Confirm new_password: ')
                                password_confirmation = password_confirmation.strip()
                    else:
                        print('pass is good')
                    password_confirmation = getpass.getpass('Confirm new_password: ')
                    password_confirmation = password_confirmation.strip()

                    while new_pasw != password_confirmation:  # check password confirmation
                        print('Password not confirmed')
                        new_pasw = getpass.getpass('Type new password: ')
                        new_pasw = new_pasw.strip()
                        while not (len(new_pasw) >= 6 and new_pasw.isalnum() and not (
                                new_pasw.isalpha() or new_pasw.isnumeric())):
                            print('Insecure password ')
                            new_pasw = getpass.getpass('Type new password: ')
                            new_pasw = new_pasw.strip()

                        password_confirmation = getpass.getpass('Confirm new_password: ')
                        password_confirmation = password_confirmation.strip()

                    credentials_f['password'] = hash_password(new_pasw)

                    with open(os.path.join('game', 'data', str(user), f'{user}.json'), 'w') as json_file_w:
                        json_object = json.dumps(credentials_f)
                        json_file_w.write(json_object)
                        print('Password successfully changed')
                else:
                    print('Wrong password')
                    while True:
                        print("""\n Select:
                           0 - EXIT
                           1 - TRY AGAIN 
                           """)
                        s = input()
                        if s == '1':
                            return chg_pass(user)
                        else:
                            exit(0)
        except IOError:
            print("Warning: auth file not found")
