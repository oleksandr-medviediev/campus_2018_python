import json
import os.path

SAVE_FILE_NAME = "save.json"

def save_game_state(generated_map, player_position, map_size, bag, hp):
    """
    Saves current game state in json format to file with SAVE_FILE_NAME
    Rewrites the file
    :param generated_map: map of the game
    :param player_position: current player position
    :paramtype generated_map: list[list(str)]
    :paramtype player_position: tuple(int,int)
    :return: nothing
    :rtype: None
    """
    saved_objects = list()
    saved_objects.extend(generated_map)
    saved_objects.append(player_position)
    saved_objects.append(map_size)
    saved_objects.append(bag)
    saved_objects.append(hp)

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
        generated_map = objects_list[0:len(objects_list) - 4]
        player_position = objects_list[len(objects_list) - 4]
        map_size = objects_list[len(objects_list) - 3]
        bag = objects_list[len(objects_list) - 2]
        hp = objects_list[-1]

    return generated_map,player_position,map_size,bag,hp


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

