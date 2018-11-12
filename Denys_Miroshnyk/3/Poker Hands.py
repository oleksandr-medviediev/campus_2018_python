from collections import Counter

ranks = dict({
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
})


def check_for_three(hand):
    """checks if hand has three same cards

    Arguments:
        hand {str} -- a hand

    Returns:
        bool -- True if hand has three same cards
    """

    cards = hand.split(" ")
    for i in range(len(cards)):
        cards[i] = cards[i][:-1]
    c = Counter(cards).most_common(1)[0][1]

    is_three = c == 3
    return is_three


def check_for_pair(hand):
    """checks if hand has two same cards

    Arguments:
        hand {str} -- a hand

    Returns:
        bool -- True if hand has two same cards
    """
    cards = hand.split(" ")
    for i in range(len(cards)):
        cards[i] = cards[i][:-1]
    c = Counter(cards).most_common(1)[0][1]

    is_two = c == 2
    return is_two


def check_for_flush(hand):
    """checks if hand has flush

    Arguments:
        hand {str} -- a hand

    Returns:
        bool -- True if hand has flush
    """
    cards = hand.split(" ")
    for i in range(len(cards)):
        cards[i] = cards[i][-1]
    c = Counter(cards).most_common(1)[0][1]

    is_flush = c == 5
    return is_flush


def check_for_straight(hand):
    """checks if hand has straight

    Arguments:
        hand {str} -- a hand

    Returns:
        bool -- True if hand has straight
    """
    cards = hand.split(" ")
    for i in range(len(cards)):
        if cards[i][0].isdigit():
            cards[i] = int(cards[i][:-1])
        else:
            cards[i] = ranks.get(cards[i][:-1])
    cards.sort()

    is_straight = True
    for i in range(len(cards))[1:]:
        if cards[i] != cards[i-1] + 1:
            is_straight = False
    return is_straight


def check_for_straight_flush(hand):
    """checks if hand has straight and flush

    Arguments:
        hand {str} -- a hand

    Returns:
        bool -- True if hand has straight and flush
    """
    is_straight_flush = check_for_straight(hand) and check_for_flush(hand)
    return is_straight_flush


def check_for_four(hand):
    """checks if hand has four same cards

    Arguments:
        hand {str} -- a hand

    Returns:
        bool -- True if hand has four same cards
    """
    cards = hand.split(" ")
    for i in range(len(cards)):
        cards[i] = cards[i][:-1]
    c = Counter(cards).most_common(1)[0][1]

    is_four = c == 4
    return is_four


def check_for_full_house(hand):
    """checks if hand has full house

    Arguments:
        hand {str} -- a hand

    Returns:
        bool -- True if hand has full house
    """
    cards = hand.split(" ")
    for i in range(len(cards)):
        cards[i] = cards[i][:-1]
    c = Counter(cards).most_common(2)

    is_full_house = c[0][1] == 3 and c[1][1] == 2
    return is_full_house


def get_highest_rank_hands(hands):
    """from list of hands gets hands with highest card in it
    (may be many of them)
    
    Arguments:
        hands {list} -- hands
    
    Returns:
        dict_keys -- hands with highest card in it
    """

    hands_and_highest = dict()

    for j in hands:
        cards = j.split(" ")
        for i in range(len(cards)):
            if cards[i][0].isdigit():
                cards[i] = int(cards[i][:-1])
            else:
                cards[i] = ranks.get(cards[i][:-1])

        cards.sort()
        hands_and_highest[j] = max(cards)
    max_rank = max(hands_and_highest.values())

    new_dict = {key: val for key, val in hands_and_highest.items()
                if val == max_rank}
    return new_dict.keys()


def pick_best_poker_hands(hands):
    """finds the best hands
    
    Arguments:
        hands {list} -- hands
    
    Returns:
        dict_keys -- best hands
    """


    best_hands = list(filter(check_for_straight_flush, hands))
    if len(best_hands):
        return get_highest_rank_hands(best_hands)

    best_hands = list(filter(check_for_four, hands))
    if len(best_hands):
        return get_highest_rank_hands(best_hands)

    best_hands = list(filter(check_for_full_house, hands))
    if len(best_hands):
        return get_highest_rank_hands(best_hands)

    best_hands = list(filter(check_for_flush, hands))
    if len(best_hands):
        return get_highest_rank_hands(best_hands)

    best_hands = list(filter(check_for_straight, hands))
    if len(best_hands):
        return get_highest_rank_hands(best_hands)

    best_hands = list(filter(check_for_three, hands))
    if len(best_hands):
        return get_highest_rank_hands(best_hands)

    best_hands = list(filter(check_for_pair, hands))
    if len(best_hands):
        return get_highest_rank_hands(best_hands)

    return get_highest_rank_hands(hands)


hands = [
    "4D 5S 6S 8D 3C",
    "2S 4C 7S 9H 10H",
    "3S 4S 5D 6H JH"
]
print(pick_best_poker_hands(hands))
# ["3S 4S 5D 6H JH"]

hands = [
    "4D 5S 6S 8D 3C",
    "2S 4C 7S 9H 10H",
    "3S 4S 5D 6H JH",
    "3H 4H 5C 6C JD"]

print(pick_best_poker_hands(hands))
# ["3S 4S 5D 6H JH",
# "3H 4H 5C 6C JD"]

hands = ["10D QS 6S 8D 3C",  # high
         "2S 4C 7S 10S 10H",  # pair
         "3S 3D 3C 9H 9S",  # full house
         "10S JS QS KS AS"]  # royal flush

print(pick_best_poker_hands(hands))
