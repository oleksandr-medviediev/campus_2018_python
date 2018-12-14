from threading import Event
from threading import Thread
from player_input import player_input
from custom_logger import logger as log
from enemy import enemy
from time import sleep
from game_terrain import game_terrain
from random import choice
from character import character
from custom_exception import PlayerInputError
from save_load import save_game
from save_load import load_game

WALL = '⏹'


class GameLoop:
    def __init__(self):
        self.game_over_event = Event()

    def loop(self):

        enemy_update = Thread(target=self.move_enemy, name="enemy's thread")
        player_input_update = Thread(
            target=self.perform_player_action, name="player input thread")

        player_input_update.start()
        enemy_update.start()

        player_input_update.join()
        enemy_update.join()

    def clear(self):
        self.game_over_event.clear()

    def is_over(self):
        return self.game_over_event.is_set()

    def move_enemy(self):
        while not self.is_over():
            move = choice(enemy.moves)
            while game_terrain.terrain[enemy.position[0] + move[0]][
                                       enemy.position[1] + move[1]] == '⏹':
                move = choice(enemy.moves)

            game_terrain.terrain[enemy.position[0]][
                                 enemy.position[1]] = enemy.previous_cell
            enemy.position[0] += move[0]
            enemy.position[1] += move[1]
            enemy.previous_cell = game_terrain.terrain[enemy.position[0]][
                                                       enemy.position[1]]

            if enemy.position[0] == character.position[0] and enemy.position[1] == character.position[1]:
                character.current_hp -= 1
                log.info(
                    f"You've found a {'👾'} \n{character.current_hp} / 3 hp")
                game_terrain.respawn_enemy()
                if character.current_hp == 0:
                    self.game_over_event.set()
                    log.info("\nyou lost \n press any button")
            else:
                game_terrain.terrain[enemy.position[0]][
                                     enemy.position[1]] = '👾'
            log.info("enemy moved somewhere")
            
            x = enemy.position[0]
            y = enemy.position[1]

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if game_terrain.terrain[i][j] == '웃':
                        log.info("enemy is near")
            sleep(3)

    def perform_player_action(self):
        while not self.is_over():
            log.info("enter your action :")
            log.info(player_input.player_actions)
            action = input()

            new_player_position = list(character.position)

            try:
                if action in player_input.player_actions:
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
                        game_terrain.terrain[character.position[0]
                                             ][character.position[1]] = '🟋'
                        character.position = new_player_position
                        game_terrain.terrain[character.position[0]
                                             ][character.position[1]] = '웃'
                    elif game_terrain.terrain[new_player_position[0]][new_player_position[1]] == '◉':
                        character.current_hp -= 1
                        log.info(
                            f"You've found a trap ◉ \n{character.current_hp} / 3 hp")
                        game_terrain.terrain[character.position[0]
                                             ][character.position[1]] = '🟋'
                        character.position = new_player_position
                        game_terrain.terrain[character.position[0]
                                             ][character.position[1]] = '웃'
                    else:
                        game_terrain.terrain[character.position[0]
                                             ][character.position[1]] = '🟋'
                        character.position = new_player_position
                        game_terrain.terrain[character.position[0]
                                             ][character.position[1]] = '웃'

                    if character.current_hp == 0:
                        self.game_over_event.set()
                        log.info("\nyou lost you lost \n press any button")
                    elif character.current_backpack == 3:
                        self.game_over_event.set()
                        log.info("\nyou won")
                else:
                    raise PlayerInputError(action)
            except:
                log.info("wrong input")
            finally:
                player_input.print_state()


game_loop = GameLoop()
