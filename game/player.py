def get_current_player(step, pl1, pl2):
    """
    This function is used for getting data about the current player.
    :param step: Integer about the current iteration,
    :param pl1 str for player_1 name,
    :param pl2 for player_2 name
    :return: (player_name, player_sign)
    """
    if step % 2 == 0:
        name = pl1
        sign = 'x'
    else:
        name = pl2
        sign = 'o'

    return name, sign
