def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """ 
    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?
    Return:
        bool: Can a ghost be eaten?
    """

    return power_pellet_active and touching_ghost

def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """
    Parameters:
        touching_power_pellet (bool): Is the player touching a power pellet?
        touching_dot (bool): Is the player touching a dot?
    Return:
        bool: Has the player scored or not?
    """

    return touching_power_pellet or touching_dot

def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): is the player touching a ghost?
    Return:
        bool: Has the player lost the game?
    """

    return not power_pellet_active and touching_ghost

def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Parameters:
        has_eaten_all_dots (bool): Has the player "eaten" all the dots?
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?
    Return:
        bool: Has the player won the game?
    """

    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)

print(lose(False, True))