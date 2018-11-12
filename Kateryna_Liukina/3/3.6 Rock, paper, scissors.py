from random import choice
from random import shuffle


def beat(weapons_names, weapon1, weapon2):
    """
    Function decide which weapon win
    Args:
        weapons_names(dict(str, int)): return index of weapon
        weapon1(str): string with name of weapon
        weapon2(str): string with name of weapon
    Returns:
        bool: true if firth weapon beat second
    """
    return weapons_names[weapon1] - weapons_names[weapon2] % 3 == 2


def print_weapons(player_lose, bots, number_of_not_empty_weapons, player_weapon, index_of_lose):
    """
    Function prints weapons for current round of game
    Args:
        number_of_not_empty_weapons(list(list)): name of weapon and number of bots with this weapon
        player_weapon(str): player weapon
        player_lose(bool): true if player lost
        index_of_lose(int): index of weapon that lose
    Returns:
        none
    """
    if not player_lose:
        print("You: " + player_weapon)

    i = 0

    index = (index_of_lose + 1) % 2
    for j in range(number_of_not_empty_weapons[index][1]):
        print("Bot " + str(bots[i]) + ": " + number_of_not_empty_weapons[index][0])
        i += 1

    for j in range(number_of_not_empty_weapons[index_of_lose][1]):

        print("Bot " + str(bots[i]) + ": " + number_of_not_empty_weapons[index_of_lose][0])
        i += 1


def print_leader_board(leader_board):
    """
    Function prints leaderboard
    Args:
        leader_board(list): list of players
    Returns:
        none
    """
    i = 1
    print("\nLeader board:")
    for element in leader_board:
        if element == "you":
            print(str(i) + ". You")
        else:
            print(str(i) + ". Bot " + str(element))
        i += 1



def play_game():
    """
    Function launch the Rock, paper, scissors - game
    Returns:
        none
    """
    continue_game = 'y'
    while continue_game == 'y':

        number_of_players = int(input("Number of players:"))
        weapons_names = {"rock": 0, "paper": 1, "scissors": 2}
        number_of_bot = number_of_players - 1
        bots = list(range(1, number_of_bot + 1))
        leader_board = bots.copy()

        number_of_weapons = {}
        player_lose = False
        while number_of_players > 1:

            separaters_for_numbers = [choice(range(number_of_bot + 1)) for i in range(2)]
            separaters_for_numbers.sort()

            number_of_weapons["rock"] = separaters_for_numbers[0]
            number_of_weapons["paper"] = separaters_for_numbers[1] - separaters_for_numbers[0]
            number_of_weapons["scissors"] = number_of_bot - number_of_weapons["rock"] - number_of_weapons["paper"]

            if not player_lose:

                player_weapon = input("Your weapon:")
                number_of_weapons[player_weapon] += 1

            number_of_not_empty_weapons = [[name, number] for name, number in number_of_weapons.items() if number]

            if len(number_of_not_empty_weapons) != 2:
                print("Tie!")
                continue

            index_of_lose = int(beat(weapons_names, number_of_not_empty_weapons[1][0], number_of_not_empty_weapons[0][0]))

            number_of_players -= number_of_not_empty_weapons[index_of_lose][1]

            if player_weapon == number_of_not_empty_weapons[0][0]:
                number_of_not_empty_weapons[0][1] -= 1

            if player_weapon == number_of_not_empty_weapons[1][0]:
                number_of_not_empty_weapons[1][1] -= 1

            print_weapons(player_lose, bots, number_of_not_empty_weapons, player_weapon, index_of_lose)

            if player_weapon == number_of_not_empty_weapons[index_of_lose][0]:
                player_lose = True

            number_of_bot = number_of_players - 1 * (not player_lose)

            bots = bots[:number_of_bot]
            leader_board = bots + leader_board[number_of_bot:]
            if player_weapon == number_of_not_empty_weapons[index_of_lose][0]:
                leader_board.insert(number_of_bot, "you")
            shuffle(bots)
        if not player_lose:
            print("\nYou won!")
            leader_board.insert(0, "you")
        print_leader_board(leader_board)
        continue_game = input('Continue? (y/n)')

		
play_game()		
