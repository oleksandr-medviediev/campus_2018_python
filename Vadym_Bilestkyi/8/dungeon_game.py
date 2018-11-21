from dungeon_logging import logger, with_logging
from world import World
from player import Player
import settings

directions = {
    'w': [ 0, -1],
    'a': [-1,  0],
    's': [ 0,  1],
    'd': [ 1,  0]
}


@with_logging
def game_loop():
    while True:
        user_input = input('Enable debug mode (y/n):')
        if user_input == 'y':
            settings.DEBUG_ENABLED = True
            break
        elif user_input == 'n':
            settings.DEBUG_ENABLED = False
            break
        else:
            print('Invalid input. Try again.\n')

    world = None
    while world is None:
        user_input = input('New game(1)\nLoad game (2)\n')

        if user_input == '1':
            world = World(size=10)
            world.spawn_player(Player('urpoK'))
            logger.warning('New game started')
        elif user_input == '2':
            try:
                world = World.load()
                logger.warning('Game loaded')
            except RuntimeError as error:
                logger.warning(error)

    won = False
    lose = False
    while not (won or lose):
        if world.is_trap_around():
            logger.warning('There is a trap within one square from you!')
        else:
            logger.warning('No traps around.')
        if world.is_treasure_around():
            logger.warning('There is a treasure within one square from you!')
        else:
            logger.warning('No treasures around.')

        input_is_valid = False
        while not input_is_valid:
            logger.warning('Your move (w/a/s/d)? (Input \'save\' to save game)')
            user_input = input()

            input_is_valid = True
            if user_input in directions.keys():
                world.move_player(directions[user_input])
            elif user_input == 'save':
                world.save()
                logger.warning('Game saved.')
            else:
                logger.warning('Invalid input. Try again.')
                input_is_valid = False

        world.update()

        won = world.is_found_treasure()
        lose = world.is_trapped()

    if won:
        logger.warning('You won!')
    else:
        logger.warning('You lose!')

    world.print()


if __name__ == '__main__':
    game_loop()
