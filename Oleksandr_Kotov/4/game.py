
def _structure_is_near(structure, curr_row, curr_col, squares_map):
    
    is_near = False
    scale = len(squares_map)

    if curr_col < scale - 1:
        if squares_map[curr_row][curr_col + 1] == structure:
            is_near = True

    if curr_col > 1:
        if squares_map[curr_row][curr_col - 1] == structure:
            is_near = True

    if curr_row < scale - 1:
        if squares_map[curr_row + 1][curr_col] == structure:
            is_near = True

    if curr_row > 1:
        if squares_map[curr_row - 1][curr_col] == structure:
            is_near = True

    return is_near

def run(start_row, start_col, squares_map):
    
    border = len(squares_map) - 1

    curr_row = start_row
    curr_col = start_col

    while True:

        if squares_map[curr_row][curr_col] == 't':

            print("You have entered a trap!")
            break

        if squares_map[curr_row][curr_col] == '*':
            
            print("You have found a treasure!")
            break

        if _structure_is_near('t', curr_row, curr_col, squares_map):
            print('There is a trap within one square!')

        if _structure_is_near('*', curr_row, curr_col, squares_map):
            print('There is a treasure within one square!')

        while True:
            direction = input("Where to go?: ")

            if direction == 'up':

                if curr_row == 0:
                    print("You are already on top of the map!")

                else:

                    print("Moving up")
                    curr_row -= 1
                    break

            elif direction == 'down':

                if curr_row == border:
                    print("You are already on bottom of the map!")

                else:

                    print("Moving down")
                    curr_row += 1
                    break
            
            elif direction == 'right':

                if curr_col == border:
                    print("You are already on the right border of the map!")

                else:

                    print("Moving right")
                    curr_col += 1
                    break

            elif direction == 'left':

                if curr_col == 0:
                    print("You are already on the left border of the map!")

                else:

                    print("Moving left")
                    curr_col -= 1
                    break

            else:
                print("Unknown command")
                