import world

directions = {
    'w': [ 0, -1],
    'a': [-1,  0],
    's': [ 0,  1],
    'd': [ 1,  0]
}

world.create_world(10)
player_pos = world.spawn_player()

won = False
lose = False
while not (won or lose):
    if world.is_trap_around(player_pos):
        print('There is a trap within one square from you!')
    else:
        print('No traps around.')
    if world.is_treasure_around(player_pos):
        print('There is a treasure within one square from you!')
    else:
        print('No treasures around.')

    user_input = input('Your move (w/a/s/d)?')

    world.move_player(player_pos, directions[user_input])

    won = world.is_found_treasure(player_pos)
    lose = world.is_trapped(player_pos)

if won:
    print('You won!')
else:
    print('You lose!')

world.print_world(player_pos)


