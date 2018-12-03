# only 2 of them, but this one is highly(moderately) reusable 
class OutOfMapError(Exception):

    def __init__(self, tile):
        '''
            tile: 2D tuple
        '''
        super().__init__(f'the tile ({tile[0]},{tile[1]}) is out of bounds of the DungeonMap')


class AlreadyDeadError(Exception):

    def __init__(self):
        super().__init__('attempting to kill a player whose health is <= 0')

