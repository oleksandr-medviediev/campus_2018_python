from os.path import isfile
from pickle import dump
from pickle import load


_file_name = 'game_save.txt'


def game_load():

    save_data = None
    if isfile(_file_name):
        save_file = open(_file_name, 'rb')
        save_data = load(save_file)

    return save_data


def game_save(game_map):

    save_file = open(_file_name, 'wb')
    dump(game_map, save_file)