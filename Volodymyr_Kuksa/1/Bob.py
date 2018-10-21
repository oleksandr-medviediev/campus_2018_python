print('Type whatever you want to tell Bob or type "Bye" to end the conversation.')

is_conversation_going = True

while is_conversation_going:
    input_string = input('\n- ')

    input_string = input_string.strip()

    if len(input_string) == 0:
        print('- Fine. Be that way!')
        continue

    is_question = input_string[-1] == '?'
    is_yelling = input_string.isupper()

    if input_string == "Bye":
        is_conversation_going = False
        print('- Finally!')
    elif is_question and is_yelling:
        print("- Calm down, I know what I'm doing!")
    elif is_question:
        print('- Sure.')
    elif is_yelling:
        print('- Whoa, chill out!')
    else:
        print('- Whatever.')

