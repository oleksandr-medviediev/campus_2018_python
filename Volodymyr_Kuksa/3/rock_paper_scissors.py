from random import choice


AVAILABLE_WEAPONS = ('rock', 'paper', 'scissors')
POSITIVE_ANSWERS = ('y', 'yes')
NEGATIVE_ANSWERS = ('n', 'no')


def query_number_of_players():

    number_of_players = input('Enter number of players (2-5): ')

    while not number_of_players.isdigit() or not 2 <= int(number_of_players) <= 5:
        number_of_players = input('Wrong! Try again: ')

    return int(number_of_players)


def query_player_weapon():

    weapon = input('Enter your weapon (rock, paper, scissors): ')

    while not AVAILABLE_WEAPONS.count(weapon):
        weapon = input('Wrong! Try again: ')

    return weapon


def query_weapon(name):

    weapon = ''

    if name == 'You':
        weapon = query_player_weapon()
    else:
        weapon = choice(AVAILABLE_WEAPONS)

    return weapon


def generate_player_names(num_of_players):

    player_names = ['You']

    for i in range(1, num_of_players):
        player_names.append(f'Bot_{i}')

    return player_names


def determine_weakest_weapon_for_round(weapons_presence):

    result = ''

    if weapons_presence['rock'] and weapons_presence['paper'] and not weapons_presence['scissors']:
        result = 'rock'
    elif weapons_presence['rock'] and not weapons_presence['paper'] and weapons_presence['scissors']:
        result = 'scissors'
    elif not weapons_presence['rock'] and weapons_presence['paper'] and weapons_presence['scissors']:
        result = 'paper'

    return result


def determine_loosers(weapons_for_round):

    loosers = []

    weapons_selected = list(weapons_for_round.values())

    weapons_presence = {weapon: bool(weapons_selected.count(weapon)) for weapon in AVAILABLE_WEAPONS}

    weakest_weapon = determine_weakest_weapon_for_round(weapons_presence)

    for player in weapons_for_round.keys():

        if weapons_for_round[player] == weakest_weapon:
            loosers.append(player)

    return loosers


def run_game():

    num_of_players = query_number_of_players()

    active_players = generate_player_names(num_of_players)
    rank = {}

    while len(active_players) > 1:

        weapons_for_round = {player: query_weapon(player) for player in active_players}
        print(weapons_for_round)

        loosers = determine_loosers(weapons_for_round)
        print(loosers)

        for player in active_players:

            if loosers.count(player):

                rank[player] = len(active_players)
                active_players.remove(player)

    rank[active_players[0]] = 1

    print('leaderboard:')
    print(rank)


def query_replay():

    answer = input('Play again? (Y/N): ').casefold()

    while not POSITIVE_ANSWERS.count(answer) and not NEGATIVE_ANSWERS.count(answer):
        answer = input('Wrong! Try again: ').casefold()

    return bool(POSITIVE_ANSWERS.count(answer))


def play_rock_paper_scissors():

    while True:

        run_game()

        if not query_replay():
            break


play_rock_paper_scissors()
