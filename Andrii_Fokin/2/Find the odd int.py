
def find_odd(arr):
    Set = set(arr)
    for val in Set :
        if arr.count(val) % 2:
            return val

print(find_odd([1, 2, 3, 1, 3, 2, 1]))