FACE_CARDS = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
SUITS = ['C', 'D', 'H', 'S']
INDICES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
INDEX, SUIT = 0, 1


def card_to_number(card):
    '''
    Return a numeric equivalent of a card
    :param card: a poker card;
    :return: a numeric representation of a card;
    :type card: str;
    :rtype: int
    '''
    if card[INDEX].isnumeric():
        result = int(card[INDEX])
    else:
        result = FACE_CARDS[card[INDEX]]
    return result


def is_straight_flush(hand):
    '''
    Function checks if hand contains the 'straight flush' poker combination
    :param hand: a poker hand;
    :return: True if contains, False otherwise;
    :type hand: a list of strings where each strihg is a poker card code name;
    :rtype: bool.
    '''
    return is_flush(hand) and is_straight(hand)


def is_four_of_kind(hand):
    '''
    Function checks if hand contains the 'four kind' poker combination
    :param hand: a poker hand;
    :return: True if contains, False otherwise;
    :type hand: a list of strings where each strihg is a poker card code name;
    :rtype: bool.
    '''
    result = False
    for index in INDICES:
        number = sum(index == card[INDEX] for card in hand)
        if number == 4:
            result = True

    return result


def is_full_house(hand):
    '''
    Function checks if hand contains the 'full house' poker combination
    :param hand: a poker hand;
    :return: True if contains, False otherwise;
    :type hand: a list of strings where each strihg is a poker card code name;
    :rtype: bool.
    '''
    only_indices = [card[INDEX] for card in hand]
    unique_indices = set(only_indices)
    
    if len(unique_indices) != 2:
        result = False
    else:
        index_one, index_two = unique_indices
        result = only_indices.count(index_one) == 3 and only_indices.count(index_two) == 2 or\
            only_indices.count(index_one) == 2 and only_indices.count(index_two) == 3

    return result


def is_flush(hand):
    '''
    Function checks if hand contains the 'flush' poker combination
    :param hand: a poker hand;
    :return: True if contains, False otherwise;
    :type hand: a list of strings where each strihg is a poker card code name;
    :rtype: bool.
    '''
    flush_suit = hand[0][SUIT]
    result = all(flush_suit == card[SUIT] for card in hand)
    return result


def is_straight(hand):
    '''
    Function checks if hand contains the 'straight' poker combination
    :param hand: a poker hand;
    :return: True if contains, False otherwise;
    :type hand: a list of strings where each strihg is a poker card code name;
    :rtype: bool.
    '''
    numeric_card_view = list(map(card_to_number, hand))
    numeric_card_view.sort()
    result = numeric_card_view == list(range(numeric_card_view[0], numeric_card_view[0] + len(numeric_card_view)))
    return result


def is_three_of_kind(hand):
    '''
    Function checks if hand contains the 'three of kind' poker combination
    :param hand: a poker hand;
    :return: True if contains, False otherwise;
    :type hand: a list of strings where each strihg is a poker card code name;
    :rtype: bool.
    '''
    only_indices = [card[INDEX] for card in hand]
    unique_indices = set(only_indices)
    result = any(only_indices.count(unique_index) == 3 for unique_index in unique_indices)
    return result


def is_two_pairs(hand):
    '''
    Function checks if hand contains the 'two pairs' poker combination
    :param hand: a poker hand;
    :return: True if contains, False otherwise;
    :type hand: a list of strings where each strihg is a poker card code name;
    :rtype: bool.
    '''
    only_indices = [card[INDEX] for card in hand]
    unique_indices = set(only_indices)

    number_of_pairs = sum(only_indices.count(unique_index) == 2 for unique_index in unique_indices)
    return number_of_pairs == 2


def is_one_pair(hand):
    '''
    Function checks if hand contains the 'one pair' poker combination
    :param hand: a poker hand;
    :return: True if contains, False otherwise;
    :type hand: a list of strings where each strihg is a poker card code name;
    :rtype: bool.
    '''
    only_indices = [card[INDEX] for card in hand]
    unique_indices = set(only_indices)

    number_of_pairs = sum(only_indices.count(unique_index) == 2 for unique_index in unique_indices)
    return number_of_pairs == 1


def find_best_hands_with_high_card(hands):
    '''
    Finds the hands with the best (high) card
    :param hands: a poker hands;
    :return: the best ones according to the high card rule;
    :type hands: a list of str
    :rtype: a list of str
    '''
    best_hands = []

    best_card = 2
    best_hands = []
    for hand in hands:
        numeric_card_view = list(map(card_to_number, hand))
        for card in numeric_card_view:
            if card == best_card and hand not in best_hands:
                best_hands.append(hand)
            elif card > best_card:
                best_card = card
                best_hands.clear()
                best_hands.append(hand)
    
    return best_hands


def pick_best_poker_hands(hands):
    '''
    The function calculates which of given poker hands are the best and returns them
    :param hands: a poker hands;
    :return: the best of poker hands;
    :type hands: a list of strings with poker hands. Example: ["4D 5S 6S 8D 3C", "2S 4C 7S 9H 10H"];
    :rtype: a list of strings.
    '''
    for i in range(len(hands)):
        hands[i] = hands[i].split(' ')
    
    straight_flushes, fours_of_kind, full_houses, flushes, straights, threes_of_kind, two_pairs, one_pairs =\
        range(8)

    combinations_priority_queue = [[] for i in range(8)]
    
    for hand in hands:
        if is_straight_flush(hand):
            combinations_priority_queue[straight_flushes].append(hand)
        elif is_four_of_kind(hand):
            combinations_priority_queue[fours_of_kind].append(hand)
        elif is_full_house(hand):
            combinations_priority_queue[full_houses].append(hand)
        elif is_flush(hand):
            combinations_priority_queue[flushes].append(hand)
        elif is_straight(hand):
            combinations_priority_queue[straights].append(hand)
        elif is_three_of_kind(hand):
            combinations_priority_queue[threes_of_kind].append(hand)
        elif is_two_pairs(hand):
            combinations_priority_queue[two_pairs].append(hand)
        elif is_one_pair(hand):
            combinations_priority_queue[one_pairs].append(hand)

    for combo_hands in combinations_priority_queue:
        if len(combo_hands) > 0:
            return combo_hands
        
    return find_best_hands_with_high_card(hands)
