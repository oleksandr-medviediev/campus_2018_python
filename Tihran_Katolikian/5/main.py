from DungeonGame import run_game, StartMenu, process_game_start


game_start_mode = process_game_start()
if game_start_mode is StartMenu.NEW_GAME:
    map_size = int(input('Choose map size (should be >= 5): '))
else:
    map_size = None
run_game(game_start_mode, map_size)
