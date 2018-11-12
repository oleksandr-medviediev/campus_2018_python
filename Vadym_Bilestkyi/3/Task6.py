import random


weapons = ['rock', 'paper', 'scissors']


rules = {
    ('rock', 'scissors'):   True,
    ('rock', 'paper'):      False,
    ('paper', 'rock'):      True,
    ('paper', 'scissors'):  False,
    ('scissors', 'paper'):  True,
    ('scissors', 'rock'):   False,
}


def get_stronger_weapon(weapon1, weapon2):
    return weapon1 if rules[weapon1, weapon2] else weapon2


def run_round(choices):
    if len(choices) > 2 or len(choices) == 1:
        return []

    return choices[get_stronger_weapon(*choices.keys())]


def run_bots(bots):
    choices = {}
    for i in bots:
        choice = random.choice(weapons)
        choices[choice] = choices.get(choice, [])
        choices[choice].append(i)

    return choices


def player_to_str(player_index, user_index):
    if player_index == user_index:
        return 'You'
    else:
        return 'Bot #{}'.format(player_index)


def print_choices(choices, players, user_index):
    for i in players:
        for choice, players in choices.items():
            if i in players:
                print('{}: {}'.format(player_to_str(i, user_index), choice))
                break


def print_leaderboard(winners, losers, user_index):
    print('LeaderBoard:')

    leaderboard = [winners]
    for round_number in reversed(sorted(losers.keys())):
        leaderboard.append(losers[round_number])

    for i, players in enumerate(leaderboard, 1):
        row = ', '.join(player_to_str(player_index, user_index) for player_index in players)
        print('{}. {}'.format(i, row))


def game_loop():
    players_amount = int(input('Choose amount of players (2-5): '))

    user_index = 0
    players = set(range(players_amount))
    winners = []
    losers = {}
    round_number = 0
    while len(winners) != 1:
        round_number += 1
        print('Round #{}'.format(round_number))

        choices = run_bots(players - {user_index})

        if user_index in players:
            user_weapon = input('Choose your weapon: ')
            choices[user_weapon] = choices.get(user_weapon, [])
            choices[user_weapon].append(user_index)

        print_choices(choices, players, user_index)

        winners = run_round(choices)

        if len(winners) >= 1:
            losers[round_number] = players - set(winners)
            players = set(winners)
        elif len(winners) == 0:
            print('Draw')

    if user_index in winners:
        print('You won.')
    else:
        print('You lose')

    print_leaderboard(winners, losers, user_index)


if __name__ == '__main__':
    prompt = 'y'

    while prompt != 'n':
        game_loop()
        prompt = input('Play again (y/n)?')
