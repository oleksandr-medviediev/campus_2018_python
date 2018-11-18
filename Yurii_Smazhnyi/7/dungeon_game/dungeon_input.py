import decorators


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

            direction = input("input command:")

            if direction in DungeonInput.COMMANDS_TYPES:
                
                return direction


if __name__ == "__main__":
    DungeonInput.get_direction()
