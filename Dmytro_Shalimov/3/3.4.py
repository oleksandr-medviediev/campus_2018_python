from collections import Counter


RANKS = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6,
         '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}

POINTS_MODIFIER_PER_COMBINATIONS = {"Straight flush" : 100000000, "Four of a kind" : 10000000,
                                    "Full house" : 1000000, "Flush" : 100000, "Straight" : 10000,
                                    "Three of a kind" : 1000, "Two pair" : 100, "One pair" : 10,
                                    "High card" : 1}


is_least_straight = False

hands_and_score = {}


def hands_input():
    """
    Prompts user to enter poker hands to compare. Ends on empty input

    :return: dict of hands and empty score
    :rtype: dict
    """
    
    hands = []
    user_input = input("Enter hand to compare(use empty input to proceed): ")

    while len(user_input) > 0:

        hands.append(user_input)
        user_input = input("Enter hand to compare(use empty input to proceed): ")

    hands_and_score = {key : None for key in hands}
    
    return hands_and_score


def split_hand(hand):
    """
    Splits given hand on ranks and suits

    :param str hand: current poker hand in string of correct format
    :return: ranks and suits
    :rtype: tuple
    """

    current_cards = hand.split()
    current_cards = [(RANKS[card[:len(card) - 1]], card[-1]) for card in current_cards]
    
    return zip(*current_cards)


def check_flush(suits):
    """
    Checks given suits list on 'Flush' combination

    :param list suits: list of suits
    :return: True if Flush, False otherwise
    :rtype: bool
    """

    return suits.count(suits[0]) == len(suits)


def check_straight(ranks):
    """
    Checks given ranks list on 'Straight' combination

    :param list ranks: list of ranks
    :return: True is Straight, False otherwise
    :rtype: bool
    """

    least_straight = [14, 5, 4, 3, 2]
    is_straight = True

    if ranks == least_straight:

        global is_least_straight
        is_least_straight = True

        return is_straight

    
    for x in range(len(ranks) - 1):

        if ranks[x] - ranks[x + 1] != 1:

            is_straight = False
            break

    return is_straight


def check_and_process_straight_flush(current_hand, suits, ranks):
    """
    Checks for 'Straight' and 'Flush' combinations,
     if they are present - writes score to appropriate hand and returns True, otherwise - returns False

    :param str current_hand: current hand
    :param list suits: list of suits
    :param list ranks: list of ranks
    :return: False if not 'Straight' and 'Flush', True otherwise
    :rtype: bool
    """    

    is_flush = check_flush(suits)
    is_straight = check_straight(ranks)

    is_flush_or_straight = False

    if is_flush or is_straight:

        is_flush_or_straight = True
        if is_flush and is_straight:

            if is_least_straight:
                hands_and_score[current_hand] = POINTS_MODIFIER_PER_COMBINATIONS["Straight flush"] * RANKS['5']

            else:
                hands_and_score[current_hand] = POINTS_MODIFIER_PER_COMBINATIONS["Straight flush"] * ranks[0]

        elif is_flush:
            hands_and_score[current_hand] = POINTS_MODIFIER_PER_COMBINATIONS["Flush"] * ranks[0]

        else:

            if is_least_straight:
                hands_and_score[current_hand] = POINTS_MODIFIER_PER_COMBINATIONS["Straight"] * RANKS['5']

            else:
                hands_and_score[current_hand] = POINTS_MODIFIER_PER_COMBINATIONS["Straight"] * ranks[0]

    return is_flush_or_straight


def check_and_process_is_four_of_a_kind(current_hand, ranks):
    """
    Checks for 'Four of a kind' combination,
     if present - writes score to appropriate hand and returns True, otherwise - returns False

    :param str current_hand: current hand
    :param list ranks: list of current ranks
    :return: True is 'Four of a kind', False otherwise
    :rtype: bool 
    """
    
    count_ranks = Counter(ranks)
    count_ranks = count_ranks.most_common(1)

    is_four_of_a_kind = False
    
    if count_ranks[0][1] == 4:

        is_four_of_a_kind = True
        hands_and_score[current_hand] = POINTS_MODIFIER_PER_COMBINATIONS["Four of a kind"] * count_ranks[0][0]

    return is_four_of_a_kind


def check_and_process_full_house_or_three_of_a_kind(current_hand, ranks):
    """
    Checks for 'Full House' and 'Three of a kind' combinations,
     if they are present - writes score to appropriate hand and returns True, otherwise - returns False

    :param str current_hand: current hand
    :param list ranks: list of ranks
    :return: False if not 'Full House' or 'Three of a kind', True otherwise
    :rtype: bool
    """

    count_ranks = Counter(ranks)
    count_ranks = count_ranks.most_common(2)

    is_full_house_or_three_of_a_kind = False

    if count_ranks[0][1] == 3 and count_ranks[1][1] == 2:

        is_full_house_or_three_of_a_kind = True
        hands_and_score[current_hand] = POINTS_MODIFIER_PER_COMBINATIONS["Full house"] * count_ranks[0][0]

    elif count_ranks[0][1] == 3:

        is_full_house_or_three_of_a_kind = True
        hands_and_score[current_hand] = POINTS_MODIFIER_PER_COMBINATIONS["Three of a kind"] * count_ranks[0][0]


    return is_full_house_or_three_of_a_kind


def check_and_process_one_or_two_pairs(current_hand, ranks):
    """
    Checks for 'One pair' and 'Two pairs' combinations,
     if they are present - writes score to appropriate hand and returns True, otherwise - returns False

    :param str current_hand: current hand
    :param list ranks: list of ranks
    :return: False if not 'One pair' or 'Two pairs', True otherwise
    :rtype: bool
    """

    count_ranks = Counter(ranks)
    count_ranks = count_ranks.most_common(2)

    is_one_or_two_pairs = False

    if count_ranks[0][1] == 2 and count_ranks[1][1] == 2:

        is_one_or_two_pairs = True
        hands_and_score[current_hand] = (POINTS_MODIFIER_PER_COMBINATIONS["Two pair"] *
                                         max(count_ranks[0][0], count_ranks[1][0]))

    elif count_ranks[0][1] == 2:

        is_one_or_two_pairs = True
        hands_and_score[current_hand] = POINTS_MODIFIER_PER_COMBINATIONS["One pair"] * count_ranks[0][0]

    return is_one_or_two_pairs


def process_hand(current_hand):
    """
    Processes given hand

    :param str current_hand: current hand
    """

    ranks, suits = split_hand(current_hand)
    ranks = list(ranks)
    suits = list(suits)

    ranks.sort(reverse = True)

    (check_and_process_straight_flush(current_hand, suits, ranks) or
    check_and_process_is_four_of_a_kind(current_hand, ranks) or
    check_and_process_full_house_or_three_of_a_kind(current_hand, ranks) or
    check_and_process_one_or_two_pairs(current_hand, ranks))

    hands_and_score[current_hand] = POINTS_MODIFIER_PER_COMBINATIONS["High card"] * ranks[0]


hands_and_score = hands_input()

for hand in hands_and_score:
    process_hand(hand)

max_rank = max(list(hands_and_score.values()))
winners = [hands for hands, score in hands_and_score.items() if score == max_rank]

print(winners)
