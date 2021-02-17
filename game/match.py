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
    print('Chosen option {choice} therefore {no_of_games} games')
    logger.info(f'Chosen option {choice} therefore {no_of_games} games')
    return no_of_games


def check_match_status(player, match_dict, no_of_games_in_match, match_is_over, match_is_won):
    """
    Update match stats after a game
    # Win logic of the match : current player is the winner if
    # 1) wins N/2 + 1 games of the match
    # or
    # 2) has more wins than the other players and all the N games were played
    :param : player - who won current game,
            match_dict - current game stats genre {'draw': 0, 'total': 2, 'Player 1': 2},
            no_of_games_in_match - chosen number of games,
            match_is_over - is current match over according to specs,
            match_is_won - - is current with winner according to specs
    :return: match_is_over, match_is_won, match_winner, match_dict, match_winner
    match_dict is a dict containing current stats
    how many wins for each player, how many draws, how many total games
    match_winner should be returned as the current game could be match_over and current game
    could be a draw
    """
    match_winner = ''
    if match_dict.get(player):
        match_dict[player] = match_dict[player] + 1
    else:
        match_dict[player] = 1
    match_dict['total'] = match_dict['total'] + 1

    if ((match_dict[player] * 2 > no_of_games_in_match) or (
            match_dict[player] * 2 > no_of_games_in_match - match_dict['draw'])) and player != 'draw':
        match_is_won = True
        match_winner = player
    if match_dict['total'] == no_of_games_in_match or match_is_won:
        match_is_over = True
    if match_is_over and match_winner == '':
        match_winner = 'draw'
        # Still last game could have been a draw, if game is over
        # check if one winner had more games than the other
        # in this case it is still the winner, even not winning N/2+1 games
        players = [k for k, v in match_dict.items() if k not in ('draw', 'total')]
        # print(players)
        if len(players) > 0:  # at least one player won a match
            match_is_won = True
            # print(players[0])
            match_winner = players[0]
            if len(players) > 1 and match_dict[match_winner] < match_dict[players[1]]:  # 2nd player might have won
                # print(players[1])
                match_winner = players[1]
        # A draw match can finish the game we should return also the winner - it is not necessarily current player

    logger.info(f'Set_match_status to  match_is_over={match_is_over} match_is_won={match_is_won} '
                f'match_winner={match_winner} match_dict={match_dict}')
    # print(match_is_over, match_is_won, match_winner, match_dict)
    return match_is_over, match_is_won, match_dict, match_winner
