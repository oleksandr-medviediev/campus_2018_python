from random import shuffle
from random import randint


game_entities = {'cell': '-', 'trap': '#', 'treasure':'X', 'player':'I', 'path':'+'}
treasure_inverse_rate = 20
trap_inverse_rate = 10
generated_map = []


def generate_characters_list(map_square):
    """
    generates list of characters except player in random order
    :param: square of map
    :paramtype: int
    :return: list of characters
    :rtype:list(string)
    """
    treasures_count = map_square // treasure_inverse_rate
    trap_count = map_square // trap_inverse_rate

    empty_cells_count = map_square - (trap_count + treasures_count)

    map_filling = []
    map_filling.extend([game_entities['cell'] for count in range(empty_cells_count)])
    map_filling.extend([game_entities['trap'] for count in range(trap_count)])
    map_filling.extend([game_entities['treasure'] for count in range(treasures_count)])

    shuffle(map_filling)

    return map_filling


def spawn_player(map_filling,map_size_x):
    """
    randomly puts player on generated map
    :param: generated list of characters - map
    :paramtype: list(string)
    :return: player spawn position 
    :return type: (int,int)
    """
    is_empty_cell = False
    player_position = 0
    
    while not is_empty_cell:
        player_position = randint(0, len(map_filling) - 1)
        is_empty_cell = map_filling[player_position] in [game_entities['trap'],game_entities['treasure']]

    map_filling[player_position] = game_entities['player']

    player_start_position_x = player_position // map_size_x
    player_start_position_y = player_position % map_size_x

    return player_start_position_x,player_start_position_y
    

def generate_map(map_size_x,map_size_y):                
    """
    transforms list of characters to matrix - list of lists
    :param map_size_x: number of columns
    :param map_size_y: number of rows
    :paramtype map_size_x, map_size_y: int
    :return: player position 
    :return type: (int,int)
    """
    map_square = map_size_x*map_size_y

    map_characters_list = generate_characters_list(map_square)

    start_pos_x,start_pos_y = spawn_player(map_characters_list,map_size_x)

    generated_map.extend([map_characters_list[i*map_size_x:(i+1)*map_size_x] for i in range(map_size_y)])

    return start_pos_x,start_pos_y

def print_map():
    """
    prints map
    :param generated_map: map of characters list of lists
    :paramtype generated_map: list(list(string))
    :return: nothing
    :return type: None
    """
    for row in generated_map:
        print(''.join(row))


if __name__ == '__main__':

    generate_map(10,8)
    print_map()

