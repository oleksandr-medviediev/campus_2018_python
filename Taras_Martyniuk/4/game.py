from DungeonMap import DungeonMap
from Player import Player
import DungeonMap as dm
from logging_defs import debug_logger as dlog, output_logger as olog
from serialization import save, load


player_moves = {
    'up' : (0, 1),
    'right' : (1, 0),
    'down' : (0, -1),
    'left' : (-1, 0)
}

PLAYER_HP = 3
TREAUSURES_FOR_WIN = 3


def play_game(size):
    dmap = DungeonMap(size)
    player = Player(TREAUSURES_FOR_WIN, dmap)

    start = dmap.get_random_empty_tile()
    dlog.debug(f'Starting at {start}')

    olog.info('Note: you can input \'save\' any time to save the game, or \'load\' to load last saved one')
    player.position = start
    while True:
        assert dmap.in_bounds(player.position)
        # uncomment for perfect debug experience
        # print(dm.map_to_str(dmap, player_pos))
        olog.info(f'you stand at the tile {player.position}')

        if dmap.is_trap_nearby(player.position):
            olog.info("Careful! There's a trap nearby!")

        if dmap.is_treasure_nearby(player.position):
            olog.info("There's a treasure right next to you! Eyes on the prize!")

        input_result = handle_user_input(player)

        if input_result == Save:
            save(dmap, player)
            olog.info('Saved your game!\n')
            continue

        elif input_result == Load:
            try:
                dmap, player = load()
                dlog.debug('changed state to loaded:')
                olog.info('Loaded your game!\n')
            except FileNotFoundError:
                dlog.debug('Tried to load when savefile does not exist')
                olog.info('You haven\'t saved it yet!')
            continue

        tile_type = dmap.at(player.position)
        if tile_type == dm.Treasure:
            win(dmap, player.position)
            break

        if tile_type == dm.Trap:
            lose(dmap, player.position)
            break

        olog.info('\n')


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


def win(dmap, end_pos):
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
    print(dmap.map_to_str(end_pos))


def lose(dmap, end_pos):
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
    print(dmap.map_to_str(end_pos))


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

