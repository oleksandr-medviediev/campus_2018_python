
def main():
    print(quicker(input()))

def quicker (string):
    x_count = o_count = 0
    for ch in string:
        if ch == 'x':
            x_count += 1
        elif ch == 'o':
            o_count += 1

    return x_count == o_count

def nicer (string):
    return string.count('x') == string.count('o')

if __name__ == "__main__":
    main()