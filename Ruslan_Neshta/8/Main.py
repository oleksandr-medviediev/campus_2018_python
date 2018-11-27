import View
import DungeonSaver
from Player import Player
from World import World
from DungeonLogger import main_logger
from DungeonLogger import debugger_output
from DataLoadError import DataLoadError


@debugger_output()
def handle_player_move(world, player):
    """
    Handles player movement accordingly tp user input

    :param world: world map
    :param player: player
    :rtype: None
    """

    player_move_fail = 'Player can\'t make this move'
    user_input_fail = 'Invalid input'
    user_input_prompt = 'Choose where you want to move:\n\'u\' - up,\n\'d\' - down,\n\'l\' - left,\n\'r\' - right.\n\
Input move:'

    moves = {'u' : player.up, 'd' : player.down, 'l' : player.left, 'r' : player.right}
    is_valid = False

    while not is_valid:
        main_logger.info(user_input_prompt)
        move = input()

        if move not in moves:
            main_logger.info(user_input_fail)
            continue

        is_valid = moves[move]()

        if is_valid:
            world.update_player_position(player)
        else:
            main_logger.info(player_move_fail)


@debugger_output()
def generate_warnings_if_required(world):
    """
    Generates warnings if required

    :param world: worlds map
    :param player_position: players position
    :param trap: defines trap
    :param treasure: defines treasure
    :return: nothing
    :rtype: None
    """

    is_trap = world.is_trap_near_player()
    is_treasure = world.is_treasure_near_player()

    View.warn_player(is_treasure, is_trap)


@debugger_output()
def play_game(game_save):
    """
    Starts Dungeon game

    :param game_save: saved game state(if any)
    :return: nothing
    :rtype: None
    """

    move_command = 'Move'
    save_command = 'Save'
    end_game_session = 'End'

    user_options = [move_command, save_command, end_game_session]
    user_prompt = '\n'.join(user_options)

    result = ''
    game_over = False

    game_world = World(10)
    size = game_world.size()

    game_world.fill_the_map(size*size / 10, World.trap)
    game_world.fill_the_map(size*size / 20, World.treasure)

    game_player = Player(game_world)
    hidden = [World.trap, World.treasure]

    if game_save != {}:
        game_world.load(game_save)
        game_player.load(game_save)
    
    while not game_over:

        world = game_world.print_except(hidden)

        main_logger.info(f'Player info:\n\thealth: {game_player.health} <3\n\ttreasures: {game_player.treasures}\n')
        main_logger.info(world)
        
        generate_warnings_if_required(game_world)
        main_logger.info(user_prompt)
        
        choice = input()
        if choice == move_command:
            handle_player_move(game_world, game_player)

        elif choice == save_command:
            objects = {}
            game_world.save(objects)
            game_player.save(objects)
            DungeonSaver.save_game(objects)

        elif choice == end_game_session:
            result = 'Game over'
            break

        else:
            main_logger.info('Invalid input')

        treasures = game_player.treasures
        health = game_player.health

        if treasures >= 3:
            game_over = True
            result = 'You captured 3 treasures! You won!'

        if health <= 0:
            game_over = True
            result = 'You have 0 health =/ You lose.'

    if game_over:
        main_logger.info(result)
        world = game_world.print()
        main_logger.info(world)


@debugger_output()
def main_menu():
    """
    Shows main menu and allows user to make choice

    :return: nothing
    :rtype: None
    """

    new_game = 'New'
    load_game = 'Load'
    exit_game = 'Exit'
    prompt = 'Choose one of options above:'
    save_not_found = 'There is no saved games'
    invalid_input = 'Invalid input'

    menu_items = [new_game, load_game, exit_game, prompt]
    quit_game = False

    while not quit_game:

        main_logger.info('\n'.join(menu_items))
        choice = input()

        if choice not in menu_items:
            main_logger.info(invalid_input)

        elif choice == new_game:
            save = {}
            play_game(save)

        elif choice == load_game:
            try:
                save = DungeonSaver.load_game()
                play_game(save)

            except FileNotFoundError:
                main_logger.info(save_not_found)
            
            except DataLoadError:
                main_logger.info('Saved game file has been corrupted')

        else:
            quit_game = True


if __name__ == "__main__":
    main_menu()
