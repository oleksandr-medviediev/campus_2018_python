import random
from logging_utility import logger

player_repr = "P"
fog_repr = "-"
unknown_repr = "?"
map_cells_repr = [".", "!", "x"]

# Contains map cells as: (String equivalent, symbol, probability)
map_elements = [
    ("Nothing", map_cells_repr[0], 17 / 20),
    ("Treasure", map_cells_repr[1], 1 / 20),
    ("Trap", map_cells_repr[2], 1 / 10)
]


def shuffle_map(game_map):
    """
    Because random.shuffle with list worked somewhat strangely - 
    need to shuffle every sub-list independently.

    Args:
        game_map (list[str]): game map
    """
    logger.debug("map shuffle started")
    for i in game_map:
        random.shuffle(i)
    logger.debug("map shuffle ended")


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
            formatted_map[dstep].append(game_map[j + dstep])

    return formatted_map


def generate_prob_map(x):
    """
    Generates probabilistic map from map_elements sized x*x

    Args:
        x (int): rows/columns of the map square
    Returns:
        [[str...]...] - game map.
    """
    logger.debug("probabilistic map generation started")
    if not isinstance(x, int):
        logger.debug("probabilistic map gen failed, argument inconsistency")
        return None
        
    probabilities = [i[2]*100 for i in map_elements]
    cells = [i[1] for i in map_elements]
    game_map = random.choices(cells, weights=probabilities, k=x * x)

    game_map = format_map(game_map, x)
    shuffle_map(game_map)
    logger.debug("probabilistic map gen succeeded")
    return game_map


def generate_map(x):
    """
    Generates map from map_elements sized x*x

    Args:
        x (int): rows/columns of the map square
    Returns:
        [[str...]...] - game map.
    """
    logger.debug("map generation started")
    if not isinstance(x, int):
        logger.debug("map gen failed, arguments incosistency")
        return None

    cells_amounts = []
    for entry in map_elements:
        cells_amounts.append(int(entry[2] * x * x))

    cells = sum(cells_amounts)
    cells_amounts[0] += x * x - cells

    game_map = []
    for i, entry in enumerate(cells_amounts):
        for j in range(0, entry):
            game_map.append(map_elements[i][1])

    game_map = format_map(game_map, x)
    shuffle_map(game_map)
    logger.debug("map gen succeeded")
    return game_map


def generate_random_map(probabilistic=False):
    """
    Returns map of random size between 10 and 20.

    Args:
        probabilistic (bool): whether to generate map filled
                            by cell's probability.
    Returns:
        [[str...]...] - game map.
    """
    logger.debug("map generation started")
    size = int(random.uniform(10, 20))
    logger.debug("random size generated")
    if probabilistic:
        return generate_prob_map(size)
    return generate_map(size)
