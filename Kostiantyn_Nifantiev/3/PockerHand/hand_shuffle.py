from random import shuffle


suits = ['S', 'H', 'C', 'D']
card_values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

pocker_deque = []

for suit in suits:

    pocker_deque += [''.join([value, suit]) for value in card_values]


def get_suffled_hands(how_many):
    """
    This function intended to be used for test-case generation
    """
    shuffle(pocker_deque)
    
    hands = [' '.join(pocker_deque[x : x + 5]) for x in range(0, how_many * 5, 5)]

    return hands

