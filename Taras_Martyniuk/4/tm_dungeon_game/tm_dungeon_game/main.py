from logging_decors import log_decor, output_logger as olog
from game import play_game
from .tm_dungeon_game.tests import test_enemy

SIZE = 10
ZORK_INTRO = '''
    You are standing in an open field west of a white house, 
    with a boarded front door. 
    There is a small mailbox here.
'''


@log_decor
def main():
    olog.info(ZORK_INTRO)
    olog.info('oops, wrong game!. Now, what do we have here?')
    olog.info('\n====== Dungeon Game! ======\n')

    play_game(SIZE)

if __name__ == "__main__":
    main()
    