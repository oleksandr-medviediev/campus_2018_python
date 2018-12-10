from character import character
from custom_logger import logger as log
from game_terrain import game_terrain
from logger_decorator import debug_log_decorator



class PlayerInput:
    def __init__(self):
        self.player_actions = ('up', 'down', 'right', 'left', 'load', 'save')

    @debug_log_decorator
    def print_state(self):

        x = character.position[0]
        y = character.position[1]

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if game_terrain.terrain[i][j] == '⭐':
                    log.info("treasure is near")
                elif game_terrain.terrain[i][j] == '◉':
                    log.info("trap is near")
                


player_input = PlayerInput()
