from Poker import pick_best_poker_hands

example_1 = ["4D 5S 6S 8D 3C",
"2S 4C 7S 9H 10H",
"3S 4S 5D 6H JH"]

example_2 = ["4D 5S 6S 8D 3C",
"2S 4C 7S 9H 10H",
"3S 4S 5D 6H JH",
"3H 4H 5C 6C JD"]

result_1 = pick_best_poker_hands(example_1)
result_2 = pick_best_poker_hands(example_2)

print(result_1)
print(result_2)
