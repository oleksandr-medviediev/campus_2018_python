import random


def validate_play_again_choice():
    """
    This method is used to validate play again choice
    :return: a True if player want to play again, False otherwise
    """
    choice = input('Play again? <any key> - yes, q - no')
    return choice is not 'q'


def validate_weapon_choice():
    """
    This method is used to validate the weapon choice
    :return: a string with a weapon name
    """

    weapon_choices = {
        1 : 'rock',
        2 : 'paper',
        3 : 'scissors'
    }

    while True:
        print('Please, choose your weapon:')
        choice = input('1 - rock;\n2 - paper;\n3 - scissors\n')
        if int(choice) not in weapon_choices.keys():
            continue
        else:
            return weapon_choices[int(choice)]



def resolve_fight(left_weapon, right_weapon):
    """
    Used to resolve fights between 2 weapons
    :param left_weapon: one of 2 weapons
    :param right_weapon: one of 2 weapons
    :type param left_weapon: string
    :type param right_weapon: string
    :return: True if left_weapon beats right_weapon, False if right_weapon beats left_weapon, None if weapons are equal
    :type return: bool or None
    """

    result = None

    if left_weapon == 'rock':
        if right_weapon == 'scissors':
            result = True
        elif right_weapon == 'paper':
            result = False
    elif left_weapon == 'scissors':
        if right_weapon == 'paper':
            result = True
        elif right_weapon == 'rock':
            result = False
    else:
        if right_weapon == 'rock':
            result = True
        elif right_weapon == 'scissors':
            result = False

    return result


def random_weapon_gen():
    """
    Used for 'Rock, paper, scissors' game to generate a randomly choosen weapon
    :return: randomly choosen weapon
    :type return: string
    """
    weapons = ['rock', 'paper', 'scissors']
    return random.choice(weapons)


def run_game_stage(active_players):
    """
    Used to simulate a game stage
    :param active_players: a list of tuples that contain names of players and type of player
    :type active_players: a list of strings
    :return: a list of tuples with player name and player status
    :type return: a list of strings
    """
    players_and_weapons = {}
    for player, player_type in active_players:
        weapon = ''
        if player_type is 'human': # human
            weapon = validate_weapon_choice()
            players_and_weapons[(player, player_type)] = weapon
        else: #bot
            weapon = random_weapon_gen()
            players_and_weapons[(player, player_type)] = weapon
        print(f'Player {player} picks weapon {weapon}')

    winners = active_players
    for one_player, one_weapon in players_and_weapons.items():
        for other_player, other_weapon in players_and_weapons.items():
            if one_player != other_player:
                result = resolve_fight(one_weapon, other_weapon)
                if result == True:
                    if other_player in winners:
                        winners.remove(other_player)
    winners = list(set(winners))

    print(f'Stage winners: {winners}')

    return winners

should_run = True

number_of_players = int(input('Number of players: '))

while should_run:
    players = [('You', 'human')]
    for i in range(1, number_of_players):
        players.append((f'Player{i}', 'bot'))

    survivors = players
    while len(survivors) > 1:
        print('-----------------------------------------------------------')
        input('Press something to run game stage')
        survivors = run_game_stage(survivors)

    print('Game over!')
    should_run = validate_play_again_choice
