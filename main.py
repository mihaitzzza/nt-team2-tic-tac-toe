import logging
import game
import uuid
import os.path
from game import match
from datetime import datetime

log_filename = datetime.now().strftime('%Y%m%d%H%M%S') + '_' + str(uuid.uuid4()) + '.txt'

logging.basicConfig(
    filename=os.path.join('games', log_filename),
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger('Tic-Tac-Toe App')

if __name__ == '__main__':
    try:
        no_of_games_in_match = match.input_number_of_matches()
        match_is_over = False
        match_is_won = False
        match_winner = None
        match_stats = {
            'draw': 0,
            'total': 0, }
        while not match_is_over:
            game_winner = game.start()
            match_is_over, match_is_won, match_stats, match_winner = \
                match.check_match_status(game_winner, match_stats, no_of_games_in_match)
            print(f'Current match stats: {match_stats}!!!')
        if match_is_won:
            print(f'Player {match_winner} has won the game with {match_stats}!')
        else:
            print(f'Match ended in a draw with {match_stats}!!!')
    except BaseException as e:
        logger.exception(e)
