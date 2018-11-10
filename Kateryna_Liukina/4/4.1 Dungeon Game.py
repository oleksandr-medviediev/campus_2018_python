import Map_generator
import Warning_generator
import math


def dungeon_game():
    size_of_map = int(input("Enter size of map"))
    game_map = Map_generator.generate_map([size_of_map] * 2, 0.1, 0.05)

    player_position = Map_generator.generate_coordinates(game_map)
    direction_map = {'up': [1, 0], 'down': [-1, 0], 'left': [0, -1], 'right': [0, 1]}

    game_over = False
    player_win = False

    while not game_over:
        print("Your position:" + str(player_position))
        Warning_generator.generate_warning(game_map, player_position, 1)
        Warning_generator.generate_warning(game_map, player_position, 2)

        direction = direction_map[input("Enter direction")]

        player_position[0] += direction[0]
        player_position[1] += direction[1]

        player_position[0] = max(0, min(player_position[0], size_of_map - 1))
        player_position[1] = max(0, min(player_position[1], size_of_map - 1))

        if game_map[player_position[0]][player_position[1]] == 1:
            game_over = True

        elif game_map[player_position[0]][player_position[1]] == 2:

            game_over = True
            player_win = True

    if player_win:
        print("You won!!!")
    else:
        print("You lost.")
    print(game_map)


dungeon_game()