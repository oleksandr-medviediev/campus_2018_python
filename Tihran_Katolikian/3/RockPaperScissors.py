import random


def first_beats_second(first_weapon, second_weapon):
    '''
    Function takes 2 weapon names as arguments and resolves a fight between
    this weapons and returns a result
    :param first_weapon: a name of first weapon
    :param second_weapon: a name of second weapon
    :return: True if first weapon beats second, False otherwise
    :type first_weapon: a string
    :type second_weapon: a string
    :rtype: bool
    '''
    weapons_map = {
        'rock' : 'scissors',
        'paper' : 'rock',
        'scissors' : 'paper'
    }

    if weapons_map[first_weapon] is second_weapon:
        result = True
    else:
        result = False

    return result


def validate_weapon_input():
    '''
    Function validates weapon input and works until used will input a correct weapon
    name
    :return: a choosen weapon
    :rtype: string
    '''
    weapon_choice_map = {
        '1' : 'rock',
        '2' : 'paper',
        '3' : 'scissors'
    }

    while True:
        print('Please, choose your weapon:\n1 to pick a rock;\n2 to pick a paper;\n3 to pick a scissors.')
        weapon_choice = input("Your choice: ")
        if weapon_choice in weapon_choice_map.keys():
            return weapon_choice_map[weapon_choice]


def get_random_weapon():
    '''
    Function returns a random weapon
    :return: a random weapon name
    :rtype: a string
    '''
    weapons = ['rock', 'paper', 'scissors']
    result = random.choice(weapons)
    return result


def run_game_stage(players_and_statuses):
    '''
    Function runs a game stage and returns a list of winners and their statuses
    :param players_and_statuses: a list of tuples with player name and it's status.
    Status is a string that equals 'human' if player is user or 'bot' if player is
    bot
    :return: a list of tuples with player name and it's status
    '''
    players_and_weapons = {}
    for player_name, status in players_and_statuses:
        if status is 'human':
            picked_weapon = validate_weapon_input()
            players_and_weapons[(player_name, status)] = picked_weapon
        else:
            picked_weapon = get_random_weapon()
            players_and_weapons[(player_name, status)] = picked_weapon
        print(f'{player_name} picks {picked_weapon}')
    
    stage_winners = players_and_statuses

    for first_player, first_weapon in players_and_weapons.items():
        for second_player, second_weapon in players_and_weapons.items():
            first_player_won = first_beats_second(first_weapon, second_weapon)
            if first_player_won and second_player in stage_winners:
                print(f'{first_player} wins {second_player}!')
                stage_winners.remove(second_player)

    return stage_winners


def choose_number_of_players():
    '''
    Function is used to choose and validate a number of players according
    to the rules
    :return: the number of players
    :rtype: integer
    '''
    while True:
        number_of_players = input("Please, choose a number of players (2 - 5): ")
        if not number_of_players.isdigit():
            continue
        
        number_of_players = int(number_of_players)
        if number_of_players not in range(2, 6):
            continue
        else:
            return number_of_players

game_should_continue = True

while game_should_continue:
    number_of_players = choose_number_of_players()

    players = [('You', 'human')]
    for i in range(1, number_of_players):
        players.append((f'Player {i}', 'bot'))

    round_number = 1
    while len(players) > 1:
        print(f'---------------------------------Round {round_number}. Fight!-------------------------------')
        round_number += 1
        players = run_game_stage(players)

    if len(players) is 0:
        print('Draw!')
    else:
        print(f'Winner: {players[0]}')
    should_continue = input('Play again? \'y\' means yes, any other key means no:')
    game_should_continue = should_continue is 'y'
