def get_current_player(step, players):
    """
    This function is used for getting data about the current player.
    :param step: Integer about the current iteration,
    :param players tuple containing player_1 name and
    player_name
    :return: (player_name, player_sign)
    """
    if step % 2 == 0:
        return players[0], 'x'
    else:
        return players[1], 'o'
