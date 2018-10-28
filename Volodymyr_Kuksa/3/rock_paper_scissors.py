from random import choice


AVAILABLE_WEAPONS = ('rock', 'paper', 'scissors')
POSITIVE_ANSWERS = ('y', 'yes')
NEGATIVE_ANSWERS = ('n', 'no')


def query_number_of_players():
    """
    Query input that is a number from 2 to 5.

    :return: entered number.
    :rtype: int.
    """
    number_of_players = input('\nEnter number of players (2-5): ')

    while not number_of_players.isdigit() or not 2 <= int(number_of_players) <= 5:
        number_of_players = input('Wrong! Try again: ')

    return int(number_of_players)


def query_player_weapon():
    """
    Query input that represents a weapon (rock, paper, scissors).

    :return: entered weapon.
    :rtype: str.
    """
    weapon = input('\nEnter your weapon (rock, paper, scissors): ')

    while not AVAILABLE_WEAPONS.count(weapon):
        weapon = input('Wrong! Try again: ')

    return weapon


def choose_weapons(name):
    """
    Choose/Query weapons for a participant of the game.

    :param name: name of the participant.
    :type name: str.

    :return: name of the weapon.
    :rtype: str.
    """
    if name == 'You':
        weapon = query_player_weapon()
    else:
        weapon = choice(AVAILABLE_WEAPONS)

    return weapon


def generate_player_names(num_of_players):
    """
    Generate list of player names.

    :param num_of_players: number of players.
    :type num_of_players: int.

    :return: list of player names.
    :rtype: list.
    """
    player_names = ['You']

    for i in range(1, num_of_players):
        player_names.append(f'Bot_{i}')

    return player_names


def determine_weakest_weapon_for_round(weapons_presence):
    """
    Return the name of the weakest weapon in the round.

    :param weapons_presence: dict that determines if the weapon is present in current round.
    :type weapons_presence: dict(weapon_name: bool).

    :return: name of the weakest weapon in the round.
    :rtype: str.
    """
    result = ''

    if weapons_presence['rock'] and weapons_presence['paper'] and not weapons_presence['scissors']:
        result = 'rock'
    elif weapons_presence['rock'] and not weapons_presence['paper'] and weapons_presence['scissors']:
        result = 'scissors'
    elif not weapons_presence['rock'] and weapons_presence['paper'] and weapons_presence['scissors']:
        result = 'paper'

    return result


def determine_losers(weapons_for_round):
    """
    Return list of players hwo lost in the current round.

    :param weapons_for_round: dict that represents the choice of weapon by each player.
    :type weapons_for_round: dict(player_name: weapon_name).

    :return: list of players who lost in the current round.
    :rtype: list.
    """
    losers = []

    weapons_selected = list(weapons_for_round.values())

    weapons_presence = {weapon: bool(weapons_selected.count(weapon)) for weapon in AVAILABLE_WEAPONS}

    weakest_weapon = determine_weakest_weapon_for_round(weapons_presence)

    for player in weapons_for_round.keys():

        if weapons_for_round[player] == weakest_weapon:
            losers.append(player)

    return losers


def display_choice_of_weapons(weapons_for_round):
    """
    Display choice of weapons for each player in game.

    :param weapons_for_round: dict of player names and their weapons.
    :type weapons_for_round: dict(player_name: weapon_name).

    :return: None
    """
    names = tuple(weapons_for_round.keys())
    weapons = tuple(weapons_for_round.values())

    print('\nWeapon of the round:')

    for i in range(len(names)):
        print(f'{names[i]} chose {weapons[i]}.')


def display_losers(losers):
    """
    Display all losers for the round.

    :param losers: list of losers.
    :type losers: list.

    :return: None.
    """
    if not len(losers):
        print('\nDRAW!')
    else:
        print('\nLosers of the round:')

    for loser in losers:
        print(f'{loser} dropped out.')


def display_leader_board(rank):
    """
    Display leader board.

    :param rank: list of player names, sorted in descending order according to their rank.
    :type rank: iterable

    :return: None
    """
    print('\nLeader Board:')

    for place, player in enumerate(reversed(rank)):

        print(f'{place + 1}. {player}')


def run_game():
    """
    Execute game logic until there is only one player left.

    :return: None.
    """
    num_of_players = query_number_of_players()

    active_players = generate_player_names(num_of_players)
    rank = []

    while len(active_players) > 1:

        weapons_for_round = {player: choose_weapons(player) for player in active_players}
        display_choice_of_weapons(weapons_for_round)

        losers = determine_losers(weapons_for_round)
        display_losers(losers)

        for loser in losers:

            rank.append(loser)
            active_players.remove(loser)

    rank.extend(active_players)

    display_leader_board(rank)


def query_replay():
    """
    Query the player to play again.

    :return: True if the player wants to play again, False otherwise.
    :rtype: bool.
    """
    answer = input('\nPlay again? (Y/N): ').casefold()

    while not POSITIVE_ANSWERS.count(answer) and not NEGATIVE_ANSWERS.count(answer):
        answer = input('Wrong! Try again: ').casefold()

    return bool(POSITIVE_ANSWERS.count(answer))


def play_rock_paper_scissors():
    """
    Run games of rock paper scissors as long as player wants to.

    :return: None.
    """
    while True:

        run_game()

        if not query_replay():
            break


play_rock_paper_scissors()
