class DungeonGameError(Exception):
    pass


class PlayerDiedError(DungeonGameError):

    def __str__(self):
        return 'Player died('


class PlayerBagFullError(DungeonGameError):

    def __str_(self):
        return 'Player Bag is full!'
