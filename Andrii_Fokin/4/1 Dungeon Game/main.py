import game_map as m
import game


while (True):
    player_answer = input("Start the Game? y/n")

    if player_answer == 'y':
        game_map = m.new_map()
        game.loop(game_map)
    else:
        break

