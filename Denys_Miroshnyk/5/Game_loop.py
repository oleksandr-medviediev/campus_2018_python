import Map_generator


player_position = (-1, -1)

player_moves = {1: 'up', 2: 'down', 3: 'right', 4: 'left'}
player_actions = {
    1: lambda point: [point[0], point[1] + 1],
    2: lambda point: [point[0], point[1] - 1],
    3: lambda point: [point[0] + 1, point[1]],
    4: lambda point: [point[0] - 1, point[1]]}


def player_input(game_map):
    global player_position

    print("Your action : ", *
          [f'{key} - {val},' for key, val in player_moves.items()])
    action = int(input())

    result = True
    if action in player_actions.keys():
        player_position_new = player_actions[action](player_position)
        cell_type = game_map[player_position_new[1]][player_position_new[0]]
        if cell_type == Map_generator.treasure or cell_type == Map_generator.trap:
            player_position = player_position_new
            result = False
        elif cell_type == Map_generator.wall:
            print("you found the wall. Can't move further")
        else:
            game_map[player_position[1]][player_position[0]] = Map_generator.empty_cell
            player_position = player_position_new
            game_map[player_position[1]][player_position[0]] = Map_generator.player
    else:
        print("invalid input \n")

    return result


def print_state(game_map):
    global player_position

    for val in player_actions.values():
        player_neighbored_point = val(player_position)
        if game_map[player_neighbored_point[1]][player_neighbored_point[0]] == Map_generator.trap:
            print("trap is somewhere near")
        elif game_map[player_neighbored_point[1]][player_neighbored_point[0]] == Map_generator.treasure:
            print("Treasure is somewhere near")


def loop(game_map):
    global player_position
    print_state(game_map)

    while player_input(game_map):
        print_state(game_map)

    cell_type = game_map[player_position[1]][player_position[0]]
    if cell_type == Map_generator.treasure:
        print("you found the treasure! Victory")
    else:
        print("Trap *traps*\n You *lost* xD")
