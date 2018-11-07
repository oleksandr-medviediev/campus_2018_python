from collections import Counter


CARDS_IN_HAND = 5
LOWEST_RANK_ROYAL_FLASH = 10
alpha_ranks = {'J':11, 'Q':12, 'K':13, 'A':14}
suits = ['H', 'D', 'S', 'C']
high_card, one_pair, two_pairs, three_of_kind, straight, flush, full_house, four_of_kind, straight_flush, royal_flush = range(10)


def get_card_info(card):
    """
    parse card information in tuple(rank - int, char - suit)
    :param card: card information [Rank][Suit]
    :paramtype card: string
    :return: parsed card information
    :rtype: tuple(int,string)
    """
    card_info = None
    
    if len(card) > 3 or card[-1] not in suits :
        print("Wrong format")

    card_rank = card[0:len(card) - 1]
    
    if card_rank.isalpha():
        
        if card_rank in alpha_ranks:
            card_info = alpha_ranks[card_rank],card[-1]
        else:
            print("Wrong format")

    else:
        
        card_rank = int(card_rank)
        if card_rank > 10 :
            print("Wrong format")
        else:
            card_info = card_rank,card[-1]

    return card_info


def get_hand_combination_rank(hand):
    """
    finds appropriate hand combination
    :param hand: string with info about five cards
    :paramtype hand: string
    :return: hand combination rank and highest card rank
    :rtype: tuple(int,int)
    """

    cards = [get_card_info(card) for card in hand.split(' ')]

    if len(cards) != CARDS_IN_HAND:
        print("Wrong number of cards")

    cards.sort()
    highest_rank = cards[-1][0]

    is_sequential = (cards[-1][0] - cards[0][0] == 4 and len(cards) == len(set([card_info[0] for card_info in cards])))
    is_one_suit = len(set([card_info[1] for card_info in cards])) == 1
    
    counter = Counter(card_info[0] for card_info in cards)

    most_common_ranks_count = [result[1] for result in counter.most_common(2)]

    hand = high_card
    
    if is_sequential and is_one_suit:
        hand = royal_flush if cards[0][0] == LOWEST_RANK_ROYAL_FLASH else straight_flush

    elif most_common_ranks_count[0] == CARDS_IN_HAND - 1:
        hand = four_of_kind

    elif sum(most_common_ranks_count) == CARDS_IN_HAND:
        hand = full_house

    elif is_one_suit:
        hand = flush
    
    elif is_sequential:
        hand = straight

    elif most_common_ranks_count[0] == CARDS_IN_HAND - 2:
        hand = three_of_kind

    elif sum(most_common_ranks_count) == CARDS_IN_HAND - 1:
        hand = two_pairs

    elif most_common_ranks_count[0] == CARDS_IN_HAND - 3:
        hand = one_pair

    return (hand, highest_rank)


def pick_best_poker_hands(hands):
    """
    finds best hand in list of hands
    :param hand: list of hands
    :paramtype hand: list(string)
    :return: list of best hands
    :rtype: list(string)
    """    
    hand_combination_ranks = [(get_hand_combination_rank(hand), hand) for hand in hands]

    max_combination_rank = max(combination[0][0] for combination in hand_combination_ranks)
    best_combination_hands = [(hand[0][1], hand[1]) for hand in hand_combination_ranks if hand[0][0] == max_combination_rank]
    max_rank_in_best_combinations = max(hand[0] for hand in best_combination_hands)
    best_hands = [hand[1] for hand in best_combination_hands if hand[0] == max_rank_in_best_combinations]
    return best_hands
    
    
print(pick_best_poker_hands([
"2S 4C 7S 9H 10H",
"3S 4S 5D 6H JH",
"3H 4H 5C 6C JD",
"4D 5S 6S 8D 3C"]))
