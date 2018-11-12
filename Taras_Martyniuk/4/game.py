import dungeon_map as dm
from logging_defs import debug_logger as dlog, output_logger as olog
from serialization import save, load


player_moves = {
    'up' : (0, 1),
    'right' : (1, 0),
    'down' : (0, -1),
    'left' : (-1, 0)
}


def play_game(size):
    dmap = dm.create_map(size)

    start = dm.get_random_empty_tile(dmap)
    dlog.debug(f'Starting at {start}')

    olog.info('Note: you can input \'save\' any time to save the game, or \'load\' to load last saved one')

    player_pos = start
    while True:
        assert dm.in_bounds(dmap, player_pos)
        # uncomment for perfect debug experience
        # print(dm.map_to_str(dmap, player_pos))
        olog.info(f'you stand at the tile {player_pos}')

        if dm.is_trap_nearby(dmap, player_pos):
            olog.info("Careful! There's a trap nearby!")

        if dm.is_treasure_nearby(dmap, player_pos):
            olog.info("There's a treasure right next to you! Eyes on the prize!")

        input_result = handle_user_input(dmap, player_pos)

        if input_result == Save:
            save(dmap, player_pos)
            olog.info('Saved your game!\n')
            continue

        elif input_result == Load:
            try:
                dmap, player_pos = load()
                dlog.debug('changed state to loaded:')
                olog.info('Loaded your game!\n')
            except FileNotFoundError:
                dlog.debug('Tried to load when savefile does not exist')
                olog.info('You haven\'t saved it yet!')
            continue

        player_pos = input_result

        tile_type = dm.at(dmap, player_pos)
        if tile_type == dm.Treasure:
            win(dmap, player_pos)
            break

        if tile_type == dm.Trap:
            lose(dmap, player_pos)
            break

        olog.info('\n')


def handle_user_input(dmap, curr_pos):
    '''
        continuesly gets the command from user
        for move, also simulates the position change
        move command can be rejected (player re-prompted) if it would move player out of the map

        :param dmap: dungeon map
        :param curr_pos: tile player stands at

        :returns 
            Save if save command was issued
            Load is load command was issued
            Simulated position after moving if move command was issued 
    '''
    while True:
        command = parse_user_input()

        if command == Save or command == Load:
            return command

        delta = command
        dlog.debug(f'trying to move by delta of {delta}')
        simulated_pos = (curr_pos[0] + delta[0], curr_pos[1] + delta[1])
        dlog.debug(f'trying to move to {simulated_pos}')

        if dm.in_bounds(dmap, simulated_pos):
            dlog.debug(f'moved to {simulated_pos}')
            return simulated_pos
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
    olog.info(dm.map_to_str(dmap, end_pos))


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
    olog.info(dm.map_to_str(dmap, end_pos))


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

