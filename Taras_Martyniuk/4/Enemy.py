import DungeonMap as dm
from utils import move_directions, tuple_add
from random import randrange
from logging_decors import log_decor, debug_file_console_logger as dlog, output_logger as olog
from exceptions import OutOfMapError
import threading
from functools import partial

class Enemy:
    # sec
    MOVE_INTERVAL = 4

    @log_decor
    def __init__(self, dmap):
        '''
            sets position to a random empty tile within dmap
            :param dmap: DungeonMap
        '''
        self.position = dmap.get_random_empty_tile()

    
    def start_patroling(self, dmap, player):
        '''
            asynchronously moves in a random non-walled direction every MOVE_INTERVAL seconds
            :param dmap: DungeonMap
            :param player: Player to chase (not really following himm still movign totally random)
        '''
        self.try_attack_player(player)
        self.move_randomly(dmap)
        self.try_attack_player(player)

        tile_val = dmap.at(self.position)
        # eats our treasure!
        if tile_val == dm.Treasure:
            dlog.debug(f'enemy ate treasure at {self.position}')
            dmap.set_tile(self.position, dm.Empty)

        elif tile_val == dm.Trap:
            dlog.debug(f'enemy respawned to {self.position}')
            self.position = dmap.get_random_empty_tile()

        threading.Timer(self.MOVE_INTERVAL, partial(self.start_patroling, dmap, player)).start()


    @log_decor
    def move_randomly(self, dmap):
        '''
            moves one delta in the random direction
            (not going into walls)

            :param dmap: DungeonMap to navigate 
        '''
        if not dmap.in_bounds(self.position):
            ValueError('enemie\'s position is out of bounds of argument DungeonMap')
            
        while True:
            rand_move_dt = move_directions[randrange(len(move_directions))]

            new_pos = tuple_add(self.position, rand_move_dt)
            if dmap.in_bounds(new_pos):
                self.position = new_pos
                dlog.debug(f'enemy moved to {self.position}')
                break

    
    @log_decor
    def gotcha_player(self, player):
        '''
            :returns: True if player is about to get rekt
        '''
        return self.position == player.position

    
    @log_decor
    def try_attack_player(self, player):
        '''
            unleashes the whole might of our 1 dmg attack 
            on the unsuspecting player, if he is in reach (on the same tile as enemy)
        '''
        if self.gotcha_player(player):
            dlog.debug('damaged player')
            player.lose_health()
            