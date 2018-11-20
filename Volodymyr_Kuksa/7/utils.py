import dungeon_game_decorators


@dungeon_game_decorators.log_decor
@dungeon_game_decorators.debug_decor
def query_player_input(prompt, possible_answer):
    player_input = input(prompt)

    while not possible_answer.count(player_input):
        player_input = input('Wrong! Try again: ')

    return player_input
