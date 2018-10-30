def hands_input():
    """
    Prompts user to enter poker hands to compare. Ends on empty input

    :return: list of hands
    :rtype: list
    """

    hands = []
    user_input = input("Enter hands to compare(use empty input to proceed): ")

    while len(user_input) > 0:

        hands.append(user_input)
        user_input = input("Enter hands to compare(use empty input to proceed): ")

    return hands
