from random import choice

WEAPON_TYPES = ("rock", "paper", "scissors")

APPLY_WEAPON = { WEAPON_TYPES[0] : WEAPON_TYPES[2], 
                 WEAPON_TYPES[1] : WEAPON_TYPES[0],
                 WEAPON_TYPES[2] : WEAPON_TYPES[1] }


def is_valid(weapon_list):
    """
    Check is list of weapons not contains all type of weapons.

    :param weapon_list: all ingame weapons
    :weapon_list type: list of strings.
    :returns: result of check.
    :rtype: bool.
    """

    weapon_count = 0

    for weapon in WEAPON_TYPES:

        if weapon in weapon_list:
            weapon_count += 1

    return weapon_count != 1 and weapon_count != len(WEAPON_TYPES)


def get_win_weapon(weapon_list):
    """
    Checks whether list of weapons is valid

    :param weapon_list: list of weapons.
    :weapon_list type: list of str.
    :returns: result of check.
    :rtype: str.
    """

    for weapon in weapon_list:

        if APPLY_WEAPON[weapon] in weapon_list:
            return weapon


def play_round(amount_of_players):
    """
    Play round of rock-paper-scissors game

    :param amount_of_players: current amount of players.
    :amount_of_players: int.
    :returns: amount of players that stayed alive.
    :rtype: int.
    """

    while True:

        player_weapon = input(f"choose weapon from {WEAPON_TYPES} :")

        if player_weapon not in WEAPON_TYPES:

            print("Incorrect weapon - Restarting!")
            continue

        bots_weapon = []

        for i in range(amount_of_players - 1):

            bots_weapon.append(choice(WEAPON_TYPES))

        all_weapons = []

        all_weapons.extend(bots_weapon)
        all_weapons.append(player_weapon)

        if not is_valid(all_weapons):

            print("Confusing situations - Restarting!")
            continue

        win_weapon = get_win_weapon(all_weapons)

        if win_weapon != player_weapon:

            print("You Loose")
            return 
        
        alive_players = bots_weapon.count(win_weapon)

        return alive_players + 1


def print_leaderboard(position, amount_of_players):
    """
    Prints Leaderboard

    :param position: index of players in leaderboard.
    :param amount_of_players: size of leaderboard.
    :position type: int.
    :amount_of_players: int.
    :returns: None
    """

    print("Leaderboard:")
    
    for i in range(amount_of_players):

        if i == position:
            print("You")
        else:
            print(f"Bot: {i}")


def start_game():

    amount_of_players = ""

    while not amount_of_players:

        amount_of_players = input("Number of players:")

        if not amount_of_players.isnumeric():
            amount_of_players = ""
            continue

        amount_of_players = int(amount_of_players)
        players_left = amount_of_players

        if players_left < 2:
            continue


    while True:   
        
        players_left = play_round(players_left)

        if players_left == 1:

            print_leaderboard(0, amount_of_players)

            return None
        
        elif players_left is None:

            print_leaderboard(amount_of_players - 1, amount_of_players)

            return None

start_game()
