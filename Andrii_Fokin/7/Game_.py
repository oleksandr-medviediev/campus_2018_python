import Player
import Map_
import dg_decorators

from IO import game_save
from IO import game_load


class Game:

    _player_move_comand = { 1:'Up', 2:'Dawn', 3:'Right', 4:'Left', 5:'Save game'}


    @dg_decorators.decorator_start_end_logging
    def __init__(self):
        self.player = Player.Player()
        self.map_ = Map_.Map_(10)

        self.player.position = self.map_.get_free_cell()


    @dg_decorators.decorator_start_end_logging
    def loop(self):

        self._print_the_spawn_location()
        while self.player.HP > 0 and self.player.score < 3:
            self._spell_game_state()
            players_action = self._player_input()

            if players_action in Player.move_types:
                self.player.move(players_action)
                self._proscess_player_move()
            elif players_action == 'Save game':
                self.save()

        else:
            print(f'You {"Won" if self.player.score == 3 else "Lose"}')
            self.map_.set_cell_type(self.player.position, self.map_.cell_player)
            print(self)


    @dg_decorators.decorator_start_end_logging
    def save(self):
        save_data = [self.map_, self.player]
        game_save(save_data)


    @dg_decorators.decorator_start_end_logging
    def load(self):
        save_data = game_load()
        self.map_ = save_data[0]
        self.player = save_data[1]


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
        top_left_cell = [cord - 1 for cord in self.player.position]
        location = []
        for i in range(3):
            y =  top_left_cell[1] + i
            location.append([self.map_.get_cell_type([top_left_cell[0] + j, y]) for j in range(3)])
        
        location[1][1] = self.map_.cell_player
        print(*[f'\n{line}' for line in location[::-1]], '\n----------')


    @dg_decorators.decorator_start_end_logging
    def _spell_game_state(self):

        for val in Player.move_types.values():
            y = self.player.position[1] + val[1]
            x = self.player.position[0] + val[0]
            cell_type = self.map_.field[y][x]

            if cell_type == self.map_.cell_trap:
                print('Trap is near')
            elif cell_type == self.map_.cell_treasure:
                print('Treasure is near')


    @dg_decorators.decorator_start_end_logging
    def __str__(self):
        return f'Player:\n{self.player}\n\nMap:\n{self.map_}\n'