import dungeon_map_generate
import dungeon_logic
import dungeon_serializer


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

        if command == 'save':
            dungeon_serializer.serialize_dungeon_game(dun_map, position)

        elif command == 'load':
            data = dungeon_serializer.deserialize_dungeon_game()
            dun_map = data[0]
            position = data[1]

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
    print("Use 'save' or 'load' commands to save/load game")

    game_state = 'ingame'
    while game_state == 'ingame':
        game_state = run_frame(dun_map, position)

    for row in dun_map:
        print(row)


game()
