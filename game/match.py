import logging

logger = logging.getLogger(__name__)


def input_number_of_matches():
    """
    Input number of matches.
    :param : None, input from keyboard
    :return: 1, 2 , 3 (1 (Choose "1") ; 2 of 3 (Choose "2") ; 3/5 (Choose "3") )
    """
    is_no_matches_chosen = False
    choice = 0
    while not is_no_matches_chosen:
        choice = input('Pick how many matches: 1 (Choose "1") ; 2 of 3 (Choose "2") ; 3/5 (Choose "3") : ')
        logger.info('Pick how many matches: 1 (Choose "1") ; 2 of 3 (Choose "2") ; 3/5 (Choose "3") : ')
        try:
            choice = int(choice)

            if choice not in (1, 2, 3):
                raise ValueError()
        except ValueError as e:
            print('Your choice of no of matches is not an option.')
            logger.error('Your choice of no of matches is not an option.')
            logger.exception(e)
            continue
        else:
            is_no_matches_chosen = True
            logger.info('Player choice: %s' % choice)
    no_of_games = (choice - 1) * 2 + 1
    print(no_of_games)
    logger.info(f'Chosen option {choice} therefore {no_of_games} games')
    return no_of_games


no_of_matches = input_number_of_matches()


def get_number_of_matches():
    global no_of_matches
    print(no_of_matches)
    return no_of_matches


match_is_over = False
match_is_won = False
match_winner = ''
match_dict = {
    'd': 0,
    't': 0, }


def set_match_status(player):
    """
    Update match stats after a game
    :param : Player who won, 'd' for draw
    :return: match_is_over, match_is_won, match_winner, match_dict
    match_dict is a dict containing current stats
    how many wins for each player, how many draws, how many total games
    """
    global match_is_over, match_is_won, match_winner, match_dict
    if match_dict.get(player):
        match_dict[player] = match_dict[player] + 1
    else:
        match_dict[player] = 1
    match_dict['t'] = match_dict['t'] + 1
    if (match_dict[player] * 2 > no_of_matches) and player != 'd':
        match_is_won = True
        match_winner = player
    if match_dict['t'] == no_of_matches or match_is_won:
        match_is_over = True
    if match_is_over and match_winner == '':
        match_winner = 'd'
    logger.info(f'Set_match_status to  match_is_over={match_is_over} match_is_won={match_is_won} '
                f'match_winner={match_winner} match_dict={match_dict}')
    # print(match_is_over, match_is_won, match_winner, match_dict)


def get_match_status():
    global match_is_over, match_is_won, match_winner, match_dict
    # print(match_is_over, match_is_won, match_winner)
    return match_is_over, match_is_won, match_winner, match_dict
