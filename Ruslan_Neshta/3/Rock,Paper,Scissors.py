from random import choice


def get_amount_of_bots():
    """
    Gets amount of bots from user

    :return: amount of bots
    :rtype: int
    """

    try:
        amount = int(input("Enter number of players:"))

    except ValueError:
        print("Please, enter a number.")
        amount = get_amount_of_bots()

    return amount


def get_player_input(possible_inputs):
    """
    Gets players choice and returns it

    :param possible_inputs: list of possible inputs

    :return: players choice
    :rtype: str
    """

    is_input_correct = False
    user_choice = 'rock'

    while not is_input_correct:
        user_choice = input("Your weapon:")

        if possible_inputs.count(user_choice) != 0:
            is_input_correct = True
        else:
            print("You can't choose this weapon. Consider one of:", *possible_inputs, sep="\n")

    return user_choice


def generate_bots_input(amount_of_bots, possible_inputs):
    """
    Generates bots choices

    :param amount_of_bots: amount of bots
    :param possible_inputs: list of possible inputs

    :return: list of bots choices
    :rtype: list
    """

    result = []

    for index in range(amount_of_bots):
        result.append(choice(possible_inputs))

    return result


def get_winner_id(players_weapons, possible_inputs, checker):
    """
    Returns id of winner, if any
    -1 otherwise

    :param players_weapons: list of strings
    :param possible_inputs: list of available input values
    :param checker: function for winner detection in 100% winnable case scenario

    :return: index of winner in players_weapon
    :rtype: int
    """

    items_found = 0
    for it in possible_inputs:

        if players_weapons.count(it) > 0:
            items_found += 1

    if items_found == len(possible_inputs):
        result = -1
    else:
        result = checker(players_weapons)

    return result


def rock_paper_scissors_winner_checker(inputs):
    """
    Returns winner index from given input

    :param inputs: input

    :return: winner index, if any
    :rtype: int
    """
    try:
        if inputs.count('paper') == 0:
            winners_index = inputs.index('rock')

        elif inputs.count('rock') == 0:
            winners_index = inputs.index('scissors')

        else:
            winners_index = inputs.index('paper')

    except ValueError:
        winners_index = -1

    return winners_index


def rock_paper_scissors():
    """
    Returns inputs list and function checker for winnable validated result

    :return: inputs list and function checker
    :rtype: tuple
    """

    return ['rock', 'paper', 'scissors'], rock_paper_scissors_winner_checker


def play(amount_of_players):
    """
    Gets user input and returns winners name

    :param amount_of_players: int

    :return: winners index, players answers
    :rtype: tuple
    """

    possible_inputs, winner_checker = rock_paper_scissors()

    weapons = [get_player_input(possible_inputs)]
    weapons.extend(generate_bots_input(amount_of_players - 1, possible_inputs))

    winners_id = get_winner_id(weapons, possible_inputs, winner_checker)

    return winners_id, weapons


def create_report(winner_index, answers):
    """
    Returns list of inputs and results

    :param winner_index: index of winner
    :param answers: answers of players

    :return: list of strings
    :rtype: list
    """

    reports = ["You: " + answers[0]]

    for index in range(1, len(answers)):
        reports.append("Bot " + str(index) + ": " + answers[index])

    if winner_index == 0:
        reports.append("You won!")

    elif winner_index == -1:
        reports.append("Nobody won =/")

    else:
        reports.append("Bot " + str(winner_index) + " won!")

    return reports


def check_end_game():
    """
    Checks if user want's to play again

    :return: bool flag if player wants to end the game
    :rtype: bool
    """

    end = input("Play again?(Y/N)")
    result = False

    if end.lower() == "n":
        result = True

    return result


def launch_game():
    """
    Starts main game cycle

    :return: nothing
    :rtype: None
    """

    game_over = False

    while not game_over:
        players_amount = get_amount_of_bots()
        winner, answers = play(players_amount)

        report = create_report(winner, answers)
        print(*report, sep="\n")

        game_over = check_end_game()


if __name__ == "__main__":
    launch_game()
