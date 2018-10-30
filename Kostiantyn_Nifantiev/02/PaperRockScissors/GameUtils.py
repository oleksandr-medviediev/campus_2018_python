import random


def bot_generator(weapons_list):
    
    return random.choice(weapons_list)


def get_number_of_players():

    while True:

        try: players_quantity = int(input('Enter prefarable number of players: '))
        
        except: continue
        
        if players_quantity in range(2,6):

            return players_quantity

        else: 

            continue


def get_player_weapon(weapons_list):

    while True:

        player_weapon = input('Enter your weapon: ')

        if player_weapon in weapons_list:

            return player_weapon

        else:

            print('Wrong weapon')
