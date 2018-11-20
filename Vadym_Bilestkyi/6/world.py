from dungeon_logging import logger, with_logging

import random
import map_generator
import saver


world_size = 0
world = None
SAVE_DIR = 'savegame.dat'

cell_repr = {
    'Trap': '#',
    'Treasure': '$',
    'Player': 'P',
    None: '.',
}


@with_logging
def save(player_pos):
    logger.debug('Try to save game')
    saver.save([player_pos, world], SAVE_DIR)
    logger.debug('Game saved successfully')


@with_logging
def load():
    global world
    global world_size

    logger.debug('Try to load game')
    try:
        player_pos, world = saver.load(SAVE_DIR)
    except FileNotFoundError:
        raise RuntimeError('No saved games.')

    world_size = len(world)
    logger.debug('Game loaded successfully')
    return player_pos


@with_logging
def print_world(player_pos):
    logger.debug('Printing world')

    print('You at: {}'.format(player_pos))
    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            if player_pos[0] == x and player_pos[1] == y:
                cell = 'Player'
            print('{} '.format(cell_repr[cell]), end='')
        print()

    logger.debug('World was printed')


@with_logging
def get_neighbor_cells(player_pos):
    logger.debug('Searching for neighbor cells')
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx, dy) != (0, 0):
                neighbor_pos = [player_pos[0] + dx, player_pos[1] + dy]
                if is_inside_world(neighbor_pos):
                    neighbors.append(neighbor_pos)

    logger.debug('Found {} neighbor cells'.format(len(neighbors)))
    return neighbors


@with_logging
def is_trap_around(player_pos):
    logger.debug('Checking for traps')

    neighbors = get_neighbor_cells(player_pos)
    is_trap_around = any(world[neighbor[1]][neighbor[0]] == 'Trap' for neighbor in neighbors)
    return is_trap_around


@with_logging
def is_treasure_around(player_pos):
    logger.debug('Checking for treasures')

    neighbors = get_neighbor_cells(player_pos)
    is_treasure_around = any(world[neighbor[1]][neighbor[0]] == 'Treasure' for neighbor in neighbors)
    return is_treasure_around


@with_logging
def is_trapped(player_pos):
    logger.debug('Checking game over condition')
    return world[player_pos[1]][player_pos[0]] == 'Trap'


@with_logging
def is_found_treasure(player_pos):
    logger.debug('Checking winning condition')
    return world[player_pos[1]][player_pos[0]] == 'Treasure'


@with_logging
def is_inside_world(pos):
    return all(0 <= coord < len(world) for coord in pos)


@with_logging
def move_player(player_pos, direction):
    logger.debug('Player tries to move')
    new_pos = [
        player_pos[0] + direction[0],
        player_pos[1] + direction[1]
    ]
    if is_inside_world(new_pos):
        player_pos[:] = new_pos
        logger.debug('Player successfully moves')


@with_logging
def create_world(size):
    global world_size
    global world

    world_size = size
    world = map_generator.generate(size)

    logger.debug('World was created')


@with_logging
def spawn_player():
    logger.debug('Attempting to spawn player')
    player_pos = [random.choice(range(world_size)), random.choice(range(world_size))]

    while world[player_pos[1]][player_pos[0]] is not None:
        player_pos = [random.choice(range(world_size)), random.choice(range(world_size))]
        logger.debug('Player spawn retrying')

    logger.debug('Player spawned')
    return player_pos
