from random import choice
from collections import Counter
import sys


print("Rock, paper, scissors game")

WEAPON_ID = {'rock': 0, 'paper': 1, 'scissors': 2}
WEAPON_TYPE_BY_ID = {0: "rock", 1: "paper", 2: "scissors"}

# see get_winner function for details
WEAPON_EFFECT_BY_ID = [[0, 2, 1],
                       [1, 0, 2],
                       [2, 1, 0]]

is_user_in_game = True
is_one_more_game = True

def select_amount_of_players():
    """
    Process input until user enters correct amount of players(min 2, max 5)

    :return: amount of players
    :rtype: int
    """

    while True:

        user_input = input("Enter amount of players: ")

        if user_input.isdigit() and int(user_input) in range(2, sys.maxsize):
            return int(user_input)

        else:
            print("Invalid input, try again.")


def select_user_weapon():
    """
    Process input until user enters correct type of weapon

    :return: weapon id
    :rtype: int
    """

    while True:

        user_input = input("Enter weapon type(rock, paper or scissors): ")

        weapon_id = WEAPON_ID.get(user_input)
        
        if weapon_id != None:
            return weapon_id

        else:
            print("Invalid input, try again.")


def generate_bots(amount_of_players):
    """
    Generates bots dict in range(0 + user, amount of players) with name 'Bot' + number and empty value

    :param int amount_of_players: amount of players in game
    :return: dict of Bots with numbers and empty values
    :rtype: dict
    """

    bots_dict = {f"Bot{x}" for x in range(1, amount_of_players)}

    return bots_dict

        
def generate_weapon_for_bots(bots):
    """
    Generates bots weapons' using random.choice()

    :param list bots: amount of players minus user
    :return: dict with bot as key and weapon id as value
    :rtype: dict
    """

    bots_weapons = {bot:choice([0, 1, 2]) for bot in bots}

    return bots_weapons


def get_winner(weapon_types):
    """
    Using WEAPON_EFFECT_BY_ID, function determines the winner
    0 is Draw, 1 is first weapon wins, 2 is second weapon wins

    :param list weapon_types: list with current active weapons ids
    :return: id of winner weapon
    :rtype: int
    """
    
    winner = WEAPON_EFFECT_BY_ID[weapon_types[0]][weapon_types[-1]]

    if winner == 1:
        return weapon_types[0]

    else:
        return weapon_types[-1]


def resolve_turn(active_players, weapon_types):
    """
    Finds winner weapon and creates new dict of won players

    :param dict active_players: current dict of active players and theirs weapons
    :param list weapon_types: list with 2 pairs - weapon id, amount of this weapon
    :return: dict with won players with None values
    :rtype: dict 
    """

    global is_user_in_game
    new_active_players = {}

    winner_weapon = get_winner(list(weapon_types))
    print("Winners of the round: ")

    for player, weapon in active_players.items():

        if weapon == winner_weapon:

            new_active_players[player] = -1
            print(f"{player}")

    empty_input = input("Press Enter to proceed")

    if is_user_in_game and new_active_players.get('User') == None:
        is_user_in_game = False

    return new_active_players


def process_turn(active_players):
    """
    Prints players and their weapons
    Counts weapon types and process players according to amount:
        if there are 2 types - resolving turn
        otherwise - remove user record

    :param dict active_players: dict with player, weapon id
    :return: dict with winner players or with removed user
    :rtype: dict
    """

    new_active_players = active_players

    for player, weapon_id in new_active_players.items():
        print(f"{player} has {WEAPON_TYPE_BY_ID.get(weapon_id)}")

    counter_result = Counter(new_active_players.values())
    weapon_types = dict(counter_result.items())

    if len(weapon_types) == 2:
        new_active_players = resolve_turn(new_active_players, weapon_types.keys())
    
    else:

        empty_input = input("Nothing interesting, press enter to continue")

        if is_user_in_game:
            new_active_players.pop('User')

    return new_active_players


def replay_game():
    """
    Process input from user whether or not he wants to play one more game

    :return: True if user enters 'yes', false otherwise
    :rtype: bool
    """

    global is_user_in_game

    user_input = input("One more game?(type 'yes' to replay or whatever you want to quit): ")

    if user_input == "yes":

        is_user_in_game = True
        return True

    else:
        return False


def game_func():
    """
    Starts and processes game cycle
    After game finish user can replay or exit

    :return: None
    :rtype: None
    """

    while True:

        players_amount = select_amount_of_players()
        generated_bots = generate_bots(players_amount)

        active_players = generate_weapon_for_bots(generated_bots)
        active_players['User'] = select_user_weapon()

        while True:

            active_players = process_turn(active_players)

            if len(active_players) == 1:
                break

            active_players = generate_weapon_for_bots(active_players)

            if is_user_in_game:
                active_players['User'] = select_user_weapon()

        winner = list(active_players.keys())
        print(f"{winner[0]} won!")
        
        is_one_more_game = replay_game()

        if not is_one_more_game:
            break


game_func()
