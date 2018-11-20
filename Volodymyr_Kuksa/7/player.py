from character import Character

PLAYER_MOVES = {'u': (0, -1), 'd': (0, 1), 'l': (-1, 0), 'r': (1, 0)}


class Player(Character):

    def __init__(self, name):

        super().__init__(name)


player = Player('Vovchik')

print(player.name)
player.name = 'Vovan'
print(player.name)
