import dungeon_map_generate
import dungeon_logic


def run_frame(dun_map, position):
    """
    :param dun_map: map for game
    :type dun_map: list[list[]]

    :param position: position of plauer on the map
    :type position: list[x, y]

    :return: game state from dungeon_logic.GAME_STATE
    :rtype: str
    """

    print('\n')
    command = ''
    while command not in dungeon_logic.COMMANDS:
        command = input("Type valid input \n")

    game_state = dungeon_logic.make_move(dun_map, position, len(dun_map), command)

    return game_state


def game():
    """
    :description: run dungeon game
    
    :return:
    :rtype:
    """

    size = int(input('Type map size \n'))
    dun_map = dungeon_map_generate.generate_map(size)
    position = dungeon_map_generate.set_player_randomly(dun_map)

    print("Use following commands to navigate your position", dungeon_logic.COMMANDS)

    game_state = 'ingame'
    while game_state == 'ingame':
        game_state = run_frame(dun_map, position)

    for row in dun_map:
        print(row)


game()
