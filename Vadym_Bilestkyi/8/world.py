from dungeon_logging import logger, methods_with_logging

import random
import map_generator
import saver


@methods_with_logging
class World:

    SAVE_DIR = 'savegame.dat'

    cell_repr = {
        'Trap': '#',
        'Treasure': '$',
        'Player': 'P',
        None: '.',
    }

    def __init__(self, size_or_map):
        self._map = None
        self._size = None
        self._player = None

        def _init_new_map(size):
            self._size = size
            self._map = map_generator.generate(size)

        def _init_with_existing_map(map):
            self._map = map
            self._size = len(map)

        if isinstance(size_or_map, int):
            _init_new_map(size_or_map)
        elif isinstance(size_or_map, list):
            _init_with_existing_map(size_or_map)

    def get_cell(self, x, y):
        return self._map[y][x]

    def place_cell(self, x, y, cell):
        self._map[y][x] = cell

    def clear_cell(self, x, y):
        self.place_cell(x, y, None)

    def spawn_player(self, player):
        self._player = player

        self._player.position = [random.choice(range(self._size)), random.choice(range(self._size))]

        while self.get_cell(*self._player.position) is not None:
            self._player.position = [random.choice(range(self._size)), random.choice(range(self._size))]

    def save(self):
        saver.save([self._player, self._map], World.SAVE_DIR)

    @staticmethod
    def load():
        try:
            player, map = saver.load(World.SAVE_DIR)
        except FileNotFoundError:
            raise RuntimeError('No saved games.')

        world = World(map)
        world._player = player

        return world

    def print(self):
        print('You at: {}'.format(self._player.position))
        for y, row in enumerate(self._map):
            for x, cell in enumerate(row):
                if self._player.is_standing_at(x, y):
                    cell = 'Player'
                print('{} '.format(World.cell_repr[cell]), end='')
            print()

    def get_neighbor_cells(self):
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (dx, dy) != (0, 0):
                    neighbor_pos = self._player.get_neighbor_within(dx, dy)
                    if self.is_inside(neighbor_pos):
                        neighbors.append(neighbor_pos)

        return neighbors

    def is_inside(self, pos):
        return all(0 <= coord < self._size for coord in pos)

    def is_trap_around(self):
        neighbors = self.get_neighbor_cells()
        is_trap_around = any(self.get_cell(*neighbor) == 'Trap' for neighbor in neighbors)
        return is_trap_around

    def is_treasure_around(self):
        neighbors = self.get_neighbor_cells()
        is_treasure_around = any(self.get_cell(*neighbor) == 'Treasure' for neighbor in neighbors)
        return is_treasure_around

    def is_trapped(self):
        return self._player.is_dead()

    def is_found_treasure(self):
        return self._player.is_rich()

    def update(self):
        if self.get_cell(*self._player.position) == 'Trap':
            self.clear_cell(*self._player.position)
            self._player.hurt()
        elif self.get_cell(*self._player.position) == 'Treasure':
            self.clear_cell(*self._player.position)
            self._player.pickup_treasure()

    def move_player(self, direction):
        new_pos = self._player.get_neighbor_within(*direction)

        if self.is_inside(new_pos):
            self._player.position = new_pos
