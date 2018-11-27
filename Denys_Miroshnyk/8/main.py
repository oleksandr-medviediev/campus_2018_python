from game_terrain import game_terrain
from player_input import player_input
from save_load import load_game
from character import character


while True:
    player_answer = input(
        "enter 'new' to start new game or 'load' to load saved game:\n").lower()

    if player_answer == 'new':
        game_terrain.generate_new_map()
        character.current_backpack = 0
        character.current_hp = 3

        while player_input.perform_player_action():
            player_input.print_state()

        for line in game_terrain.terrain[::-1]:
            print(*line, '\n')

    elif player_answer == 'load':
        game_terrain.terrain = load_game()

        if game_terrain.terrain == None:
            game_terrain.generate_new_map()

            while player_input.perform_player_action():
                player_input.print_state()

            for line in game_terrain.terrain[::-1]:
                print(*line, '\n')
        else:
            character.position = game_terrain.find_player_position()

            while player_input.perform_player_action():
                player_input.print_state()

        for line in game_terrain.terrain[::-1]:
            print(*line, '\n')
    else:
        break
