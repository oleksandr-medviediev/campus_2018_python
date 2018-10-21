twit = input('Normal guy writes a text on Twitter like this: ')
words = twit.split(' ')
for i in range(len(words)):
    words[i] = words[i].capitalize()
capitalizedTwit = str(' ').join(words)
print('But Jaden does things this way: ' + capitalizedTwit)