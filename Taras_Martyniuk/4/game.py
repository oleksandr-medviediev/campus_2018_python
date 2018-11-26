from DungeonMap import DungeonMap
from Player import Player
import DungeonMap as dm
from logging_decors import log_decor, output_logger as olog, debug_file_console_logger as dlog
from serialization import save, load, save_exists
from utils import player_moves
from threading import Event
from Enemy import Enemy
from pickle import UnpicklingError


PLAYER_HP = 1
TREAUSURES_FOR_WIN = 1


@log_decor
def play_game(size):
    dmap = DungeonMap(size)

    player_dead = Event()
    player_won = Event()

    player = Player(TREAUSURES_FOR_WIN, dmap, lambda: player_dead.set())

    start = dmap.get_random_empty_tile()
    dlog.debug(f'Starting at {start}')

    olog.info('Note: you can input \'save\' any time to save the game, or \'load\' to load last saved one')
    player.position = start

    enemy = Enemy(dmap)
    enemy.start_patroling(player)

    print(dmap.map_to_str(player.position, enemy.position))

    while not player_dead.is_set() and not player_won.is_set():
        run_turn(player_dead, player_won, player, dmap)
        # uncomment for perfect debug experience
        print(dmap.map_to_str(player.position, enemy.position))

    enemy.stop_patroling()

    won = player_won.is_set()
    lost = player_dead.is_set()
    assert won != lost

    if won:
        win(dmap, player.position, enemy.position)
    else:
        assert lost
        lose(dmap, player.position, enemy.position)


@log_decor
def run_turn(death_event, win_event, player, dmap):
    '''
        notifies about object nearby, polls for input, applies the input
        if the player died, death_event is set,
        if he's won - win_event is set

        :param death_event, win_event: Events
        :param dmap: DungeonMap
        :param player: Player
    '''
    assert dmap.in_bounds(player.position)

    olog.info(f'you stand at the tile {player.position}')

    if dmap.is_trap_nearby(player.position):
        olog.info("Careful! There's a trap nearby!")

    if dmap.is_treasure_nearby(player.position):
        olog.info("There's a treasure right next to you! Eyes on the prize!")

    input_result = handle_user_input(player)

    if input_result == Save:
        try:
            save(dmap, player)
            olog.info('Saved your game!\n')
        except IOError:
            olog.info('could not write to save file. Maybe folder of the game is somewhere protected?')
            
        return

    elif input_result == Load:
        deserialized = handle_load()
        if deserialized is not None:
            dmap, player = deserialized
        return

    tile_type = dmap.at(player.position)
    if tile_type == dm.Treasure:
        assert player.treasures < TREAUSURES_FOR_WIN
        olog.info('The Treasure is yours!')
        player.add_treasure()

        if player.treasures >= TREAUSURES_FOR_WIN:
            win_event.set()
            return

    elif tile_type == dm.Trap:
        player.lose_health()

    olog.info('\n')


def handle_load():
    '''
        tries to load, telling user if the savefile does not exist
        :returns: tuple (dmap, player) - deserialized DungeonMap and Player
            or None if the load was unsuccessful
    '''
    if not save_exists():
        dlog.debug('Tried to load when savefile does not exist')
        olog.info('You haven\'t saved it yet!')
        return None

    try:
        deserialized = load()
        dlog.debug('changed state to loaded:')
        olog.info('Loaded your game!\n')

        return deserialized

    except UnpicklingError:
        olog.info('Could not load the save, savefile corrupted')
        return None



@log_decor
def handle_user_input(player):
    '''
        continuously gets the command from user
        for move, also simulates the position change
        move command can be rejected (player re-prompted) if it would move player out of the map
        in that case, user is reprompted until a valid command is issued

        :param player: Player

        :returns 
            Save if save command was issued
            Load is load command was issued
            None if move command was issued (and successfully simulated)
    '''
    while True:
        command = parse_user_input()

        if command == Save or command == Load:
            return command

        delta = command

        if player.try_move(delta):
            dlog.debug(f'moved to {player.position}')
            return None
        else:
            olog.info("Can't move there - a wall blocks the path")

        
Save, Load = range(2)


@log_decor
def parse_user_input():
    '''
        prompts player to issue a command,
        performs validation,
        the command might be : move, save and load

        :returns: player command, if it is Save/Load
            or move delta if command is to move
    '''
    while True:
        command = input('Where to go? ')
        if command.lower() == 'save':
            return Save

        if command.lower() == 'load':
            return Load

        if command in player_moves:
            return player_moves[command]
        else:
            olog.info(f'You can go only: {", ".join(player_moves.keys())}')


@log_decor
def win(dmap, player_end_pos, enemy_end_pos):
    '''
        prints win message
        :param dmap: dungeon map
        :param end_pos: Tile player stands at the time of game end
    '''
    olog.info('''Suddenly you trip over a treasure chest!
        The ideas on where to spend the goodies inside race thorugh your mind even as you fall!''')
    olog.info(TREASURE_ASCI)
    olog.info('---------------------------------------------------------')
    olog.info("Now look at all the traps you've evaded!")
    print(dmap.map_to_str(player_end_pos, enemy_end_pos))


@log_decor
def lose(dmap, end_pos, enemy_end_pos):
    '''
        prints lose message
        :param dmap: dungeon map
        :param end_pos: Tile player stands at the time of game end
    '''
    olog.info("You've got dismembered by some razory and hammery thingy!")
    olog.info("Happens to the best of us adventurers!")
    olog.info(BLOODY_SWORD_ASCI)
    olog.info('---------------------------------------------------------')
    olog.info("Now look at all the treasures you could've had for yourself!")
    print(dmap.map_to_str(end_pos, enemy_end_pos))


TREASURE_ASCI = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

BLOODY_SWORD_ASCI = '''
              .-.
              | |____________________________________________________
 _ _ _ _ _ _ _| |                                                  .'`.
|_|_|_|_|_|_|_| |-mbfh-------------------------------------------.'****>
`.            | |_______________________________________________.'***.'
  `.        .'| |                                               `**'
    `-.___.'  `-'                                              .'*`.
                                                               `._.' .
                                                               .   .'*`.
                                                             .'*`. `._.'
'''

