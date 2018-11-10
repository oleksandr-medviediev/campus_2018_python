"""
This script solves task 3.6 from Coding Campus 2018 Python course
(Rock, paper, scissors)
"""

import random

weapons = {"rock": 0, "paper": 1, "scissors": 2}
leaderboard = {}


def get_weapon(player_index):
    """
    Gets weapon for current player index. Zero is player, everyone else are bots
    :param player_index: Player index
    :return: Weapon code and weapon name
    """

    weapon_input_string = "Choose your weapon!\n [Rock], [Paper] or [Scissors]!: "
    return_weapon = -1
    return_weapon_name = ""
    if player_index == 0:

        return_weapon_name = get_input(predicate_choose_weapon, weapon_input_string)
        return_weapon_name = return_weapon_name.lower()

    else:
        return_weapon_name = random.choice(list(weapons.keys()))

    return_weapon = weapons[return_weapon_name]

    return return_weapon, return_weapon_name


def get_input(predicate, input_message):
    """
    Gets input from user satisfying given predicate
    :param predicate: Predicate, accepts string, returns tuple of Bool and string (error message)
    :param input_message: Message to display user
    :return: Accepted string
    """

    return_string = ""

    while True:
        string = input(input_message)
        predicate_result, predicate_error_string = predicate(string)

        if predicate_result:

            return_string = string
            break
        else:
            print(predicate_error_string)

    return return_string


def predicate_player_count(string):
    """
    Predicate for player count input
    :param string: String to check
    :return: Tuple of bool and string, where bool signifies result, and string - error message
    """

    bool_result = False
    str_result = ""

    if string.isdigit():

        count = int(string)
        if 2 <= count <= 5:
            bool_result = True
        else:
            str_result = "Unacceptable number of players! Try again"
    else:
        str_result = "Input is not integer! Try again"

    return bool_result, str_result


def predicate_choose_weapon(string):
    """
    Predicate for choose weapon input
    :param string: String to check
    :return: Tuple of bool and string, where bool signifies result, and string - error message
    """

    bool_result = False
    str_result = ""

    if string.lower() in weapons.keys():
        bool_result = True
    else:
        str_result = "Incorrect weapon! You can choose rock, paper or scissors"

    return bool_result, str_result


def predicate_game_end(string):
    """
    Predicate for choosing game end input
    :param string: String to check
    :return: Tuple of bool and string, where bool signifies result, and string - error message
    """

    bool_result = False
    str_result = ""

    if string.lower() == "y" or string.lower() == "n":
        bool_result = True
    else:
        str_result = "Unknown command, try again"

    return bool_result, str_result


def is_beatable(attacker_weapon, defender_weapon):
    """
    Determines whether attacker can beat defender with wielded weapon
    :param attacker_weapon: Index of attacker weapon
    :param defender_weapon: Index of defender weapon
    :return: Bool, True for beatable, False for unbeatable
    """

    return_value = False

    if attacker_weapon == weapons["rock"]:

        if defender_weapon == weapons["scissors"]:
            return_value = True

    elif attacker_weapon == weapons["paper"]:

        if defender_weapon == weapons["rock"]:
            return_value = True

    elif attacker_weapon == weapons["scissors"]:

        if defender_weapon == weapons["paper"]:
            return_value = True

    return return_value


def resolve_brawl(brawl):
    """
    Determines the result of rock-paper-scissors brawl
    :param brawl: Dictionary of player index on chosen weapon index
    :return: List of players still in the game
    """

    weapons_present = set(brawl.values())

    if weapons_present is set(weapons.values()):
        return []

    for attacker_weapon in weapons_present:

        for defender_weapon in weapons_present:

            if is_beatable(attacker_weapon, defender_weapon):
                brawl = {key:val for key, val in brawl.items() if val != defender_weapon}

    return list(brawl.keys())


def play(player_count):
    """
    Plays rock, paper, scissors game
    :param player_count: Amount of players to play with, one player and everyone else are bots
    :return: None
    """

    # Player is zero, everyone else are bots
    global leaderboard

    leaderboard = dict.fromkeys(range(player_count), 0)

    while True:

        play_round()
        user_response = get_input(predicate_game_end, "\n\nContinue? [Y]/[N]: ")

        if user_response.lower() == "n":
            print("Ending game")
            break


def play_round():
    """
    Plays round of rock, paper, scissors and displays leaderboard at the end
    :return:
    """

    global leaderboard

    active_players = list(range(player_count))

    while True:

        brawl = dict.fromkeys(active_players, -1)

        for player_index in active_players:

            player_weapon, player_weapon_name = get_weapon(player_index)
            brawl[player_index] = player_weapon

            print(f"Player {player_index} chose {player_weapon_name}")

        active_players = resolve_brawl(brawl)

        if len(active_players) == 0:

            print("Round ended in draw")
            break

        elif len(active_players) == 1:

            winner_index = active_players[0]
            print(f"Player {winner_index} is winner!")
            leaderboard[winner_index] += 1
            break

        else:
            print(f"Players left: {active_players}\n\n")

    show_leaderboard(leaderboard)


def show_leaderboard(leaderboard):
    """
    Prints leaderboard to console
    :param leaderboard: Dict with player index as key and wins as value pairs
    :return: None
    """

    print("\n===== LEADERBOARD =====")
    for key, value in leaderboard.items():
        print(f"Player {key}, Wins: {value}")


if __name__ == "__main__":

    player_count_input_string = "Input number of players [2-5]: "
    player_count_string = get_input(predicate_player_count, player_count_input_string)
    player_count = int(player_count_string)

    play(player_count)



