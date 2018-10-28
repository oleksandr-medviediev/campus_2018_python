from random import randint

options = ["Rock", "Paper", "Scissors"]

bots_amount = int(input("bots num: "))

if bots_amount < 2:
    bots_amount = 2
elif bots_amount > 5:
    bots_amount = 5


def step(bots_amount):
    """
    Rock-paper-scissors game step
    Args:
        bots_amount (int): bots amount
    Return:
        None.
    """
    computers = []
    for i in range(0, bots_amount):
        computers.append(options[randint(0, 2)])

    player = ""

    enable_cheat = bool(input("Enable cheats?True/nothing+Enter\n"))
    if enable_cheat:
        print(computers)

    player = input("Rock, Paper, Scissors?")
    if computers.count("Paper") > 0 and computers.count("Scissors") > 0 and computers.count("Rock") > 0:
        print("Everyone loses!")
        return None
    elif player == "Rock":
        if computers.count("Paper") > 0:
            print("You lose!", "Paper", "covers", player)
            return None
        else:
            print("You win!", player, "smashes everything else!")
    elif player == "Paper":
        if computers.count("Scissors") > 0:
            print("You lose!", "Scissors", "cut", player)
            return None
        else:
            print("You win!", player, "covers everythin else!")
    elif player == "Scissors":
        if computers.count("Rock") > 0:
            print("You lose...", "Rock", "smashes", player)
            return None
        else:
            print("You win!", player, "cuts everything else!")
    elif player == "E":
        return None
    else:
        print("That's not a valid play. Check your spelling!")
        return None

    if not enable_cheat:
        print(computers)
    if computers.count(player) > 0:
        step(computers.count(player))

play_flag = True

while play_flag:
    step(bots_amount)
    play_flag = bool(input("Play?True/nothing+Enter\n"))
