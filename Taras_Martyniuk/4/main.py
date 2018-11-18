from logging_defs import debug_logger as dlog
from logging_defs import output_logger as olog
from game import play_game

SIZE = 10
ZORK_INTRO = '''
    You are standing in an open field west of a white house, 
    with a boarded front door. 
    There is a small mailbox here.
'''

def main():
    dlog.debug('Main start')

    # olog.info(ZORK_INTRO)
    # olog.info('oops, wrong game!. Now, what do we have here?')
    # olog.info('\n====== Dungeon Game! ======\n')

    play_game(SIZE)

if __name__ == "__main__":
    main()
    