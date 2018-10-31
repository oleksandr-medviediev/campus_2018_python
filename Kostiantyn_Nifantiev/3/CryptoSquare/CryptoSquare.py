from CryptoSquareFunction import encode_string, decode_string

while True:

    string_to_encode = input('Type your string to encode:\n')
    print(string_to_encode)
    encoded_string = encode_string(string_to_encode)
    print(encoded_string)
    decoded_string = decode_string(encoded_string)
    print(decoded_string)
