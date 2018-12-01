from game_terrain import game_terrain
from save_load import load_game
from character import character
from game_loop import game_loop

'''
this package repository
https://test.pypi.org/project/dungeon-game-by-dmiroshnyk/
'''

while True:
    player_answer = input(
        "enter 'new' to start new game or 'load' to load saved game:\n").lower()

    if player_answer == 'new':
        game_terrain.generate_new_map()
        character.current_backpack = 0
        character.current_hp = 3

        game_loop.clear()

        game_loop.loop()

        for line in game_terrain.terrain[::-1]:
            print(*line, '\n')

    elif player_answer == 'load':
        game_terrain.terrain = load_game()

        if game_terrain.terrain == None:
            game_terrain.generate_new_map()

            game_loop.clear()
            game_loop.loop()

            for line in game_terrain.terrain[::-1]:
                print(*line, '\n')
        else:
            character.position = game_terrain.find_player_position()

            game_loop.clear()

            game_loop.loop()

        for line in game_terrain.terrain[::-1]:
            print(*line, '\n')
    else:
        break
