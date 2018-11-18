from logger import debug_decorator
from logger import info_decorator


class Player:

    def __init__(name, game_map):

        self.name = name
        self.bag = 0
        self.hp = 3
        self.islost = False
        self.iswon = False
        self.position = spawn_player(game_map)


    @debug_decorator
    @info_decorator
    def pick_treasure():
        bag += 1
        if bag >= 3:
            global iswon
            iswon = True


    @debug_decorator
    @info_decorator
    def pick_trap():
        hp -= 1
        if hp <= 0:
            global islost
            islost = True


    @debug_decorator
    @info_decorator
    def input_direction():

        player_choice = input('Where do you want to move: ')
        player_choice.casefold()

        available_choices = ['up', 'down', 'left', 'right', 'save']
        while not player_choice in available_choices:

            print("I'm sorry, I don't understand your choice.\nTry once more: ")
            player_choice = input()
            player_choice.casefold()

        return player_choice


    @debug_decorator
    @info_decorator
    def spawn_player(game_map):

        position = choice(range(game_map.mapsize * game_map.mapsize))

        row, col = position // game_map.mapsize, position % game_map.mapsize

        while game_map.game_map[row][col] == -1 or game_map.game_map[row][col] == 1:

            position = choice(range(game_map.mapsize * game_map.mapsize))
            row, col = position // game_map.mapsize, position % game_map.mapsize

        return row, col
