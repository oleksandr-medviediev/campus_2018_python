CARD_RANK = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def is_straight(ranks):
    """check if ranks form the straight

    Arguments:
        ranks [str] -- list of ranks

    Returns:
        bool -- true if ranks form the straight, false otherwise
    """

    ranks = [CARD_RANK[rank] for rank in ranks]

    ranks.sort()

    result = True

    for idx, rank in enumerate(ranks[:-1]):

            if rank + 1 != ranks[idx + 1]:
                result = False

    return result


def compute_score(cards):
    """compute card hand score

    Arguments:
        cards str -- cards in hand separated by space

    Returns:
        int -- hand score
    """

    cards = cards.split()
    ranks = [card[:-1] for card in cards]

    rank_variety = len(set(ranks))

    score = 9

    if rank_variety == 5:

        suits = [card[-1] for card in cards]
        is_flush = len(set(suits)) == 1

        if is_straight(ranks) and is_flush:
            score = 1
        elif is_straight(ranks):
            score = 5
        elif is_flush:
            score = 4

    elif rank_variety == 4:
        score = 8

    elif rank_variety == 3:

        counts = [ranks.count(rank) for rank in ranks]

        if max(counts) == 2:
            score = 7
        else:
            score = 6

    elif rank_variety == 2:

        counts = [ranks.count(rank) for rank in ranks]

        if max(counts) == 4:
            score = 2
        else:
            score = 3

    return score


def higher_card(hands):
    """check if hand1 has higher card than hand2

    Arguments:
        hands [str] -- list of hands with cards in hand separated by space

    Returns:
        [str] -- list of hands with highest cards
    """

    hands_ranks = []

    for hand in hands:

        ranks = hand.split()
        ranks = [CARD_RANK[card[:-1]] for card in ranks]
        ranks.sort(reverse=True)
        hands_ranks.append(ranks)

    print(hands_ranks)

    curr_idx = 0

    while curr_idx < 5:

        elements = list(zip(*hands_ranks))[curr_idx]
        max_rank = max(elements)

        new_ranks = []
        new_hands = []

        for element in elements:

            i = elements.index(element)

            if element == max_rank:

                new_ranks.append(hands_ranks[i])
                new_hands.append(hands[i])

        hands_ranks = new_ranks
        hands = new_hands
        curr_idx += 1

    return hands


def pick_best_poker_hands(hands):
    """pick best poker hand

    Arguments:
        hands [str] -- list of poker hands

    Returns:
        [str] -- list of best poker hands
    """

    scores = [compute_score(cards) for cards in hands]

    high_score = min(scores)

    for cards, score in zip(hands, scores):

        if score < high_score:

            hands.remove(cards)
            scores.remove(score)

    hands = higher_card(hands)

    return hands

