import random

possible_weapons = ['rock', 'paper', 'scissors']

def recognize_player_numbers():

    """ Function returns input of player numbers

        Args:
            (none)

        Returns:
            int: expected player's number

    """
    
    numbers = int(input('Enter amount of players: '))
    
    return numbers


def recognize_player_weapon():

    """ Function returns input of player's weapon

        Args:
            (none)

        Returns:
            str: expected player's weapon from possible_weapons

    """
    
    weapon = input('Your weapon: ')
    while (weapon not in possible_weapons):
        print('Wrong weapon!')
        weapon = input('Your weapon: ')

    return weapon
    

def show_weapons(statistic_list):

    """ Function shows all weapons of players (not loosers) using statistics

        Args:
            (none)

        Returns:
            void: print this weapons in terminal

    """
    
    if not statistic_list[0]['is_looser']:
        print('You:', statistic_list[0]['weapon'])
        
    for i in range(1, len(statistic_list)):
        statistic = statistic_list[i]
        if not statistic['is_looser']:
            index = statistic['index']
            weapon = statistic['weapon']
            print('Bot {0}: {1}'.format(index, weapon))


def get_weapons_from_statistics(statistic_list):

    """ Function takes weapons from statistic list to pass it next
        to check best weapon

        Args:
            statistic_list(list): list of players statistics

        Returns:
            list: list of player's weapons

    """
    
    weapons_list = []
    for i, statistic in enumerate(statistic_list):
        if not statistic['is_looser']:
            weapons_list.append(statistic['weapon'])

    return weapons_list
                                      
    
def recognize_winner_weapon(weapon_set):

    """ Function recognize winner from weapon set and return winner weapon

        Args:
            weapon_set(set): set with two different elements

        Returns:
            str: winner weapon

    """
    
    win_weapon = None
    
    if weapon_set == set({'rock', 'scissors'}):
        win_weapon = 'rock'
    elif  weapon_set == set({'rock', 'paper'}):
        win_weapon = 'paper'
    elif  weapon_set == set({'paper', 'scissors'}):
        win_weapon = 'scissors'
    
    return win_weapon


def get_name_by_index(index):

    """ Function return full name of player by its index

        Args:
            index(int): player's index

        Returns:
            str: player's full name 

    """
    
    winner_name = 'You'
    
    if index:
        winner_name = 'Bot {}'.format(index)

    return winner_name
    

def show_leaderboard(statistic_list):

    """ Function show leaderboard in terminal by sorting of statistic list
        by score.

        Args:
            statistic_list(list): list of players statistics

        Returns:
            void: print leaderboard in terminal

    """
    
    print('Leaderboard')
    statistic_list.sort(key=lambda x: -x['points'])
    
    for i, statistic in enumerate(statistic_list):
        index = statistic['index']
        player_name = get_name_by_index(index)
        print('{index}. {name}'.format(index=i, name=player_name))


def reset_statistics(statistic_list):

    """ Function reset statistic list to start game again

        Args:
            statistic_list(list): list of players statistics

        Returns:
            void: zeroing all statistic values and sort by index

    """
    for i, el in enumerate(statistic_list):
        statistic_list[i]['points'] = 0
        statistic_list[i]['is_looser'] = False
        statistic_list[i]['weapon'] = None

    statistic_list.sort(key=lambda x: x['index'])

    
def start_game():

    """ Function is entry point to game

        Args:
            (none)

        Returns:
            void: process game

    """
    
    player_numbers = recognize_player_numbers()

    bots_numbers = player_numbers - 1

    statistics = []
    for i in range(player_numbers):
        statistics.append({'index': i,
                           'points': 0,
                           'is_looser': False,
                           'weapon': None})

    has_winner = False

    is_need_restart = True
    while is_need_restart:
        while not has_winner:

            if not statistics[0]['is_looser']:
                player_weapon = recognize_player_weapon()
                statistics[0]['weapon'] = player_weapon

            for i in range(bots_numbers):
                bot_choice = random.choice(possible_weapons)
                statistics[i + 1]['weapon'] = bot_choice

            show_weapons(statistics)
                                              
            current_turns = get_weapons_from_statistics(statistics)
            all_variants = set(current_turns)
            if len(all_variants) == 2:
                win_weapon = recognize_winner_weapon(all_variants)
                winners_count = 0
                winner_index = 0
                for i, statistic in enumerate(statistics):
                    if not statistic['is_looser']:
                        if statistic['weapon'] != win_weapon:
                            statistics[i]['is_looser'] = True
                        else:
                            statistics[i]['points'] += 1
                            winners_count += 1
                            winner_index = i

                if winners_count == 1:
                    has_winner = True
                    winner_name = get_name_by_index(winner_index)
                    print(winner_name + ' won!')
                else:
                    print('Left:', winners_count)
                
            else:
                print('Draw.')

        
        show_leaderboard(statistics)

        choice = input('Play again? y/n\n')
        if choice != 'y':
            is_need_restart = False
        else:
            reset_statistics(statistics)
            has_winner = False
