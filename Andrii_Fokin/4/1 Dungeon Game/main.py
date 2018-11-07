import game_map as m
import game


while (True):
    player_answer = input("Start the Game? y/n : ")

    if player_answer == 'y':
        game_map = m.new_map()
        game.player_position = m.fill_free_cell(game_map, m.cell_player)
        game.loop(game_map)

        m.cell_trap
        print(f'You {m.cell_player} at position {game.player_position}')
        print(f'Treasure {m.cell_treasure}')
        print(f'Trap {m.cell_trap}')
        for line in game_map[::-1]:
            print(line , '\n')

    else:
        break
