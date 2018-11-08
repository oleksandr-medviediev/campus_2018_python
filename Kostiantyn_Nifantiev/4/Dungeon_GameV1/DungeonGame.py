from game_functions import game_loop

while True:

    game_loop()
    decision = input('Do you want to play again? y/n:\n')
    if decision == 'y':

        continue

    else:

        break
