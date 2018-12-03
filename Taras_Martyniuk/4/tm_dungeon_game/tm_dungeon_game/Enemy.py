import DungeonMap as dm
from utils import move_directions, tuple_add
from random import randrange
from logging_decors import log_decor, debug_file_console_logger as dlog, output_logger as olog
from exceptions import OutOfMapError
import threading
from functools import partial
from time import sleep

class Enemy:
    # sec
    MOVE_INTERVAL = 4

    @log_decor
    def __init__(self, dmap):
        '''
            sets position to a random empty tile within dmap
            :param dmap: DungeonMap DungeonMap to navigate 
        '''
        self.position = dmap.get_random_empty_tile()
        self.dungeon_map = dmap
        self.patrol_stop_event = threading.Event()
        
    
    def start_patroling(self, player):
        '''
            asynchronously moves in a random non-walled direction every MOVE_INTERVAL seconds
            :param player: Player to chase (not really following himm still movign totally random)
        '''
        self.patrol_stop_event.clear()

        def patrol_with_pauses(self):
            while not self.patrol_stop_event.is_set():
                self.patrol(player)
                sleep(self.MOVE_INTERVAL)

        captured = partial(patrol_with_pauses, self)

        patrol_thread = threading.Thread(name='patrol thread', target=captured)
        # will end anyway when event is set, but i don't want to join on it, since it'll block us for 4 sec
        patrol_thread.setDaemon(True)
        patrol_thread.start()


    @log_decor
    def patrol(self, player):
        '''
            a single turn of patrol
            attacks player if standing on the same tile, moves randomly and tries to attack again
        '''
        self.try_attack_player(player)
        self.move_randomly()
        self.try_attack_player(player)

        tile_val = self.dungeon_map.at(self.position)
        if tile_val == dm.Treasure:
            dlog.debug(f'enemy ate treasure at {self.position}')

        elif tile_val == dm.Trap:
            dlog.debug(f'enemy died from a trap at {self.position}')
            self.position = self.dungeon_map.get_random_empty_tile()
            dlog.debug(f'enemy respawned to {self.position}')

        # eats our treasure, or destroys the trap by activating it
        self.dungeon_map.set_tile(self.position, dm.Empty)


    @log_decor
    def stop_patroling(self):
        '''
            stops chasing player
        '''
        self.patrol_stop_event.set()


    @log_decor
    def move_randomly(self):
        '''
            moves one delta in the random direction
            (not going into walls)
        '''
        if not self.dungeon_map.in_bounds(self.position):
            ValueError('enemie\'s position is out of bounds of argument DungeonMap')
            
        while True:
            rand_move_dt = move_directions[randrange(len(move_directions))]

            new_pos = tuple_add(self.position, rand_move_dt)
            if self.dungeon_map.in_bounds(new_pos):
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
            olog.info('the grue\'s got you!')
            player.lose_health()
