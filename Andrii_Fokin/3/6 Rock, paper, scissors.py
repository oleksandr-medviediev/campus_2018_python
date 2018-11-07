from random import choice


weapons = [1, 2, 3]
weapons_name = ["Scissors", "Paper", "Rock"]


def weapons_of_bots(number_of_bots):
    result = [choice(weapons) for i in range(number_of_bots)]
    return result


def weapon_of_player():
    weapon = input("Your weapon: \n1 - Scissors \n2 - Paper \n3 - Rock\n")
    return int(weapon)


def weapons_print(weapons_dict):
    for key in weapons_dict.keys():
        print('You : ' if key == 'P' else f"Bot {key} : ", weapons_name[weapons_dict[key] - 1])


def get_best_weapon(weapons):
    weapons_set = set(weapons)
    weapons_list = [*weapons_set]
    
    result = weapons_list[1] if abs(weapons_list[0] - weapons_list[1]) == 2 else weapons_list[0]
    return result


def game_loop(number_of_players):
    """One game session"""
    number_of_bots = number_of_players - 1
    bots = [(f'{i + 1}', 0) for i in range(number_of_bots)]
    players = dict([("P", 1), *bots])

    while (len(players) > 1):
        print('Players : ', *map(lambda key: 'You' if key == 'P' else f'Bot_{key}', players.keys()))
        for key in players.keys():
            players[key] = choice(weapons) if key != 'P' else weapon_of_player()
        
        weapons_print(players)
        if len(set(players.values())) != 2:
            print("Tie")
        else:
            best_weapon = get_best_weapon(players.values())
            winers = [key for key in players.keys() if players[key] == best_weapon]
            players = dict((name, 0) for name in winers)
        print('--------------------------------\n')
    return None



while(True):
    number_of_player = input("Number of players:")
    game_loop(int(number_of_player))

    if input("Play again (y/n)?") == 'n':
        break
