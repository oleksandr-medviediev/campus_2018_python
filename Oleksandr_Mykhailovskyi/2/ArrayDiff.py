def array_diff(sequenceA, sequenceB):
    return [i for i in sequenceA if sequenceB.count(i) == 0]

sequenceA = input()
number_sequenceA = sequenceA.split()
sequenceB = input()
number_sequenceB = sequenceB.split()
number_sequenceA = array_diff(number_sequenceA, number_sequenceB)
print(number_sequenceA)
