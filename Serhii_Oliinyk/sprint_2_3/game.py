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

    while True:
        value = int(input("enter value from [0-2], 0- rock, 1-paper, 2-scissors"))
        if (value < 0) and (value > 2):
            continue

        combinations_list = {}
        for i in range(players_number):
            combinations_list.setdefault(i, -1)

        combinations_list[0] = value
        print("You: ", combination[value])

        for i in range(1, players_number, 1):
            value = choice(keys)
            combinations_list[i] = value
            print("Bot", i, ": ", combination[value])

        result = []
        if (0 in combinations_list) and (1 in combinations_list) and (2 in combinations_list):
            continue
        elif (0 in combinations_list.values()) and (1 in combinations_list.values()):
            result = [k for k, v in combinations_list.items() if v == 1]
        elif (0 in combinations_list.values()) and (2 in combinations_list.values()):
            result = [k for k, v in combinations_list.items() if v == 0]
        elif (1 in combinations_list.values()) and (2 in combinations_list.values()):
            result = [k for k, v in combinations_list.items() if v == 2]
        else:
            continue

        print("Leaderboard:")
        for i in result:
            value =  combinations_list[i]
            if i == 0:
                print("You: ", combination[value])
            else:
                print("Bot", i, ": ", combination[value])

        for k, v in combinations_list.items():
            if k in result:
                continue
            if k == 0:
                print("You: ", combination[v])
            else:
                print("Bot", i, ": ", combination[v])

        check = int(input("Press 1 to continue -1 to exit"))

        if(check == -1):
            break



if __name__ == '__main__':
    players_number = 0

    while True:
        players_number = int(input("Choose number of player"))

        if (players_number >= 2) and (players_number <= 5):
            break

    game(players_number)


