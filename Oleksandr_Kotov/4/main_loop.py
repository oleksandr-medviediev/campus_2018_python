import terrain
import game

print("Welcome to the game!")
print("Type up/down/left/right to move")

while True:

    scale = input("Enter map scale: ")

    start_row, start_col, squares_map = terrain.generate(int(scale))

    game.run(start_row, start_col, squares_map)

    for row in squares_map:
        print(row)

    print("\n* - stands for a treasure")
    print("t - stands for a trap")
    print(". - stands for an empty square")
    print("s - stands for the start position\n")

    answer = input("Play again? (y/n): ")

    if answer != 'y':
        break