import GameUtils


def game_loop():

    number_of_players =  GameUtils.get_number_of_players()
    weapons_list = ["rock", "paper", "scissors"]
    participants_score = [['Player', 0]]
    participants_score += [['Bot#' + str(index), 0] for index in range(1, number_of_players)]

    while True:

        current_weapons = [GameUtils.get_player_weapon(weapons_list)]
        current_weapons += [GameUtils.bot_generator(weapons_list) for x in range(1, number_of_players)]

        for record, weapon in zip(participants_score, current_weapons):

            print(''.join([record[0],': ', weapon]))

        weapons_count = zip(weapons_list, map(current_weapons.count, weapons_list))
        weapons_count = dict(weapons_count)


        def winner_check(win_weapon, antagonist_weapon):

            if weapons_count[win_weapon] == 1 and weapons_count[antagonist_weapon] == 0:

                winner_index = current_weapons.index(win_weapon)
                participants_score[winner_index][1] += 1
                print(participants_score[winner_index][0] + " is winner!\n")

                for record in participants_score:

                    print(record[0] + ': ' + str(record[1]))

                return True
            
            else:

                return False

        if winner_check("rock", "paper") or winner_check("paper", "scissors") or winner_check("scissors", "rock"): 
        
            pass
        
        else:

            continue

        if input('Do you want to play again?\ny/n?') == 'y':

            continue

        else:

            break
