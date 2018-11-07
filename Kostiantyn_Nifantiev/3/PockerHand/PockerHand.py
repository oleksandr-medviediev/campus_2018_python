from hand_shuffle import get_suffled_hands
from pocker_hands_analyser import evaluate_hands, pick_winner_hands


while True:

    hands = get_suffled_hands(4)

    res = evaluate_hands(hands)
    print('Hands:')
    for hand in res:

        print(hand)

    winners = pick_winner_hands(res)

    print('\nWinner:')
    for hand in winners:

        print(hand)

    input('plress enter\n')

