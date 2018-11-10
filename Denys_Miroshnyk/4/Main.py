import Map_generator
import Game_loop

field_size = 10

while (True):
    player_answer = input("Start the Game? y/n \n").lower()

    if player_answer == 'y':
        game_map = Map_generator.generate_map(field_size)

        Game_loop.player_position = Map_generator.init_free_cell(
            game_map, Map_generator.player)
        Game_loop.loop(game_map)

        print(f'at {Game_loop.player_position}')
        print(f'Treasures -> {Map_generator.treasure}')
        print(f'Traps -> {Map_generator.trap}')
        for line in game_map[::-1]:
            print(*line, '\n')
    else:
        break
