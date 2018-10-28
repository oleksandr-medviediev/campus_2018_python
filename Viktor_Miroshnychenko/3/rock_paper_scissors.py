from random import choice


WEAPONS = ["scissors", "rock", "paper"]

bots = {}
losers = []
player_name = ""
user_lost = False

def generate_bots(amount):
    """
    :param number: - amount of bots to generate
    :type amount: - int

    :return: - dict of bots name and the weapon
    :rtype: dict
    """

    ret_val = {}
    while amount != 0:
        bot_name = "Bot " + str(amount)
        ret_val[bot_name] = ""
        amount -= 1

    return ret_val



def read_user_input():
    """
    :descripto: reads user input in order to get on of weapons to continue game
    
    :return: weapon which user choosen
    :rtype: str
    """

    if user_lost:
        return

    user_input = ""
    while user_input not in WEAPONS:
        user_input = input("Ener your choice \n")

    return user_input



def generate_bots_input():
    """
    :return: dict of bots names with input
    :rtype: dict
    """

    global bots
    for bot in bots:
        bots[bot] = choice(WEAPONS)

 


def delete_loosers(weapon, players):
    """
    :param weapon: all players with that weapon should be deleted
    :type weapon: str

    :param players: dictionary of all players and theit weapons
    :type players: dict

    :return: update dictionaty of players
    :rtype: dict
    """

    global losers
    for player in players:
        if players[player] == weapon:
            losers.append(player)

    players = {key : val for key,val in players.items() if val != weapon}

    return players



def update_move(user_weapon):
    """
    :param user_weapon: choosen user weapon
    :type user_weapon: str

    :return: None
    "rtype: None    
    """

    global user_lost
    global bots
    global player_name

    if user_lost == False:
        bots[player_name] = user_weapon

    print("Weapons on the move")
    for bot in bots.items():
        print(bot)
    print("\n")

    rock_picked = "rock" in bots.values()
    scissors_picked = "scissors" in bots.values()
    paper_picked = "paper" in bots.values()

    if rock_picked and scissors_picked and paper_picked:
        return
    elif rock_picked and scissors_picked:
        bots = delete_loosers("scissors", bots)
        if user_weapon == "scissors":
            user_lost = True
    elif scissors_picked and paper_picked:
        bots = delete_loosers("paper", bots)
        if user_weapon == "paper":
            user_lost = True
    elif rock_picked and paper_picked:
        bots = delete_loosers("rock", bots)
        if user_weapon == "rock":
            user_lost = True

    if user_lost == False:
        bots.pop(player_name)
    

def print_result():
    """
    :description: print winner and list of losers
    """

    global bots
    global losers
    global user_lost
    global player_name

    if user_lost == False:
        bots[player_name] = ""

    print("Winner is:", next(iter(bots)))
    losers.reverse()
    print("\nLoosers:")
    for i in range(len(losers)):
        print(str(i + 1) + ".", losers[i])



player_name = input("Enter your name \n")

finish = ""
while finish != "n":
    
    bots = {}
    losers = []
    user_lost = False
    
    bots_amount = int(input("Set number of bots \n"))

    bots = generate_bots(bots_amount)

    while len(losers) < bots_amount:
        user_input = read_user_input()
        generate_bots_input()
        update_move(user_input)

    print_result()

    finish = input("\n Do you want to play again ? [y/n] \n")

