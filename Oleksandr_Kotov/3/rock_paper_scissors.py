from random import choice



def is_confusion(choices):
    """function defines if more
    than 2 types of weapon is chosen
    and confuse happened"""

    return len(set(choices)) > 2

def beats(weapon1, weapon2):
    """function defines if weapon1 beats weapon2"""

    return (weapon1 == "scissors" and weapon2 == "paper" or
            weapon1 == "paper" and weapon2 == "rock" or
            weapon1 == "rock" and weapon2 == "scissors")



WEAPONS = ["scissors", "rock", "paper"]

while True:

    num_of_players = int(input("Number of players: "))

    choices = {}
    choices["You"] = input("Your weapon: ")
    choices.update({"Bot " + str(i) : choice(weapons) for i in range(1, num_of_players)})

    for player, choice in choices.items():
        print(player + " : " + choice)


    if is_confusion(choices.items()):
        """"""

    else:

        for player, choice in choices.items():
            