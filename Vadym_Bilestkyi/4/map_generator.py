import random


def generate(map_size):
    new_map = [[None] * map_size for _ in range(map_size)]

    for i in range(map_size**2 // 10):
        x = random.choice(range(map_size))
        y = random.choice(range(map_size))
        new_map[x][y] = 'Trap'

    for i in range(map_size**2 // 20):
        x = random.choice(range(map_size))
        y = random.choice(range(map_size))
        new_map[x][y] = 'Treasure'

    return new_map
