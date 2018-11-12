class Card:
    Ranks_order = [
        *map(str, range(2, 11)),  # all numerical cards' ranks
        'J',
        'Q',
        'K',
        'A',
    ]

    def __init__(self, card_str):
        self.rank = card_str[:-1]
        self.suite = card_str[-1]

    @property
    def rank_order(self):
        return Card.Ranks_order.index(self.rank)

    def __str__(self):
        return self.rank + self.suite

    def __repr__(self):
        return str(self)


def to_cards(hand_str):
    return list(map(Card, hand_str.split()))


def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)


def is_four_of_a_kind(hand):
    ranks = [card.rank_order for card in hand]
    found = any(ranks.count(rank) == 4 for rank in ranks)
    return found


def is_full_house(hand):
    return is_three_of_a_kind(hand) and is_pair(hand)


def is_flush(hand):
    return all(card.suite == hand[0].suite for card in hand[1:])


def is_straight(hand):
    ranks = sorted({card.rank_order for card in hand})

    previous_rank = ranks[0]
    for rank in ranks[1:]:
        if rank != previous_rank + 1:
            return False
        previous_rank = rank

    return True


def is_three_of_a_kind(hand):
    ranks = [card.rank_order for card in hand]
    found = any(ranks.count(rank) == 3 for rank in ranks)
    return found


def is_two_pair(hand):
    ranks = [card.rank_order for card in hand]
    pairs_found = set()
    for rank in ranks:
        if ranks.count(rank) == 2:
            pairs_found.add(rank)

    return len(pairs_found) == 2


def is_pair(hand):
    ranks = [card.rank_order for card in hand]
    found = any(ranks.count(rank) == 2 for rank in ranks)
    return found


Hand_ranks = [
    is_pair,
    is_two_pair,
    is_three_of_a_kind,
    is_straight,
    is_flush,
    is_full_house,
    is_four_of_a_kind,
    is_straight_flush
]


def find_hand_rank(hand):
    for rank, is_ranked_hand in reversed(list(enumerate(Hand_ranks))):
        if is_ranked_hand(hand):
            return rank


def pick_best_hands(hands_str):
    ranked_hands = {}
    for hand in map(to_cards, hands_str):
        hand_rank = find_hand_rank(hand)
        ranked_hands[hand_rank] = ranked_hands.get(hand_rank, [])
        ranked_hands[hand_rank].append(hand)

    best_hands = ranked_hands[max(ranked_hands.keys())]
    return best_hands


print(pick_best_hands([
    '5S 2C 5C 5D 5C',
    '5C 2H 3C 6D 4C',
    '5C 2S 2C 2D 5H',
    'AD JD KD 10D QD',
    '4D 2C 2S 4C 4C',
]))
