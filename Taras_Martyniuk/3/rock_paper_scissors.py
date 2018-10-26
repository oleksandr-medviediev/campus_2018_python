from random import choice
from collections import defaultdict


Rock, Paper, Scissors = range(3)
player_id = 0
# bot indices start from 1

name_to_weapon = {
    'rock' : Rock,
    'paper' : Paper,
    'scissors' : Scissors
}

weapon_to_name = { v : k for k, v in name_to_weapon.items() }

counter_weapons = {
    Scissors : Rock,
    Rock : Paper,
    Paper : Scissors 
}

stats = defaultdict(int)
stats[0] = 2
stats[1] = 10


def get_weapons(bot_ids, player_alive):
    """
        prompts player for his weapon and randoms the bots' choises
        :param bot_ids: list of bot ids
        :returns dict { id : weapon}
    """
    weapons = { id : choice(range(3)) for id in bot_ids }
    
    if player_alive:
        weapon_str = input("Your weapon:\n")
        player_weapon = name_to_weapon[weapon_str.lower()]
        weapons[player_id] = player_weapon
    
    return weapons


def simulate_round(weapons_for_ids):
    """
        plays round, determining who lost
        :param weapons: dict { id : weapon }, player must be present
        :returns: tuple (list of survivour indices, list of loosers indices)
    """
    unique_weapons = set(weapons_for_ids.values())

    survived = lambda weapon: counter_weapons[weapon] not in unique_weapons
    survivours = [id for id, weapon in weapons_for_ids.items() if survived(weapon)]
    survivours = set(survivours)

    ids = weapons_for_ids.keys()
    loosers = set(ids) - survivours

    return survivours, loosers


def format_id(id):
    """
    prints id as bot or player
    """
    return 'You' if id == player_id else f'Bot #{id}'


def run_game(number_of_players):

    """
        simulates game round until everyone have lost or there is a winner
        :param number_of_players: player including
    """

    bot_ids = list(range(1, number_of_players))
    player_alive = True

    while True:
        weapons = get_weapons(bot_ids, player_alive)

        for id, weapon in weapons.items():
            if(id != player_id):
                print(f"Bot {id} chooses {weapon_to_name[weapon]}")

        survivours, loosers = simulate_round(weapons)
        player_alive = player_id in survivours
        
        format_ids = lambda ids : ', '.join(map(format_id, ids))
        print(f'Lost this round : { "no-one" if not loosers else format_ids(loosers)}')

        if len(survivours) == 1:
            (winner,) = survivours
            print(f"Winner: {format_id(winner)}")
            stats[winner] += 1

        if len(survivours) <= 1:
            return

        print(f'survivours : {format_ids(survivours)}')
        bot_ids = survivours.difference({ player_id })


while True:
    number_of_players = int(input('Number of players:'))
    run_game(number_of_players)

    print('Leaderboard:')
    sorted_stats = sorted(stats.items(), key=lambda pair: pair[1], reverse=True)
    for i, (id, _) in enumerate(sorted_stats):
        print(f'{i + 1}.{format_id(id)}')

    ch = input('Play again (y/n)?')
    play_again = ch[0] == 'y'
    if not play_again:
        break






