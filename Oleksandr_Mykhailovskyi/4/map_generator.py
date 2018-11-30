import random

from logging_utility import logger
from logging_utility import logging_debug_decorator
from logging_utility import logging_info_decorator


@logging_debug_decorator
@logging_info_decorator
def shuffle_map(game_map):
    """
    Because random.shuffle with list worked somewhat strangely - 
    need to shuffle every sub-list independently.

    Args:
        game_map (list[str]): game map
    """
    for i in game_map:
        random.shuffle(i)


@logging_debug_decorator
@logging_info_decorator
def format_map(game_map, x):
    """
    Makes list of cells list of lists of cells.

    Args:
        game_map (list[str]): game map
        x (int): rows
    Returns:
        [[str...]...] - game map
    """
    formatted_map = []
    for dstep in range(0, x):
        formatted_map.append([])
        for j in range(0, x):
            formatted_map[dstep].append(game_map[j + dstep * x])

    return formatted_map


@logging_debug_decorator
@logging_info_decorator
def generate_prob_map(size, cell_probabilities, cell_reprs):
    """
    Generates probabilistic map from map_elements sized size*size

    Args:
        size (int): rows/columns of the map square
    Returns:
        [[str...]...] - game map.
    """
    if not isinstance(size, int):
        logger.debug("probabilistic map gen failed, argument inconsistency")
        raise TypeError(f'{type(size)} is not int.')

    # to make correspondence for each element
    # e.g. nothing in probabilities[0] and cells[0]
    probabilities = []
    cells = []

    for name, key in cell_probabilities.items():
        probabilities.append(key)
        cells.append(cell_reprs[name])

    game_map = random.choices(cells, weights=probabilities, k=size*size)

    game_map = format_map(game_map, size)
    shuffle_map(game_map)
    return game_map


@logging_debug_decorator
@logging_info_decorator
def generate_map(size, cell_quantities, cell_reprs):
    """
    Generates map from map_elements sized size*size

    Args:
        size (int): rows/columns of the map square.
        cell_quantities ({str: int}): dictionary for cell amounts.
        cell_reprs ({str: str}): dictionary for cell representations.
    Returns:
        [[str...]...] - game map.
    """
    if not isinstance(size, int):
        raise TypeError(f'{type(size)} is not int.')

    game_map = []
    for name, value in cell_quantities.items():
        for _ in range(value):
            game_map.append(cell_reprs[name])

    game_map = format_map(game_map, size)
    shuffle_map(game_map)
    return game_map


@logging_debug_decorator
@logging_info_decorator
def generate_random_map(*args, size, probabilistic=True):
    """
    Returns map of random size between 10 and 20.

    Args:
        probabilistic (bool): whether to generate map filled
                            by cell's probability.
    Returns:
        [[str...]...] - game map.
    """
    if probabilistic:
        return generate_prob_map(size, *args)
    return generate_map(size, *args)
