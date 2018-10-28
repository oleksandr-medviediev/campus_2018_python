suits = ("H", "D", "C", "S")

cards = ("2", "3", "4", "5", "6", "7", "8", "9", "10",
         "J", "Q", "K", "A")

categories = ("Straight Flush", "Four of a kind",
              "Full house", "Flush",
              "Straight", "Three of a kind",
              "Two pair", "One Pair",
              "High card")


def is_flush(hand):
    """
    Check is flush in hand

    :param hand: string hand with cards
    :hand type: str.
    :returns: bool result of check
    :rtype: bool.
    """
    result = False

    for s in suits:

        if hand.count(s) == 5:
            
            result = True
            break

    return result


def is_straight(hand):
    """
    Check is straight in hand

    :param hand: string hand with cards
    :hand type: str.
    :returns: bool result of check
    :rtype: bool.
    """

    card_in_row = 0
    result = False

    for c in cards:

        if c in hand:

            card_in_row += 1

            if card_in_row == 5:

                result = True
                break

            continue
        
        card_in_row = 0      
    
    return result


def is_straight_flush(hand):
    """
    Check is straight flush in hand

    :param hand: string hand with cards
    :hand type: str.
    :returns: bool result of check
    :rtype: bool.
    """

    result = True

    if not is_flush(hand):

        result = False
    
    if not is_straight(hand):

        result = False
    
    return result


def is_same_cards_in_hand(hand, count_of_cards):
    """
    Check is some count of cards in hand

    :param hand: string hand with cards
    :param count_of_cards: count of card that mast be same
    :hand type: str.
    :count_of_cards: int.
    :returns: bool result of check
    :rtype: bool.
    """

    result = False

    for c in cards:

        if hand.count(c) == count_of_cards:

            result = True

    return result    


def is_full_house(hand):
    """
    Check is full house in hand

    :param hand: string hand with cards
    :hand type: str.
    :returns: bool result of check
    :rtype: bool.
    """

    return is_same_cards_in_hand(hand, 2) and is_same_cards_in_hand(hand, 3)


def is_four_of_a_kind(hand):
    """
    Check is flush in hand

    :param hand: string hand with cards
    :hand type: str.
    :returns: bool result of check
    :rtype: bool.
    """

    return is_same_cards_in_hand(hand, 4)


def is_three_of_kind(hand):
    """
    Check is three of kind in hand

    :param hand: string hand with cards
    :hand type: str.
    :returns: bool result of check
    :rtype: bool.
    """

    return is_same_cards_in_hand(hand, 3)


def is_two_pair(hand):
    """
    Check is two pair in hand

    :param hand: string hand with cards
    :hand type: str.
    :returns: bool result of check
    :rtype: bool.
    """

    pair_count = 0

    for c in cards:

        if hand.count(c) == 2:

            pair_count += 1

    return pair_count == 2    


def is_one_pair(hand):
    """
    Check is pair in hand

    :param hand: string hand with cards
    :hand type: str.
    :returns: bool result of check
    :rtype: bool.
    """

    return is_same_cards_in_hand(hand, 2)


def get_rank_of_hand(hand):
    """
    Checks hand and returns it rank

    :param hand: string hand with cards
    :hand type: str.
    :returns: int score of hand
    :rtype: int.
    """

    result = len(categories)

    if is_straight_flush(hand):
        result = 0
    
    elif is_four_of_a_kind(hand):
        result = 1

    elif is_full_house(hand):
        result = 2

    elif is_flush(hand):
        result = 3

    elif is_straight(hand):
        result = 4

    elif is_three_of_kind(hand):
        result = 5
    
    elif is_two_pair(hand):
        result = 6

    elif is_one_pair(hand):
        result = 7

    else:
        result = 8

    return result


def pick_best_poker_hands(list_of_hands):
    """
    Take list of hands with cards and pick the best

    :param list_of_hands: list of strings with hand of cards
    :list_of_hands: list of strings.
    :returns: string best hand
    :rtype: str.
    """

    best_hand_index = 0
    best_hand_score = len(categories)

    for i in range(len(list_of_hands)):

        if(best_hand_score > get_rank_of_hand(list_of_hands[i])):

            best_hand_index = i

    return list_of_hands[best_hand_index]


hands = ["4D 5S 6S 8D 3C",
         "2S 4C 7S 9H 10H",
         "3S 4S 5D 6H JH",
         "3H 4H 5C 6C JD"]

print(pick_best_poker_hands(hands))
