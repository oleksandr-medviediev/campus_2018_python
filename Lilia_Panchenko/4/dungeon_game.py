import game_step as gs


def input_player_direction():
    
    player_direction = input('Where do you want to move: ')
    player_direction.casefold()
    
    DIRECTIONS = ['up', 'down', 'left', 'right']
    while not player_direction in DIRECTIONS:

        player_direction = input("I'm sorry, I don't understand where do you want to go.\nTry once more: ")
        player_direction.casefold()
        
    return player_direction


print("Welcome to dungeon game! Let's play! \nRemember, you can move up, down, left or right. Your aim is to get to treasure")


gs.init_game()

while not gs.is_game_ended():
    
    gs.notify_player_about_traps()
    gs.notify_player_about_treasures()
    direction = input_player_direction()
    gs.perform_next_step(direction)
    
gs.print_game_result()
gs.print_game_map()
