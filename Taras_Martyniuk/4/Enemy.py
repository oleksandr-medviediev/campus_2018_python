from DungeonMap import DungeonMap
from utils import move_directions, tuple_add
from random import randrange
from logging_decors import debug_file_console_logger as dlog

class Enemy:
    def __init__(self, dmap):
        self.dungeon_map = dmap
        self.position = dmap.get_random_empty_tile()


    def move_randomly(self):
        '''
            moves one delta in the random direction
            (not going into walls)
        '''
        while True:
            rand_move_dt = [randrange(len(move_directions))]

            new_pos = tuple_add(self.position, rand_move_dt)
            if self.dungeon_map.in_bounds(new_pos):
                self.position = new_pos
                dlog.debug(f'enemy moved to {self.position}')
                break

    
    def gotcha_player(self, player):
        '''
            True if player is about to get rekt
        '''
        return self.position == player.position

    
    def try_attack_player(self, player):
        '''
            unleashes the whole might of our 1 dmg attack 
            on the unsuspecting player, if he is in reach (on the same tile as enemy)
        '''
        if self.gotcha_player(player):
            dlog.debug('damaged player')
            player.lose_health()