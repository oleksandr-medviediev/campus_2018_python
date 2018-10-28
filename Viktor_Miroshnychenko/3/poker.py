CARD_HIGH = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
cards = CARD_HIGH
cards.reverse()

def check_five_kind(hand):
    """
    :param hand: hand to check on five of a kind
    :type hand: str

    :return: True if five of a kind, False otherwise
    :rtype: bool
    """

    ret_val = True
    hand = hand.replace(" ", "")
    for it in range(4):
        if hand[it * 2] != "A":
            ret_val = False
    if hand[-2] != "J":
        ret_val = False

    return ret_val


def check_flash(hand):
    """
    :param hand: hand to check on flash 
    :type hand: str

    :return: True(if flash) or False(otherwise)
    :rtype: bool
    """

    flash = True
    hand = hand.replace(" ", "")
    first_suit = hand[1]
    for it in range(4):
        if hand[it*2 + 3] != first_suit:
            flash = False

    return flash


def check_straight(hand):
    """
    :param hand: hand to check on straight 
    :type hand: str

    :return: True(if straight) or False(otherwise)
    :rtype: bool
    """

    straight = False
    hand = hand.replace(" ", "")
    counter = 0
    for card in CARD_HIGH:
        if hand.rfind(card) != -1:
            counter += 1
        else:
            counter -= 1

        if counter == 5:
            straight = True
            break

    return straight


def check_straight_flash(hand):
    """
    :param hand: hand to check on straight flash
    :type hand: str

    :return: True(if straight flash) or False(otherwise) 
    :rtype: bool
    """

    str_flash = check_flash(hand)
    ret_val = str_flash
    if str_flash:
        ret_val = check_straight(hand)

    return ret_val


def check_four_kind(hand):
    """
    :param hand: hand to check on four of a kind
    :type hand: str

    :return: True if four of a kind, False otherwise
    :rtype: bool
    """

    ret_val = False
    hand = hand.replace(" ", "")
    for it in range(5):
        if hand.count(hand[it * 2]) == 4:
            ret_val = True
            break

    return ret_val


def check_pair(hand):
    """
    :param hand: hand to check on pair
    :type hand: str

    :return: True if pair present, False otherwise
    :rtype: bool
    """

    ret_val = False
    hand = hand.replace(" ", "")
    for it in range(5):
        if hand.count(hand[it*2]) == 2:
            ret_val = True
            break

    return ret_val


def check_three_kind(hand):
    """
    :param hand: hand to check on three of a kind
    :type hand: str

    :return: True if three of a kind, False otherwise
    :rtype: bool
    """

    ret_val = False
    hand = hand.replace(" ", "")
    for it in range(5):
        if hand.count(hand[it * 2]) == 3:
            ret_val = True
            break

    return ret_val


def check_two_pairs(hand):
    """
    :param hand: hand to check on two pairs
    :type hand: str

    :return: True if has three pairs, False otherwise
    :rtype: bool
    """

    pair_amount = 0
    hand = hand.replace(" ", "")
    for it in range(5):
        if hand.count(hand[it*2]) == 2:
            pair_amount += 1

    return pair_amount == 4


def check_full_house(hand):
    """
    :param hand: hand to check on full house
    :type hand: str

    :return: True if full house, False otherwise
    :rtype: bool
    """

    return check_pair(hand) and check_three_kind(hand)


def find_highest_card(hand):
    """
    :param hand: hand to search a card in
    :type hand: str

    :return: highest card index in CARD_HIGH
    :rtype: int
    """

    global cards
    ret_val = 0
    tmp_list = hand.split(" ")
    tmp = ""
    for l in tmp_list:
        l = l[:-1]
        tmp += l
    hand = tmp    

    for card in cards:
        if hand.rfind(card) != -1:
            ret_val = CARD_HIGH.index(card)
            break

    return ret_val


def find_hand(hands):
    """
    :param hands: list of hands
    :type hands: list[str]

    :return: highest hand
    :rtype: str
    """

    power_list = []
    for index in range(len(hands)):
         power_list.append(0)
    for index in range(len(hands)):
        if check_five_kind(hands[index]):
            power_list[index] = 10
        elif check_straight_flash(hands[index]):
            power_list[index] = 9
        elif check_four_kind(hands[index]):
            power_list[index] = 8
        elif check_full_house(hands[index]):
            power_list[index] = 7
        elif check_flash(hands[index]):
            power_list[index] = 6
        elif check_straight(hands[index]):
            power_ist[index] = 5
        elif check_three_kind(hands[index]):
            power_list[index] = 4
        elif check_two_pairs(hands[index]):
            power_list[index] = 3
        elif check_pair(hands[index]):
            power_list[index] = 2

    hand_index = 0
    for index in range(len(power_list) - 1):
        index += 1
        if power_list[index] > power_list[hand_index]:
            hand_index = index
        elif power_list[index] == power_list[hand_index]:
            if find_highest_card(hands[index]) < find_highest_card(hands[hand_index]):
                hand_index = index

    return hands[hand_index]


print(find_hand( ["4D 5S 6S 8D 3C", "2S 4C 7S 9H 10H", "3S 4S 5D 6H JH"]))
print(find_hand(["4D 5S 6S 8D 3C", "2S 4C 7S 9H 10H", "3S 4S 5D 6H JH", "3H 4H 5C 6C JD"]))
