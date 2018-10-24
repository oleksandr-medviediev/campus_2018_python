
def reverse_string(string):
    tmp = []
    for i in range(len(string), 0, -1):
        tmp.append(string[i - 1])
    return str().join(tmp)

if __name__ == "__main__":
    print(reverse_string(input("enter sth:\n")))
