import logging
import game
import uuid
import os.path
from game.access import register
from game.access import chg_pass

logging.basicConfig(
    filename=os.path.join('games', f'{uuid.uuid4()}.txt'),
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger('Tic-Tac-Toe App')

if __name__ == '__main__':

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
            user = input('Type username: ')
            if user in os.listdir(os.path.join('game', 'data')):
                chg_pass(user)

            else:
                print('username does not exist')
                while True:
                    print("""\n Select:
                       0 - EXIT
                       1 - REGISTER 
                       """)
                    m = input()
                    if m == '1':
                        register()
                        try:
                            game.start()
                        except BaseException as e:
                            logger.exception(e)
                    else:
                        exit(0)
        else:
            exit(0)
