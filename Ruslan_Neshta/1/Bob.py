def talk(string):
    answer = "Whatever."

    question = string.count('?') > 0
    if string.isupper():
        if question:
            answer = "Calm down, I know what I'm doing!"
        else:
            answer = "Whoa, chill out!"
    elif question:
        answer = "Sure."
    return answer


if __name__ == "__main__":
    phrase = input("Enter a phrase you want to say to Bob: ")
    result = talk(phrase)
    print(result)
