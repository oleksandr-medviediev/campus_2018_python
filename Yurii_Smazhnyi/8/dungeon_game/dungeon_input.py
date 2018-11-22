import decorators
from dungeon_exceptions import IncorrectCommandError
import custom_log

class DungeonInput:
    """
    Class Handling player's input.

    Attributes
    :COMMANDS_TYPES: list of all supported commands
    """


    COMMANDS_TYPES = ("left", "right", "down", "up", "save", "load")


    @staticmethod
    @decorators.info_decorator
    @decorators.debug_decorator
    def get_direction():
        """
        Get direction from player.

        :returns: one of valid direction from COMMANDS_TYPES.
        :rtype: str.
        """

        while True:

            try:
                direction = input("input command:")
                
                if not isinstance(direction, str):
                    raise ValueError

                if direction in DungeonInput.COMMANDS_TYPES:
                    
                    return direction
                
                raise IncorrectCommandError

            except IncorrectCommandError:
                custom_log.logger.info("Incorrect command, try again!")
                continue
            
            except ValueError:
                custom_log.logger.info("You've input not string, try again!")
                continue


if __name__ == "__main__":
    DungeonInput.get_direction()
