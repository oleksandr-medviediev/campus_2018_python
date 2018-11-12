import world

directions = {
    'w': [ 0, -1],
    'a': [-1,  0],
    's': [ 0,  1],
    'd': [ 1,  0]
}


def game_loop():
    user_input = input('New game(1)\nLoad game (2)\n')

    if user_input == '1':
        world.create_world(10)
        player_pos = world.spawn_player()
    elif user_input == '2':
        player_pos = world.load()

    won = False
    lose = False
    while not (won or lose):
        if world.is_trap_around(player_pos):
            print('There is a trap within one square from you!')
        else:
            print('No traps around.')
        if world.is_treasure_around(player_pos):
            print('There is a treasure within one square from you!')
        else:
            print('No treasures around.')

        input_is_valid = False
        while not input_is_valid:
            user_input = input('Your move (w/a/s/d)? (Input \'save\' to save game)')

            input_is_valid = True
            if user_input in directions.keys():
                world.move_player(player_pos, directions[user_input])
            elif user_input == 'save':
                world.save(player_pos)
                print('Game saved.')
            else:
                print('Invalid input. Try again.')
                input_is_valid = False

        won = world.is_found_treasure(player_pos)
        lose = world.is_trapped(player_pos)

    if won:
        print('You won!')
    else:
        print('You lose!')

    world.print_world(player_pos)


if __name__ == '__main__':
    game_loop()
