
def array_diff(sequenceA, sequenceB):
    setA, setB = set(sequenceA), set(sequenceB)
    return setA - setB

A = [1, 2, 3, 4, 1, 1, 4]
B = [2, 3, 1]

A = list(array_diff(A, B))
print(A)