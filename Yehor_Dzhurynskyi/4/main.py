import level
import dungeon_game

while True:

    size_str = input('Enter level size (N x N): ')

    if size_str.isnumeric() and int(size_str) >= 5:

        size = int(size_str)
        break

    print('Wrong input! It should be integer >= 5 number')

lvl = level.generate_level(size)
lvl_is_valid = level.validate(lvl)

player_x, player_y = dungeon_game.spawn_player(lvl)
player_x, player_y = dungeon_game.loop(lvl, player_x, player_y)

level.print_level(lvl, player_x, player_y)
