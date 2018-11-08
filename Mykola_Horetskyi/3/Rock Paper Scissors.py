import random


def playRockPaperScissors():
    """
    Simulation of rock, paper, scissors game.
    When prompted, enter string starting with 'r' or 'rock' to play rock,
    starting with 'p' to play paper,
    starting with 's' to play scissors
    """

    weapons = {"r":"s", "p":"r", "s":"p"}
    
    is_game_in_progress = True

    
    print("Enter number of players:")
    number_of_players = input()

    while not number_of_players.isdigit() or int(number_of_players) < 2:
        print("Input incorrect, it should be integer greater than 1.\nEnter number of players again:")
        number_of_players = input()

    while is_game_in_progress:
    
        print("Choose your weapon:")
        player_weapon = input()

        while not player_weapon or player_weapon[0].lower() not in weapons.keys():
            print("Input incorrect, it start with 'r', 'p' or 's'.\n Enter weapon of ypur choosing again:")
            player_weapon = input()

        playeble_weapons = [player_weapon[0].lower()]
        playeble_weapons.extend([list(weapons.keys())[random.randint(0, len(weapons) - 1)]
                                    for i in range(len(weapons))])

        def is_winner(weapon):
            result = all([weapon != weapons[playeble_weapon] for playeble_weapon in playeble_weapons])
            return result

        winner_indexes = [i for i in range(len(playeble_weapons)) if is_winner(playeble_weapons[i])]

        if not winner_indexes:
            print("Draw")
        else:
            print("Winners:")
            for index in winner_indexes:
                if (index == 0):
                    print("Player")
                else:
                    print("Bot{}".format(index))

        print("Would you like to play again:")
        answer = input()

        if not answer or answer[0].lower() != "y":
            is_game_in_progress = False
        
    return
