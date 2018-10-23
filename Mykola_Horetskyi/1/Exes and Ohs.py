text = input('input text:\n')

numberOfO = text.count('o') + text.count('O')

numberOfX = text.count('x') + text.count('X')

isSameNumber = numberOfO == numberOfX

print(isSameNumber)
