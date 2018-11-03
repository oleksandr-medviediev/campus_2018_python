import random

# Contains map cells as: (String equivalent, symbol, probability)
map_elements = [
    ("Nothing", ".", 17 / 20),
    ("Treasure", "!", 1 / 20),
    ("Trap", "x", 1 / 10)
]


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
    if not isinstance(x, int):
        return None

    probabilities = [i[2]*100 for i in map_elements]
    cells = [i[1] for i in map_elements]
    game_map = random.choices(cells, weights=probabilities, k=x * x)

    return format_map(game_map, x)


def generate_map(x):
    """
    Generates map from map_elements sized x*x

    Args:
        x (int): rows/columns of the map square
    Returns:
        [[str...]...] - game map.
    """
    if not isinstance(x, int):
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

    random.shuffle(game_map)
    return format_map(game_map, x)


def generate_random_map(probabilistic=False):
    """
    Returns map of random size between 5 and 10.

    Args:
        probabilistic (bool): whether to generate map filled
                            by cell's probability.
    Returns:
        [[str...]...] - game map.
    """
    size = random.uniform(5, 10)
    if probabilistic:
        return generate_prob_map(size)
    return generate_map(size)
