import logging
import game
import uuid
import os.path
from access.register_engine import register
from access.auth import change_password
import sys

logging.basicConfig(
    filename=os.path.join('games', f'{uuid.uuid4()}.txt'),
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger('Tic-Tac-Toe App')

if __name__ == '__main__':

    # check if folders data and users exists if not it wil be created
    if 'data' not in os.listdir():
        os.mkdir('data')
    if 'users' not in os.listdir('data'):
        os.mkdir(os.path.join('data', 'users'))

    while True:
        print("""\n Select:
                               0 - EXIT
                               1 - PLAY
                               2 - REGISTER
                               3 - CHANGE PASSWORD
                               """)
        s = input()
        if s == '1':
            try:
                game.start()
            except BaseException as e:
                logger.exception(e)
        elif s == '2':
            register()
        elif s == '3':
            change_password()
        elif s == '0':
            sys.exit(0)
