import dungeon_game_maps
import dungeon_game_logic

if __name__ == '__main__':

    game_map = dungeon_game_maps.generate_map(10)
    dungeon_game_logic.run_game(game_map)
    dungeon_game_maps.print_map(game_map)
