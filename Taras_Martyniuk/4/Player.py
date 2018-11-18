from DungeonMap import DungeonMap
from logging_defs import debug_logger as dlog


class Player:
    '''
        in-game living entity
    '''
    def __init__(self, health, dmap):
        """
            :param health: starting hp 
            :param dmap: DungeonMap this player is going to navigate
        """   
        assert isinstance(health, int)
        self.position = (0, 0)
        self.dungeon_map = dmap
        # should i even make these private?
        # is adding a public interface modifiers (loseHealth) enough?
        # (the setters would still be present)
        self.__health = health
        self.__treasures = 0


    @property
    def health(self):
        return self.__health

    
    @property
    def treasures(self):
        return self.__treasures


    def loseHealth(self):
        '''
            takes away 1 health
            :throws RuntimeError: if no health left
        '''
        if self.health <= 0:
            raise RuntimeError('already dead')
        self.__health -= 1

    
    def add_treasure(self):
        '''
            adds a treasure to the bag
        '''
        self.__treasures += 1

    
    def try_move(self, move_dt):
        """
            tries to move 1 tile in the specified direction
            checks if the move is valid,
            if it was, updates player's position, else it is left unchanged

            :param new_pos: tile delta for movement in the range of 1 (e.g 0, 1),
                must be in bounds of dungeon_map
            :returns: True if the try was successful else False 
                
        """   
        if move_dt[0] not in (0, 1, -1) or move_dt[1] not in (0, 1, -1):
            raise ValueError()

        assert self.dungeon_map.in_bounds(self.position)

        dlog.debug(f'trying to move by delta of {move_dt}')
        moved_pos = (self.position[0] + move_dt[0], self.position[1] + move_dt[1])
        dlog.debug(f'trying to move to {moved_pos}')

        move_valid = self.dungeon_map.in_bounds(moved_pos)
        if move_valid:
            self.position = moved_pos

        return move_valid 






def decor_another(func):
    def wrapper(*args):
        print('before func')
        func(*args)
        print('after func')
    
    return wrapper

@decor
@decor_another
def test_decor(text):
    print(text)

test_decor('func    ')

