# so cool but no
# print(input()[::-1])

string = input()
rev_indices = range(len(string) - 1, -1, -1)
ls = [string[i] for i in rev_indices]
print(''.join(ls))