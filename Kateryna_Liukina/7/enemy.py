from Game_logger import log_decorator, debug_decorator, logger
import time
import random

    
class Enemy:
    
    direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    moving_interval = 3
	
    @log_decorator
    @debug_decorator
    def __init__(self, game_map_):
        self.position = game_map_.generate_coordinates()
        self._is_alive = True
    
	
    @log_decorator
    @debug_decorator
    def run_logic(self, game_map_, player_):
    
        while True:
        
            time.sleep(self.moving_interval)
            
            moving_direction = random.choice(self.direction)
            self.position[0] += moving_direction[0]
            self.position[1] += moving_direction[1]
            
            self.position[0] = max(0, min(self.position[0], game_map_.size[0] - 1))
            self.position[1] = max(0, min(self.position[1], game_map_.size[1] - 1))
            
            if self.position == player_.position:
            
                player_.hp -= 1
                self.position = game_map_.generate_coordinates()
                logger.warning("Enemy hit player")
