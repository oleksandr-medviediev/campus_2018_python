from logging_defs import dungeon_logger as dlog
import dungeon_map as dmap
from game import play_game


def main():
    dlog.debug('Main start')

    size_str = input('size: ')
    size = int(size_str)
    if size <= 0:
        dlog.info('size must be > 0')
        return

    play_game(size)

if __name__ == "__main__":
    main()