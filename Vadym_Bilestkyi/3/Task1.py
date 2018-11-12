number_spelling = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

tens_spelling = [
    'zero',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]

powers_spelling = [
    'thousand',
    'million',
    'billion',
]


def add_plural(number):
    if int(number) > 1:
        return 's'
    return ''


def spell_number(number):
    if not 0 <= number <= 999999999999:
        return 'Unspelling number'

    number_str = str(number)

    splitted_powers = [number_str[i - 3 if i >= 3 else 0:i] for i in range(len(number_str), 0, -3)]
    hundreds, splitted_powers = splitted_powers[0], splitted_powers[1:]

    spelled_powers = [spell_power(power, i) for i, power in enumerate(splitted_powers)]

    spelled = ''.join(reversed(spelled_powers))
    spelled = ''.join((spelled, spell_power(hundreds)))
    return spelled


def spell_power(power_value, power=None):
    hundreds = None
    tens = None
    ones = None

    if int(power_value) >= 100:
        hundreds, ones = power_value[0], power_value[1:]
    else:
        ones = power_value

    if int(ones) > 20:
        tens, ones = ones
    elif int(ones) == 0:
        ones = None

    spelled = ''
    if hundreds:
        spelled += '{} {}{} '.format(number_spelling[int(hundreds)], 'hundred', add_plural(hundreds))
    if tens:
        spelled += '{} '.format(tens_spelling[int(tens)])
    if ones:
        spelled += number_spelling[int(ones)]

    if power is not None:
        spelled = '{} {}{} '.format(spelled, powers_spelling[power], add_plural(power_value))

    return spelled

print(spell_number(1))
print(spell_number(6))
print(spell_number(15))
print(spell_number(65))
print(spell_number(412))
print(spell_number(2123))
print(spell_number(11121523412))
print(spell_number(1111124523412))
