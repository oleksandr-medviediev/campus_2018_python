def check_is_royal_flush(item):
    """Function check if royal flush.

    Args:
        item: type str.

    Returns:
        Return True or False.

    """

    hand_number = []
    hand_suit = []

    phrases = item.split(' ')

    for i in phrases:
        number = i[:len(i) - 1]
        hand_number.append(number)

        suit = i[len(i) - 1:]
        hand_suit.append(suit)

    result_number = False

    if (("A" in hand_number) and
        ("K" in hand_number) and
        ("Q" in hand_number) and
        ("J" in hand_number) and
        ("10" in hand_number)):
            result_number = True

    result_suit = False

    if hand_suit.count(hand_suit[0]) == len(hand_suit):
        result_suit = True

    return (result_number and result_suit)


def check_is_straight_flush(hand_number, hand_suit):
    """Function check if straight flush.

    Args:
        hand_number: type list.
        hand_suit: type list

    Returns:
        Return True or False.

    """
    result_number = True

    for i in range(len(hand_number) - 1):
        if hand_number[i] <= hand_number[i + 1]:
            result_number = False
            break

    result_suit = False

    if(hand_suit.count(hand_suit[0]) == len(hand_suit)):
        result_suit = True

    return (result_number and result_suit)


def check_is_four_king(hand_number, hand_suit):
    """Function check if four king.

    Args:
        hand_number: type list.
        hand_suit: type list

    Returns:
        Return True or False.

    """
    hand_number.sort()

    result_number = False
    if hand_number.count(hand_number[2]) == 4:
        result_number = True

    hand_suit.sort()
    result_suit = False
    if hand_suit.count(hand_suit[2]) < 3 :
        result_suit = True


    return (result_number and result_suit)


def check_is_full_house(hand_number):
    """Function check if full house.

    Args:
        hand_suit: type list.

    Returns:
        Return True or False.

    """
    hand_number.sort()
    if (hand_number.count(hand_number[0]) == 3) and (hand_number.count(hand_number[4]) == 2):
        return True
    elif (hand_number.count(hand_number[0]) == 2) and (hand_number.count(hand_number[4]) == 3):
        return True

    return False


def check_is_flush(hand_suit):
    """Function check if flush.

    Args:
        hand_suit: type list.

    Returns:
        Return True or False.

    """
    if hand_suit.count(hand_suit[0]) == len(hand_suit):
        return True

    return False


def check_is_straight(hand_number):
    """Function check if straight.

    Args:
        hand_number: type list.

    Returns:
        Return True or False.

    """
    result_number = True

    for i in range(len(hand_number) - 1):
        if hand_number[i] <= hand_number[i + 1]:
            result_number = False
            break

    return result_number


def check_is_tree_of_king(hand_number):
    """Function check if tree of king

    Args:
        hand_number: type list.

    Returns:
        Return True or False.

    """
    hand_number.sort()

    if hand_number.count(hand_number[2]) == 3:
        return True

    return False


def check_is_two_pair(hand_number):
    """Function check if two_pair

    Args:
        hand_number: type list.

    Returns:
        Return True or False.

    """
    hand_number.sort()

    first_pair = False
    if (hand_number[1] == hand_number[0]) or (hand_number[1] == hand_number[2]):
        first_pair = True

    second_pair = False
    if (hand_number[3] == hand_number[4]) or (hand_number[3] == hand_number[2]):
        second_pair = True

    return (first_pair and second_pair)


def check_is_pair(hand_number):
    """Function check if pair

    Args:
        hand_number: type hand_number.

    Returns:
        Return True or False.

    """
    for i in hand_number:
        if hand_number.count(i) == 2:
            return True

    return False


def split_string(item, hand_number, hand_suit):
    """Function split string on numbers and suits

    Args:
        hand_number: type list.
        hand_suit: type list

    Returns:
        Return None.

    """

    data = {
        "A": 1,
        "K": 13,
        "Q": 12,
        "J": 11
    }

    phrases = item.split(' ')

    for i in phrases:
        number = i[:len(i) - 1]
        if number in data:
            hand_number.append(int(data[number]))
        else:
            hand_number.append(int(number))

        suit = i[len(i) - 1:]
        hand_suit.append(suit)


def check_combinations(array):
    """Function search the best combination

    Args:
        array: type list.

    Returns:
        Return list.

    """

    data = {
        "royal_flush": [],
        "straight_flush": [],
        "four_king": [],
        "full_house": [],
        "flush": [],
        "straight": [],
        "tree_of_king": [],
        "two_pair": [],
        "pair": [],
        "none": []
    }

    for i in array:
        hand_number = []
        hand_suit = []
        split_string(i, hand_number, hand_suit)

        if(check_is_royal_flush(i)):
            data["royal_flush"].append(i)
            continue
        elif(check_is_straight_flush(hand_number, hand_suit)):
            data["straight_flush"].append(i)
            continue
        elif(check_is_four_king(hand_number, hand_suit)):
            data["four_king"].append(i)
            continue
        elif(check_is_full_house(hand_number)):
            data["full_house"].append(i)
            continue
        elif(check_is_flush(hand_suit)):
            data["flush"].append(i)
            continue
        elif(check_is_straight(hand_number)):
            data["straight"].append(i)
            continue
        elif(check_is_tree_of_king(hand_number)):
            data["tree_of_king"].append(i)
            continue
        elif(check_is_two_pair(hand_number)):
            data["two_pair"].append(i)
            continue
        elif(check_is_pair(hand_number)):
            data["pair"].append(i)
            continue
        else:
            data["none"].append(i)
            continue

    for k in data:
        if(len(data[k]) > 0):
            return data[k]

    return []


if __name__ == '__main__':
    result = check_combinations(["10D 10C 10S 8H 7D",
                                 "8D 8C 8S KH KD",
                                 "2D 9C 3S 2H 7D"])
    print(result)
