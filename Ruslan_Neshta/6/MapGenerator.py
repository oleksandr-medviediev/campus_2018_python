from random import randint
from DungeonLogger import debugger_output


@debugger_output()
def fill_the_map(world, size, amount_of_items, item):
    """
    Fills map with given amount of items

    :param world: map to fill
    :param size: maps size
    :param amount_of_items: amount of items to spawn
    :param item: item to spawn
    :return: nothing
    :rtype: None
    """

    i = 0
    while i < amount_of_items:
        x = randint(0, size - 1)
        y = randint(0, size - 1)

        if world[x][y] == item:
            continue

        else:
            world[x][y] = item
            i += 1


@debugger_output()
def generate(size, empty=' ', trap='#', treasure='@'):
    """
    Generates map: size per size squares with size*size / 10 traps and size*size / 20 treasures

    :param size: number of squares
    :param empty: string that defines empty field
    :param trap: string that defines trap
    :param treasure: string that defines treasure
    :return: map with traps and treasures
    :rtype: list
    """

    world = [[empty for _ in range(size)] for _ in range(size)]

    amount_of_traps = size * size / 10
    amount_of_treasures = size * size / 20

    fill_the_map(world, size, amount_of_traps, trap)
    fill_the_map(world, size, amount_of_treasures, treasure)

    return world


if __name__ == "__main__":
    game_map = generate(3)
    print(game_map)

    game_map = generate(5)
    print(game_map)

    game_map = generate(10)
    print(game_map)

    game_map = generate(15)
    print(game_map)
