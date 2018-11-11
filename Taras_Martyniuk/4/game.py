import dungeon_map as dm
from logging_defs import debug_logger as dlog, output_logger as olog
# from logging_defs import output_logger as olog

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

        player_pos = move_player_in_bounds(player_pos, dmap)
        dlog.debug(f'moved to {player_pos}')

        tile_type = dm.at(dmap, player_pos)
        if tile_type == dm.Treasure:
            win(dmap, player_pos)
            break

        if tile_type == dm.Trap:
            lose(dmap, player_pos)
            break


def move_player_in_bounds(curr_pos, dmap):
    '''
        prompts player to input move command
        until the resulting position will be in bounds

        :param curr_pos: Tile player is at currently
        :param dmap: dungeon map
        :returns: Tile where player is after simulating move - guaranteed to be in bounds
    '''
    while True:
        moved_to_check = move_player(curr_pos)
        dlog.debug(f'trying to move to {moved_to_check}')

        if dm.in_bounds(dmap, moved_to_check):
            return moved_to_check
        else:
            olog.info("Can't move there - a wall blocks the path")
            

def move_player(curr_pos):
    '''
        prompts player to enter move direction,
        validates it, and returns moved position

        :param curr_pos: tile where player is now
        :returns: Tile where the player is after simulating a move (can be out of bounds)
    '''
    while True:
        move = input('Where to go? ')
        if move not in player_moves:
            olog.info(f'Sorry, you can go only: {", ".join(player_moves.keys())}')
            continue

        delta = player_moves[move]
        dlog.debug(f'trying to move by delta of {delta}')
        return (curr_pos[0] + delta[0], curr_pos[1] + delta[1])


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

