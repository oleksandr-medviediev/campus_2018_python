from dungeon_logging import logger
import world

directions = {
    'w': [ 0, -1],
    'a': [-1,  0],
    's': [ 0,  1],
    'd': [ 1,  0]
}


def game_loop():
    game_started = False

    while not game_started:
        user_input = input('New game(1)\nLoad game (2)\n')

        if user_input == '1':
            world.create_world(10)
            player_pos = world.spawn_player()
            game_started = True
            logger.warning('New game started')
        elif user_input == '2':
            try:
                player_pos = world.load()
                game_started = True
                logger.warning('Game loaded')
            except RuntimeError as error:
                logger.warning(error)

    won = False
    lose = False
    while not (won or lose):
        if world.is_trap_around(player_pos):
            logger.warning('There is a trap within one square from you!')
        else:
            logger.warning('No traps around.')
        if world.is_treasure_around(player_pos):
            logger.warning('There is a treasure within one square from you!')
        else:
            logger.warning('No treasures around.')

        input_is_valid = False
        while not input_is_valid:
            logger.warning('Your move (w/a/s/d)? (Input \'save\' to save game)')
            user_input = input()

            input_is_valid = True
            if user_input in directions.keys():
                world.move_player(player_pos, directions[user_input])
            elif user_input == 'save':
                world.save(player_pos)
                logger.warning('Game saved.')
            else:
                logger.warning('Invalid input. Try again.')
                input_is_valid = False

        won = world.is_found_treasure(player_pos)
        lose = world.is_trapped(player_pos)

    if won:
        logger.warning('You won!')
    else:
        logger.warning('You lose!')

    world.print_world(player_pos)


if __name__ == '__main__':
    game_loop()
