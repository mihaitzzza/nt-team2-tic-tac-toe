import logging
from .board import board_matrix as initial_board, get_options, show, set_choice
from .status import check_status
from .player import get_current_player
from .match import check_match_status
import copy

logger = logging.getLogger(__name__)


def start():
    """
    This is the engine of the game.
    """
    is_over = False
    step = 0
    available_options = []
    is_correct_choice = True
    sign = 'x'

    # deep copy
    board_matrix = copy.deepcopy(initial_board)
    print(board_matrix)
    winner = None
    player_name = None
    played_sequence = []

    print('Welcome and good luck!')
    logger.info('Welcome and good luck!')

    while not is_over:
        if is_correct_choice:
            player_name, sign = get_current_player(step)
            print('%s is your turn.' % player_name)
            logger.info('%s is your turn.' % player_name)

            available_options = get_options(board_matrix)

        show(board_matrix)
        print('Pick a choice from available options: ', available_options)
        logger.info('Pick a choice from available options: %s' % available_options)

        choice = input('Pick your choice: ')
        logger.info('Pick your choice: ')
        try:
            choice = int(choice)

            if choice not in available_options:
                raise ValueError()
        except ValueError as e:
            print('Your choice is not an option.')
            logger.error('Your choice is not an option.')
            logger.exception(e)
            is_correct_choice = False
            continue
        else:
            is_correct_choice = True
            logger.info('Player choice: %s' % choice)

        played_sequence.append(choice)

        board_matrix = set_choice(board_matrix, choice, sign)

        # Check if the game is won or not.
        is_won, is_over = check_status(board_matrix)

        if is_won:
            winner = player_name

        step += 1

    print('Game Over!')
    logger.info('Game Over!')

    if winner:
        print(f'{winner} has won the game.')
        logger.info(f'{winner} has won the game.')
    else:
        print('Game ended as a draw.')
        logger.info('Game ended as a draw.')
        winner = 'draw'
    show(board_matrix)
    print(f'Played sequence was {played_sequence}')
    return winner
