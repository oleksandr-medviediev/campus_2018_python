def str_to_card(input_str):
	if len(input_str) > 2:
		card = input_str[:2], input_str[-1]
	else:
		card = input_str[0], input_str[-1]

	SUIT = {'H' : 0, 'S' : 1, 'C' : 2, 'D' : 3}
	CARD_RANK = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8,
	'9' : 9, '10' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}

	card = CARD_RANK[card[0]], SUIT[card[1]]

	return card


def str_to_hand(input_str):

	cards = input_str.split()
	cards = list(map(str_to_card, cards))

	return cards


def check_royal_flush(hand):
	cards_ranks = [card[0] for card in hand]
	cards_ranks.sort()

	royal = [10, 11, 12, 13, 14]

	return cards_ranks == royal


def check_staight_flush(hand):

	cards_ranks = [card[0] for card in hand]
	cards_ranks.sort()

	straights = [
	[2, 3, 4, 5, 6],
	[3, 4, 5, 6, 7],
	[4, 5, 6, 7, 8],
	[5, 6, 7, 8, 9],
	[6, 7, 8, 9, 10],
	[7, 8, 9, 10, 11],
	[8, 9, 10, 11, 12],
	[9, 10, 11, 12, 13],
	[2, 3, 4, 5, 14]
	]

	return cards_ranks in straights, cards_ranks[4]


def check_flush(hand):

	cards_ranks = [card[0] for card in hand]
	cards_ranks.sort()

	is_flush = False
	if all_same_suit(hand):
		is_flush = True
		flush_rank = cards_ranks[4]

		is_straight, straight_rank = check_staight_flush(hand)
		is_royal = check_royal_flush(hand)

	rank = -1

	if is_royal:
		rank = HANDS_RANK['royal'] * 200

	elif is_straight:
		rank = HANDS_RANK['straight_flush'] * straight_rank

	elif is_flush:
		rank = HANDS_RANK['flush'] * flush_rank

	return rank



def all_same_suit(hand):

	suits = [card[1] for card in hand]
	same_suits = {s : suits.count(s) for s in suits}

	return len(same_suits.items()) == 1


def group_same_ranks(hand):

	ranks = [card[0] for card in hand]
	ranks.sort()
	same_ranks = {s : ranks.count(s) for s in ranks}

	return same_ranks


def check_some_of_a_kind(hand):
	rank = -1

	same_ranks = group_same_ranks(hand)
	if max(same_ranks.values()) == 4:
		rank = HANDS_RANK['four_of_a_kind'] * list(same_ranks.keys())[list(same_ranks.values()).index(16)]


def hand_get_rank(hand):
	"""
	returns rank of hand
	: param : hand : list of 5 pairs, represent 5 cards in a hand

	: return : rank on card set
	: rtype : int
	"""


global HANDS_RANK
HANDS_RANK = {
	'royal_flush' : 9,
	'straight_flush' : 8,
	'four_of_a_kind' : 7,
	'full_house' : 6,
	'flush' : 5,
	'straight' : 4,
	'three_of_a_kind' : 3,
	'two_pairs' : 2,
	'one_pair' : 1,
	'high_card' : 0
}



hands1 = ["4D 5S 6S 8D 3C",
"2S 4C 7S 9H 10H",
"3S 4S 5D 6H JH"]

hands2 = ["4D 5S 6S 8D 3C",
"2S 4C 7S 9H 10H",
"3S 4S 5D 6H JH",
"3H 4H 5C 6C JD"]

rank = check_flush(hands1[1])

if rank > 0:
	hands_ranks.append(hands1[1] : rank)





