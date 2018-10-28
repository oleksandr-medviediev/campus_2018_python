def main():
    key_str = input('key:\n')
    if not key_str.isdigit():
        print('key must be an integral number')
    
    key = int(key_str)
    if key < 0 or key >= 26:
        print('key must ∈ [0, 26)')
        return

    text = input('text:\n')

    cyphered = [cypher(ch, key) if ch.isalpha() else ch for ch in text]
    print("".join(cyphered))

def cypher(ch, key):
    alphabet_size = 26
    alph_start = ord('A') if ch.isupper() else ord('a')

    alph_index = ord(ch) - alph_start
    cyphered_alph_index = (alph_index + key) % alphabet_size
    return chr(alph_start + cyphered_alph_index)


if __name__ == "__main__":
    main()