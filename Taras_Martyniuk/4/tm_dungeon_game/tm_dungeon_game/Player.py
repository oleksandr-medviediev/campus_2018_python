from DungeonMap import DungeonMap
from logging_decors import log_decor, debug_file_console_logger as dlog, output_logger as olog
from utils import move_directions, tuple_add
from exceptions import AlreadyDeadError

class Player:
    @log_decor
    def __init__(self, health, dmap, on_death):
        """
            :param health: starting hp 
            :param dmap: DungeonMap this player is going to navigate
            :param onDeath: parameterless callback, executed when player dies
        """   
        assert isinstance(health, int)
        self.position = (0, 0)
        self.dungeon_map = dmap
        self.on_death = on_death
        self.__health = health
        self.__treasures = 0


    @property
    def health(self):
        return self.__health

    
    @property
    def treasures(self):
        return self.__treasures


    @log_decor
    def lose_health(self):
        '''
            takes away 1 health
            if player is killed, executes on_death
            :throws RuntimeError: if no health left
            :returns: boolean indicating if the blow was fatal
        '''
        if self.health <= 0:
            raise AlreadyDeadError
        self.__health -= 1
        dead = self.__health == 0

        dlog.debug(f'Player lost health. Remaining: {self.health}')

        if dead:
            self.on_death()
        else:
            olog.info('Ouch! That hurt!')
            olog.info(f'You feel like you could endure only {self.health} more such hits')

        return dead

    
    @log_decor
    def add_treasure(self):
        '''
            adds a treasure to the bag
        '''
        self.__treasures += 1
        dlog.info(f'+1 treasure: total now:{self.treasures}')

    
    @log_decor
    def try_move(self, move_dt):
        """
            tries to move 1 tile in the specified direction
            checks if the move is valid,
            if it was, updates player's position, else it is left unchanged

            :param new_pos: tile delta for movement in the range of 1 (e.g 0, 1),
                must be in bounds of dungeon_map
            :returns: True if the try was successful else False 
                
        """   
        if move_dt not in move_directions:
            raise ValueError(f'move delta must be one of {move_directions}')

        assert self.dungeon_map.in_bounds(self.position)

        moved_pos = (self.position[0] + move_dt[0], self.position[1] + move_dt[1])
        dlog.debug(f'trying to move to {moved_pos}')

        move_valid = self.dungeon_map.in_bounds(moved_pos)
        if move_valid:
            self.position = moved_pos

        return move_valid 
