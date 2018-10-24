# list methods!

# list comprehensions

numbers = [i ** i for i in range(10)]   # same as map, but better
print(numbers)

filtered_numbers = [i ** i for i in range(10) if not i % 2]
print(filtered_numbers)

# tuple
x = 1, 2, 3

a, b, c = x
print(a, b, c)

# set

some_set = {'a', 'b', 'c'}  # no indexes

# frozenset - immutable set

# dict - dictionary

some_dict = {'a': 1, 'b': 2, 'c': 3}
print(some_dict['a'])

for key, value in some_dict.items():

    print(key, value)

# looping techniques

sequence = [1, 2, 3, 4, 5]

for i, el in enumerate(sequence):

    sequence[i] = el * 2

print(sequence)

for i in reversed(sequence):

    print(i)

for i in sorted(sequence):  # can be used with dict

    pass

sequence_2 = 'abcdefghi'

for i in zip(sequence, sequence_2):

    print(i)
