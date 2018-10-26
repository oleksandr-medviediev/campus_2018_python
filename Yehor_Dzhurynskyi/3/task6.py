import random

WEAPON_COLLECTION = ('scissors', 'paper', 'rock')
WEAPON_WINS = {
    'paper': 'rock',
    'rock': 'scissors',
    'scissors': 'paper'
}


def distribute_weapons(players):
    """
    distributes weapons for players
        :param list players: active players
        :return: collection of weapons distributed for each player
        :rtype: list
    """

    weapons = []
    number_of_bots = len(players)

    if 'You' in players:
        number_of_bots -= 1
        while True:
            chosen_weapon = input('Your weapon (scissors/paper/rock): ')
            if chosen_weapon not in WEAPON_COLLECTION:

                print('Wrong input! Select one of this weapon: \'scissors\', \'paper\', \'rock\'')
                continue
            weapons += [chosen_weapon]
            break

    weapons += [random.choice(WEAPON_COLLECTION) for i in range(number_of_bots)]
    return weapons


def is_draw(weapons):
    """
    determining whether game round could be evaluated
        :param list weapons: collection of used weapons
        :return: whether game round has winners
        :rtype: bool
    """

    number_of_unique_weapons = len(set(weapons))
    draw = number_of_unique_weapons == 1 or number_of_unique_weapons == len(WEAPON_COLLECTION)

    return draw


def winner_weapon(weapons):
    """
    determine which weapon is a winner depending on weapons content
        :param list weapons: weapons in current round
        :return: name of winner weapon
        :rtype: str
    """

    if 'paper' not in weapons:
        winner = 'rock'
    elif 'scissors' not in weapons:
        winner = 'paper'
    elif 'rock' not in weapons:
        winner = 'scissors'

    return winner


def print_leaderboard():
    """
    prints leaderboard on game ending
    """

    print(' - Leaderboard')
    print(f'1. {players[0]}')

    for index, name in enumerate(reversed(losers)):

        position = index + 2
        print(f'{position}. {name}')


while True:

    number_of_players_str = input('Number of players: ')
    if not number_of_players_str.isdigit() or int(number_of_players_str) < 2:

        print('Wrong input! Number of players should be positive number [2, ...)')
        continue

    number_of_players = int(number_of_players_str)
    break

players = [f'Bot {playerIndex}' for playerIndex in range(1, number_of_players)]
players.insert(0, 'You')
losers = []


while True:

    print(' - Next turn')
    weapons = distribute_weapons(players)

    player_weapon_dict = dict(zip(players, weapons))
    for player, weapon in player_weapon_dict.items():
        print(f'{player}: {weapon}')

    if is_draw(weapons):
        print(' - Draw')
        continue

    def is_winner(player): return player_weapon_dict[player] == winner_weapon(weapons)

    def is_loser(player): return player_weapon_dict[player] != winner_weapon(weapons)

    losers += list(filter(is_loser, players))
    players = list(filter(is_winner, players))

    if len(players) == 1:
        winner_message = f' - {players[0]} won!'
        print(winner_message)

        print_leaderboard()
        break
