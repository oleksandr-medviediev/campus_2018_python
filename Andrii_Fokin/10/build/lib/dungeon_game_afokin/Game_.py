from threading import Event
from threading import Thread
from time import sleep

import Player
import Map_
import Enemy

from tools import dg_decorators
from tools.IO import game_save
from tools.IO import game_load
from tools.dg_exсeptios import LoadGameError
from tools.dg_exсeptios import OutOfMapRangeError
from tools.dg_logging import DG_loger as log


class Game:

    _player_move_comand = { 1:'Up', 2:'Dawn', 3:'Right', 4:'Left', 5:'Save game', 6:'Quite'}


    @dg_decorators.decorator_start_end_logging
    def __init__(self):
        self.player = Player.Player()
        self.map_ = Map_.Map_(10)
        self.enemy = Enemy.Enemy()
        self.__game_end_event = Event()

        self.player.position = self.map_.get_free_cell()
        self.enemy.position = self.map_.get_free_cell()


    @dg_decorators.decorator_start_end_logging
    def loop(self):

        self._print_the_spawn_location()

        enemy_updater = Thread(target= self.__enemy_update)
        player_updater = Thread(target=self.__player_update)

        player_updater.start()
        enemy_updater.start()

        player_updater.join()
        self.__game_end_event.set()
        enemy_updater.join()


    @dg_decorators.decorator_start_end_logging
    def save(self):
        save_data = [self.map_, self.player]
        game_save(save_data)


    @dg_decorators.decorator_start_end_logging
    def load(self):
        save_data = game_load()

        if len(save_data) == 2 and isinstance(save_data[0], Map_.Map_) and isinstance(save_data[1], Player.Player):
            self.map_ = save_data[0]
            self.player = save_data[1]
        else:
            raise LoadGameError("Incorect data in save file")


    @dg_decorators.decorator_start_end_logging
    def _player_input(self):
        print(f"Your action : {[f'{key} - {val},' for key, val in self._player_move_comand.items()]}")
        action_type = int(input('-> '))

        result = self._player_move_comand[action_type]
        return result


    @dg_decorators.decorator_start_end_logging
    def _proscess_player_move(self):

        sell_type = self.map_.get_cell_type(self.player.position)
        if sell_type == self.map_.cell_treasure:
            self.map_.set_cell_type(self.player.position, self.map_.cell_free)
            self.player.score += 1
        elif sell_type == self.map_.cell_trap:
            self.map_.set_cell_type(self.player.position, self.map_.cell_free)
            self.player.HP -= 1
        elif sell_type == self.map_.cell_border:
            print("Wow look like wall. Try another way")
            self.player.undo_move()


    @dg_decorators.decorator_start_end_logging
    def _print_the_spawn_location(self):
        top_left_cell = [(cord - 1) for cord in self.player.position]
        location = []
        for i in range(3):
            y =  top_left_cell[1] + i
            location.append([self.map_.get_cell_type([(top_left_cell[0] + j), y]) for j in range(3)])
        
        location[1][1] = self.map_.cell_player
        print(*[f'\n{line}' for line in location[::-1]], '\n----------')


    @dg_decorators.decorator_start_end_logging
    def _spell_game_state(self):

        for val in self.player.move_types.values():
            y = self.player.position[1] + val[1]
            x = self.player.position[0] + val[0]
            cell_type = self.map_.field[y][x]

            if cell_type == self.map_.cell_trap:
                print('Trap is near')
            elif cell_type == self.map_.cell_treasure:
                print('Treasure is near')

            if self.enemy.position == [x, y]:
                print('Enemy is near')


    @dg_decorators.decorator_start_end_logging
    def __enemy_update(self):
        """
        Moving enemy while game_end event does not occur
        """
        while self.__game_end_event.is_set() == False and self.player.HP > 0:
            self.enemy.move()
            self.__proscess_enemy_move()
            sleep(0.1)


    @dg_decorators.decorator_start_end_logging
    def __player_update(self):
        while self.player.HP > 0 and self.player.score < 3:
            self._spell_game_state()
            try:
                players_action = self._player_input()
            except Exception:
                log.error('Incorect input')
            else:
                if players_action in self.player.move_types:
                    self.player.move(players_action)
                    self._proscess_player_move()
                elif players_action == 'Save game':
                    try:
                        self.save()
                    except Ellipsis as error:
                        log.error('Can not save game')
                        log.error(error)
                elif players_action == 'Quite':
                    return

        else:
            print(f'You {"Won" if self.player.score == 3 else "Lose"}')
            self.map_.set_cell_type(self.player.position, self.map_.cell_player)
            self.map_.set_cell_type(self.enemy.position, self.map_.cell_enemy)
            print(self)


    @dg_decorators.decorator_start_end_logging
    def __proscess_enemy_move(self):
        try:
            sell_type = self.map_.get_cell_type(self.enemy.position)
        except OutOfMapRangeError:
            self.enemy.position = self.map_.get_free_cell()

        else:
            if self.enemy.position == self.player.position:
                self.player.HP -= 1
                print("Enemy found you!!!!")
                self.enemy.position = self.map_.get_free_cell()

            if sell_type == self.map_.cell_border:
                self.enemy.undo_move()


    @dg_decorators.decorator_start_end_logging
    def __str__(self):
        return f'Player:\n{self.player}\n\nMap:\n{self.map_}\n'