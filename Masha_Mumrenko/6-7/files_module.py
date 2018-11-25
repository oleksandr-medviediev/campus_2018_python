import json
import os.path

SAVE_FILE_NAME = "save.json"

def save_game_state(generated_map, player_position, map_size, bag, hp, name, enemy_position):
    """
    Saves current game state in json format to file with SAVE_FILE_NAME
    Rewrites the file
    :param generated_map: map of the game
    :param player_position: current player position
    :param enemy_position: current enemy position
    :paramtype generated_map: list[list(str)]
    :paramtype player_position: tuple(int,int)
    :paramtype enemy_position: tuple(int,int)
    :return: nothing
    :rtype: None
    """
    saved_objects = list()
    saved_objects.extend(generated_map)
    saved_objects.append(player_position)
    saved_objects.append(map_size)
    saved_objects.append(bag)
    saved_objects.append(hp)
    saved_objects.append(name)
    saved_objects.append(enemy_position)

    with open(SAVE_FILE_NAME, 'w') as outfile:
        json.dump(saved_objects,outfile)


def load_game():
    """
    Loads saved game state from file with SAVE_FILE_NAME
    :return: saved game map and player position
    :rtype: list[list(str)], tuple(int,int)
    """
    with open(SAVE_FILE_NAME,'r') as infile:
        objects_list = json.load(infile)
        generated_map = objects_list[0:len(objects_list) - 6]
        player_position = objects_list[len(objects_list) - 6]
        map_size = objects_list[len(objects_list) - 5]
        bag = objects_list[len(objects_list) - 4]
        hp = objects_list[len(objects_list) - 3]
        name = objects_list[len(objects_list) - 2]
        enemy_position = objects_list[-1]

    return generated_map, map_size, player_position, bag, hp, name, enemy_position


def check_loading():
    """
    Checks that saved game exists in file with SAVE_FILE_NAME name
    :return: if file to load exists
    :rtype: bool
    """
    can_be_loaded = False
    if os.path.isfile(SAVE_FILE_NAME):
        can_be_loaded = True

    if not can_be_loaded:
        logger.logging_object.error("No saved file ")

    return can_be_loaded

