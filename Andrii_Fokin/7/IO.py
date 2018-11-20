from os.path import isfile
from pickle import dump
from pickle import load
from dg_decorators import decorator_start_end_logging


_file_name = 'game_save.txt'


@decorator_start_end_logging
def game_load():

    save_data = None
    if isfile(_file_name):
        save_file = open(_file_name, 'rb')
        save_data = load(save_file)

    return save_data


@decorator_start_end_logging
def game_save(saving_data):

    save_file = open(_file_name, 'wb')
    dump(saving_data, save_file)