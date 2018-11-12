"""
This script solves task 3.4 from Coding Campus 2018 Python course
(Poker Hands)
"""

from collections import defaultdict

card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "T": 11, "J": 12, "Q": 13, "K": 14, "A": 15}


def check_straight_flush(hand):
    """
    Checks if given hand corresponds to straight flush hand
    :param hand: List of tuples containing card rank and suit
    :return: Tuple of bool and list, bool if hand is of type, list containing hand rank if is of type
    """

    if check_flush(hand) and check_straight(hand):
        return True, [9, int(card_order_dict[hand[0][0]])]
    else:
        return False, []


def check_four_of_a_kind(hand):
    """
    Checks if given hand corresponds to four of a kind hand
    :param hand: List of tuples containing card rank and suit
    :return: Tuple of bool and list, bool if hand is of type, list containing hand rank if is of type
    """

    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 4]:

        return_list = [8]
        for v, count in value_counts.items():

            if count == 4:

                return_list.append(int(card_order_dict[v]))
                values = [i for i in values if i != v]
                break

        for v in values:
            return_list.append(int(card_order_dict[v]))

        return True, return_list

    return False, []


def check_full_house(hand):
    """
    Checks if given hand corresponds to full house hand
    :param hand: List of tuples containing card rank and suit
    :return: Tuple of bool and list, bool if hand is of type, list containing hand rank if is of type
    """

    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [2, 3]:

        return_list = [7]
        for v, count in value_counts.items():

            if count == 3:

                return_list.append(int(card_order_dict[v]))
                values = [i for i in values if i != v]
                break

        return_list.append(int(card_order_dict[values[0]]))

        return True, return_list

    return False, []


def check_flush(hand):
    """
    Checks if given hand corresponds to flush hand
    :param hand: List of tuples containing card rank and suit
    :return: Tuple of bool and list, bool if hand is of type, list containing hand rank if is of type
    """

    suits = [i[1] for i in hand]
    if len(set(suits)) == 1:

        return_list = [6]
        return_list += [int(card_order_dict[i[0]]) for i in hand]

        return True, return_list

    else:
        return False, []


def check_straight(hand):
    """
    Checks if given hand corresponds to straight hand
    :param hand: List of tuples containing card rank and suit
    :return: Tuple of bool and list, bool if hand is of type, list containing hand rank if is of type
    """

    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range == 4):

        return_list = [5, int(card_order_dict[hand[0][0]])]
        return True, return_list

    else:
        # Check straight with low Ace
        if set(values) == {"A", "2", "3", "4", "5"}:

            return_list = [5, int(card_order_dict[hand[0][0]])]
            return True, return_list

        return False, []


def check_three_of_a_kind(hand):
    """
    Checks if given hand corresponds to three of a kind hand
    :param hand: List of tuples containing card rank and suit
    :return: Tuple of bool and list, bool if hand is of type, list containing hand rank if is of type
    """

    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if set(value_counts.values()) == {3, 1}:

        return_list = [4]
        for v, count in value_counts.items():

            if count == 3:

                return_list.append(int(card_order_dict[v]))
                values = [i for i in values if i != v]
                break

        for v in values:
            return_list.append(int(card_order_dict[v]))

        return True, return_list
    else:
        return False


def check_two_pairs(hand):
    """
    Checks if given hand corresponds to two pair hand
    :param hand: List of tuples containing card rank and suit
    :return: Tuple of bool and list, bool if hand is of type, list containing hand rank if is of type
    """

    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 2, 2]:

        return_list = [3]
        for v, count in value_counts.items():

            if count == 2:

                return_list.append(int(card_order_dict[v]))
                values = [i for i in values if i != v]

        for v in values:
            return_list.append(int(card_order_dict[v]))

        return True, return_list

    else:
        return False, []


def check_one_pairs(hand):
    """
    Checks if given hand corresponds to one pair hand
    :param hand: List of tuples containing card rank and suit
    :return: Tuple of bool and list, bool if hand is of type, list containing hand rank if is of type
    """

    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if 2 in value_counts.values():

        return_list = [2]
        for v, count in value_counts.items():

            if count == 2:

                return_list.append(int(card_order_dict[v]))
                values = [i for i in values if i != v]
                break

        for v in values:
            return_list.append(int(card_order_dict[v]))

        return True, return_list

    else:
        return False, []


def check_hand(hand):
    """
    Checks and returns hand rank score
    :param hand: Space-separated string containing five cards
    :return: List containing hand score, with first element being rank score and all others used to determine score inside rank
    """

    split_hand = hand.split()
    parsed_hand = [(card[:-1], card[-1:]) for card in split_hand]
    parsed_hand.sort(key=lambda tup: card_order_dict[tup[0]], reverse=True)

    check_functions = \
        [
            check_straight_flush,
            check_four_of_a_kind,
            check_full_house,
            check_flush,
            check_straight,
            check_three_of_a_kind,
            check_two_pairs,
            check_one_pairs
        ]

    return_score = None

    for check_function in check_functions:

        is_hand, score = check_function(parsed_hand)
        if is_hand:
            return_score = score
            break

    if return_score is None:
        return_score = [1, int(card_order_dict[parsed_hand[0][0]])]

    return return_score


def pick_best_hand(hand_list):
    """
    Selects best poker hand from list
    :param hand_list: List of 'hands': strings containing space-separated cards
    :return: List containing strings that represent best hands
    """

    best_hand_value = [0, 0]
    best_hand = []

    for hand in hand_list:

        hand_value = check_hand(hand)

        for index in range(len(hand_value)):

            if hand_value[index] > best_hand_value[index]:

                best_hand_value = hand_value
                best_hand = [hand]
                break

            elif hand_value[index] == best_hand_value[index]:

                if index == len(hand_value) - 1:
                    best_hand.append(hand)
                else:
                    continue

            else:
                break

    return best_hand
