from character import character
from custom_logger import logger as log
from save_load import save_game
from save_load import load_game
from game_terrain import game_terrain
from logger_decorator import debug_log_decorator

WALL = '⏹'


class PlayerInput:
    def __init__(self):
        self.player_actions = ('up', 'down', 'right', 'left', 'load', 'save')

    def perform_player_action(self):
        log.info("enter your action :")
        log.info(self.player_actions)
        action = input()

        new_player_position = list(character.position)

        result = True

        if action in self.player_actions:
            if action == 'up':
                new_player_position[0] -= 1
            elif action == 'down':
                new_player_position[0] += 1
            elif action == 'right':
                new_player_position[1] += 1
            elif action == 'left':
                new_player_position[1] -= 1
            elif action == 'save':
                save_game(game_terrain.terrain)
            elif action == 'load':
                game_terrain.terrain = load_game()

            if game_terrain.terrain[new_player_position[0]][new_player_position[1]] == WALL:
                log.info("you found the wall. Can't move further")
            elif game_terrain.terrain[new_player_position[0]][new_player_position[1]] == '⭐':
                character.current_backpack += 1
                log.info(
                    f"You've found a treasure ⭐ \n {character.current_backpack} / 3 total")
                game_terrain.terrain[character.position[0]][character.position[1]] = '🟋'
                character.position = new_player_position
                game_terrain.terrain[character.position[0]][character.position[1]] = '웃'
            elif game_terrain.terrain[new_player_position[0]][new_player_position[1]] == '◉':
                character.current_hp -= 1
                log.info(
                    f"You've found a trap ◉ \n{character.current_hp} / 3 hp")
                game_terrain.terrain[character.position[0]][character.position[1]] = '🟋'
                character.position = new_player_position
                game_terrain.terrain[character.position[0]][character.position[1]] = '웃'
            else:
                game_terrain.terrain[character.position[0]][character.position[1]] = '🟋'
                character.position = new_player_position
                game_terrain.terrain[character.position[0]][character.position[1]] = '웃'

            if character.current_hp == 0:
                result = False
                log.info("\nyou lost")
            elif character.current_backpack == 3:
                result = False
                log.info("\nyou won")
        else:
            log.info("wrong input")

        return result

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
