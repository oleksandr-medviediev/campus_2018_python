import my_config
from my_game_flow import MyGameFlow

my_config.enable_logging()
my_config.enable_debug()

game_flow = MyGameFlow()

game_flow.init_game()
game_flow.run_game()
