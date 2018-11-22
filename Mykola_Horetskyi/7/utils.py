from random import randint, choice
from decorator import debug_decorator
from game_logger import logger
from text import wrong_y_n_input


class Position:

    @debug_decorator
    def __init__(self, x, y):
        """
        Constructor of Position class
        """
        self.x = x
        self.y = y

    @debug_decorator
    def generate_random_position(max_x, max_y):
        """
        Generates random position with x and y values at least 0
        and less than x_max and y_max respectively.
        """
        x = randint(0, max_x - 1)
        y = randint(0, max_y - 1)

        return Position(x,y)

    @debug_decorator
    def __add__(self, pos):
        """
        Adds to x and y corresponding values of pos

        param:pos (Position)

        return: (Position)
        """
        result = Position(self.x + pos.x, self.y + pos.y)

        return result


@debug_decorator
def print_dictionary(dict):
    """
    Prints dictionary

    param: dict (dictionary)
    """

    for key, value in dict.items() :
        print("{} : {}".format(key, value))


@debug_decorator
def input_number_from_boundaries(min_value, max_value):
    """
    Prompts user to enter integer in given boundaries.

    return: int from given boundaries that is entered by user
    """
    user_input = input().lower()

    number = None

    while not number and number != 0:

        if (user_input.isdigit()
        and int(user_input) >= min_value
        and int(user_input) <= max_value):
            number = int(user_input)

        if not number:
            logger.debug("incorrect input from user")
            logger.info("please enter number between {} {}".
            format(min_value, max_value))

            user_input = input()

    return number


@debug_decorator
def process_yes_no_input():
    """
    Processes input that shoul be either accept or decline

    return: (bool) True for accept, False for decline
    """
    user_input = input().lower()

    if user_input == "y" or user_input == "yes":
        return True

    elif user_input == "n" or user_input =="no":
        return False

    logger.info(wrong_y_n_input)

    user_input = input().lower()

    if user_input == "y" or user_input == "yes":
        return True

    return False
