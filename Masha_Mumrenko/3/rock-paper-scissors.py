from random import choice


rock, paper, scissors = range(3)
available_weapons = ['rock', 'paper', 'scissors']
weapons_contrrelation = {rock:paper, paper:scissors, scissors:rock}

player_index = 0

leaderboard = []

def form_weapons_set(players_indeces):
    """
    Creates list of random weapon choices for bots and takes input from player
    :param players_indeces: indeces of players in game
    :paramtype players_indeces: list(int)
    :return: weapon choices for the game turn {index of player:weapon_index}
    :rtype: dict(int,int)
    """
    chosen_weapons = { index:available_weapons.index(choice(available_weapons)) for index in players_indeces }

    weapon_validation = False
    while player_index in players_indeces and not weapon_validation:
        
        player_weapon_name = input("Choose a weapon\n").lower()
        weapon_validation = player_weapon_name in available_weapons
        if weapon_validation:
            chosen_weapons[player_index] = available_weapons.index(player_weapon_name)

        
    return chosen_weapons

    
def game_turn(chosen_weapons):
    """
    Game turn logic. Verifies if turn is confusing, determines winners of turn, appends leaderboard with loosers information
    :param: map of player index and weapon choice for the turn
    :paramtype: dict(int,int)
    :return: indeces of winners of turn
    :rtype: list(int)
    """

    distinct_used_weapons = set(chosen_weapons.values())
    turn_winners = [index for index, weapon in chosen_weapons.items() if weapons_contrrelation[weapon] not in distinct_used_weapons]

    loosers = chosen_weapons.keys() - turn_winners

    no_one_lost = len(loosers) == len(chosen_weapons)

    if not no_one_lost:
    
        print_loosers = lambda index : print(f'Bot {index}: lost') if index != player_index else print(f'You: lost')
        [print_loosers(looser_index) for looser_index in loosers]
    
        leaderboard.extend(loosers)
    else:
        turn_winners = chosen_weapons.keys()
        
    
    return turn_winners



def game_loop(players_number):
    """
    Game loop. Prints turn output, game result output and leaderboard. Assignes new set of players - winners of turn and choices of weapons
    :param: number of players in game
    :paramtype: int
    :return: nothing
    :rtype: None
    """
    
    players_indeces = range(players_number)

    print_turn_results = lambda index, weapon: print(f'Bot {index}: {weapon}') if index != player_index else print(f'You: {weapon}')
    print_leaderboard = lambda place, index : print(f'{place}. Bot {index}') if index != player_index else print(f'{place}. You')

    while True:

        turn_weapons = form_weapons_set(players_indeces)

        [print_turn_results(index, available_weapons[weapon]) for index, weapon in turn_weapons.items()]

        turn_winners = game_turn(turn_weapons)

        players_indeces = turn_winners

        if len(turn_winners) == 1:
            
            winner_index = turn_winners[0]
            
            print(f'Bot {winner_index}: won!') if winner_index!= player_index else print(f'You: won!')
            
            leaderboard.append(winner_index)
            [print_leaderboard(len(leaderboard) - leaderboard.index(player_number), player_number) for player_number in leaderboard[::-1]]
            
            break


def game_on():
    """
    Turns the game mode on. Validates the input and asks for one more game
    """
    continue_to_play = True
    while continue_to_play:
        
        validate_number = False
        while not validate_number:
        
            number_of_players = input("Number of players\n")
            validate_number = number_of_players.isnumeric() and int(number_of_players) >= 2
            if validate_number:
                number_of_players = int(number_of_players)   
           
        game_loop(number_of_players)
        
        one_more_game = input("One more game? y/n\n").lower()
        continue_to_play = one_more_game == 'y'
        
        if not continue_to_play:
            break


if __name__ == "__main__":
    
    game_on()
