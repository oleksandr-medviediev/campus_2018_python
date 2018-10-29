from random import randint
from random import shuffle

GAME_CHARACTERS = {'Empty': ' ', 'Trap': 'X', 'Treasure': 'O'}


def generate_flat_map(size_total):

    treasure_quantity = size_total // 20
    traps_quantity = size_total // 10
    empty_quantity = size_total - (treasure_quantity + traps_quantity)

    characters = []

    for i in range(size_total):

        if i < empty_quantity:
            characters.append(GAME_CHARACTERS['Empty'])
        elif i < empty_quantity + traps_quantity:
            characters.append(GAME_CHARACTERS['Trap'])
        else:
            characters.append(GAME_CHARACTERS['Treasure'])

    shuffle(characters)

    return characters


def split_rows(size, characters):

    game_map = []

    for i in range(size):
        row = characters[i * size: i * size + size]
        game_map.append(row)

    return game_map


def generate_map(size):

    characters = generate_flat_map(size * size)
    game_map = split_rows(size, characters)

    return game_map


def print_map(game_map):

    horizontal_border = ''.join(['+', '-' * len(game_map[0]), '+'])

    print(horizontal_border)

    for row in game_map:
        print(''.join(['|', ''.join(row), '|']))

    print(horizontal_border)


if __name__ == '__main__':

    new_map = generate_map(randint(5, 10))
    print_map(new_map)
