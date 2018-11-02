COMMANDS_TYPES = ("left", "right", "up", "down")

def get_direction():

    while True:

        direction = input("input direction:")

        if direction in COMMANDS_TYPES:
            
            return direction


if __name__ == "__main__":
    my_map = create_map(5)
    for i in range(len(my_map)):
        print("".join(my_map[i]))