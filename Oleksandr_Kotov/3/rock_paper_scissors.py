from random import choice


WEAPONS = ["scissors", "rock", "paper"]


def is_confusion(choices):
    """define if more than 2 types of
    weapon is chosen and confuse happened"""

    confusion = len(set(choices)) == 3 or len(set(choices)) == 1

    return confusion


answer = 'y'

while answer == 'y':

    num_of_players = int(input("Number of players: "))

    participants = ["You"]
    participants.extend(["Bot " + str(i) for i in range(1, num_of_players)])

    leaderboard = []

    while len(participants) > 1:

        choices = []

        if "You" in participants:
            choices.append(input("Your weapon: "))

        choices += [choice(WEAPONS) for i in range(1, len(participants))]

        if "You" in participants:

            for partcipant, weapon in zip(participants, choices):
                print(partcipant + " : " + weapon)

        if is_confusion(choices):

            if "You" in participants:
                print("Confusion!")

            continue

        else:

            new_participants = []

            dominant = ""

            if "scissors" in choices and "paper" in choices:
                dominant = "scissors"
            elif "paper" in choices and "rock" in choices:
                dominant = "paper"
            elif "rock" in choices and "scissors" in choices:
                dominant = "rock"

            for idx, weapon in enumerate(choices):

                if weapon == dominant:
                    new_participants.append(participants[idx])
                else:
                    leaderboard.insert(0, participants[idx])

            participants = new_participants

    if "You" in participants:
        print("You won!")
    else:
        print("You lose!")

    print("Leaders:\n")

    for position, participant in enumerate(leaderboard):
        print(F"{position + 1}. {participant}")

    answer = input("Play again? (y/n)\n")
