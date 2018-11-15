is_logging_active = False
is_debug_active = False


def select_config_options():
    """
    Prompts user to enable logging and debug output into appropriate files
    """

    while True:

        user_input = input('Do you want to enable logging(type "yes" to enable, "no" otherwise)?: ')

        if user_input == 'yes':

            global is_logging_active
            is_logging_active = True
            break

        elif user_input == 'no':
            break

        print('Invalid input! Try again')

    while True:

        user_input = input('Do you want to enable debug(type "yes" to enable, "no" otherwise)?: ')

        if user_input == 'yes':

            global is_debug_active
            is_debug_active = True
            break

        elif user_input == 'no':
            break

        print('Invalid input! Try again')
