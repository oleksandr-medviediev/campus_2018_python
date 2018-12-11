import Game_

from tools import dg_decorators
from tools.dg_exсeptios import LoadGameError


dg_decorators.DEBUG_MODE = True


def exceptions_handler(func, on_error_message = None):

    result = None
    try:
        result = func()
    except Exception as error:
        if on_error_message:
            print(on_error_message)
        print(error)
    
    return result


@dg_decorators.decorator_start_end_logging
def main():

    while input("Start the Game? y/n : ") == 'y':
        player_answer = input('(1) new game or (2) saved game : ')
        
        game = exceptions_handler(Game_.Game, "Error in Game initializing")
        if game == None:
            continue

        if player_answer == '2':
            try:
                game.load()
            except LoadGameError as error:
                print(error)
                continue

        elif player_answer != '1':
            print("Wrong input")
            continue

        print(game)
        exceptions_handler(game.loop, "Error in Game process")


main()
