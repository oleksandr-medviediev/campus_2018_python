def is_flush(suits, ranks):
	count_suits = len({s : suits.count(s) for s in suits})
	
	return count_suits == 1, max(ranks)
	

def is_straight(ranks):
	
	#the least straight
	if ranks == [14, 5, 4, 3, 2]:
		return True, 5
		
	isstraight = True
	for i in range(len(ranks) - 1):
		isstraight = ranks[i] - ranks[i + 1] == 1
		
	return isstraight, max(ranks)	


def has_n_of_a_kind(ranks, n):
	
	count_ranks = {i : ranks.count(i) for i in ranks}

	count_ranks_v = list(count_ranks.values())
	count_ranks_v.sort(reverse = True)
	
	has_n = max(count_ranks_v) == n
	
	elder_card = 0
	if has_n:
		elder_card = list(count_ranks.keys())[list(count_ranks.values()).index(n)]

	return has_n, elder_card


def has_n_and_m_of_a_kind(ranks, n, m):
	
	n, m = max(n, m), min(n, m)

	has_n, elder_card = has_n_of_a_kind(ranks, n)

	ranks = list(filter(lambda c : c != elder_card, ranks))

	has_m, card = has_n_of_a_kind(ranks, m)

	return has_n and has_m, elder_card


def calculate_hand_rank(hand):

	CARD_RANK = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
	HAND_RANK = {'high card' : 1, 'pair' : 8, 'two pairs' : 64, 'three of a kind' : 512, 'straight' : 4096, 'flush' : 32768, 'full house' : 262144, 'four of a kind' : 2097152, 'straight flush' : 16777216}

	suits = [c[1] for c in hand]

	ranks = [CARD_RANK[c[0]] for c in hand]
	ranks.sort(reverse = True)

	hand_is_flush, elder_card_f = is_flush(suits, ranks)
	hand_is_straight, elder_card_s = is_straight(ranks)

	if hand_is_flush or hand_is_straight:

		if hand_is_straight and hand_is_flush:
			hand_rank = HAND_RANK['straight flush'] * elder_card_s

		elif hand_is_flush:
			hand_rank = HAND_RANK['flush'] * elder_card_f

		else:
			hand_rank = HAND_RANK['straight'] * elder_card_s

	else:

		hand_has_4_of_kind, elder_card_4 = has_n_of_a_kind(ranks, 4)
		hand_has_3_of_kind, elder_card_3 = has_n_of_a_kind(ranks, 3)
		hand_has_full_house, elder_card_fh = has_n_and_m_of_a_kind(ranks, 3, 2)
		hand_has_two_pairs, elder_card_2p = has_n_and_m_of_a_kind(ranks, 2, 2)
		hand_has_pair, elder_card_2 = has_n_of_a_kind(ranks, 2)

		if hand_has_4_of_kind:
			hand_rank = HAND_RANK['four of a kind'] * elder_card_4

		elif hand_has_full_house:
			hand_rank = HAND_RANK['full house'] * elder_card_fh

		elif hand_has_3_of_kind:
			hand_rank = HAND_RANK['three of a kind'] * elder_card_3

		elif hand_has_two_pairs:
			hand_rank = HAND_RANK['two pairs'] * elder_card_2p

		elif hand_has_pair:
			hand_rank = HAND_RANK['pair'] * elder_card_2

		else:
			hand_rank = HAND_RANK['high card'] * max(ranks)

	return hand_rank


def find_max_hand_rank(hands_with_ranks):

	max_rank = max(list(hands_with_ranks.values()))
	hands_max_rank = [k for k, v in hands_with_ranks.items() if v == max_rank]

	return hands_max_rank


input_str = ''
hands = []
hand_ranks = []
input_str = input('Enter hand: \n')
while input_str != 'q' && input_str != '':

	hand = input_str.split()
	hand = [(c[:len(c) - 1], c[-1]) for c in hand]

	rank = calculate_hand_rank(hand)

	hands.append(input_str)
	hand_ranks.append(rank)

	input_str = input('Enter hand: \n')

print (*zip(hands, hand_ranks))

hands_with_ranks = {c[0] : c[1] for c in zip(hands, hand_ranks)}

the_best_hands = find_max_hand_rank(hands_with_ranks)

print(the_best_hands)
