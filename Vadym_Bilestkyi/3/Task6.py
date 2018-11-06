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


if __name__ == '__main__':
    players_amount = int(input('Choose amount of players (2-5): '))
    user_weapon = input('Choose your weapon: ')

    choices = {user_weapon: [0]}
    for i in range(1, players_amount + 1):
        choice = random.choice(weapons)
        choices[choice] = choices.get(choice, [])
        choices[choice].append(i)

    print('choices =', choices)

    winners = run_round(choices)
    print(winners)
