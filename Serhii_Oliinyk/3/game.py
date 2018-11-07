from random import choice


def game(players_number):
    """Function inplement game logic.

    Args:
        players_number: type int.

    Returns:
        Return None.

    """

    combination = {
        0: "rock",
        1: "paper",
        2: "scissors"
    }

    keys = [0, 1, 2]
    players = [i for i in range(0, players_number)]
    combinations_list = {}
    
    while True:
        for i in players:
            combinations_list.setdefault(i, -1)

        if 0 in players:
            value = int(input("enter value from [0-2], 0- rock, 1-paper, 2-scissors"))
            if (value < 0) and (value > 2):
                continue

        for i in players:
            if i == 0:
                combinations_list[i] = value
                print("You: ", combination[value])
                continue
            
            value = choice(keys)
            combinations_list[i] = value
            print("Bot", i, ": ", combination[value])

        winers = []
        losers = []
        
        if (0 in combinations_list.values()) and (1 in combinations_list.values()) and (2 in combinations_list.values()):
            continue
        elif (0 in combinations_list.values()) and (1 in combinations_list.values()):
            winers = [k for k, v in combinations_list.items() if v == 1]
            losers = [k for k, v in combinations_list.items() if v == 0]
        elif (0 in combinations_list.values()) and (2 in combinations_list.values()):
            winers = [k for k, v in combinations_list.items() if v == 0]
            losers = [k for k, v in combinations_list.items() if v == 2]
        elif (1 in combinations_list.values()) and (2 in combinations_list.values()):
            winers = [k for k, v in combinations_list.items() if v == 2]
            losers = [k for k, v in combinations_list.items() if v == 1]
        else:
            continue
        
        for i in losers:
            players.remove(i)

        if len(winers) > 1:
            continue

        print("Leaderboard:")
        value =  combinations_list[winers[0]]
        if winers[0] == 0:
            print("You: ", combination[value])
        else:
            print("Bot", winers[0], ": ", combination[value])

        for k, v in combinations_list.items():
            if k in winers:
                continue
            if k == 0:
                print("You: ", combination[v])
            else:
                print("Bot", i, ": ", combination[v])

        check = int(input("Press 1 to continue -1 to exit"))

        if check == -1:
            break
        else:
            players = [i for i in range(0, players_number)]
            combinations_list.clear()


if __name__ == '__main__':
    players_number = 0

    while True:
        players_number = int(input("Choose number of player [2 - 5]"))

        if (players_number >= 2) and (players_number <= 5):
            break

    game(players_number)
