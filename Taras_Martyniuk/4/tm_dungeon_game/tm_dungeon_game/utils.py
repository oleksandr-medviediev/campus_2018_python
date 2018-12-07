player_moves = {
    'up' : (0, 1),
    'right' : (1, 0),
    'down' : (0, -1),
    'left' : (-1, 0)
}

move_directions = list(player_moves.values())

def tuple_add(left, right):
    '''
        adds 2 2D tuples elementwise
    '''
    return (left[0] + right[0], left[1] + right[1])


def tuple_diff(left, right):
    '''
        subtracts 2 2D tuples elementwise
    '''
    return (left[0] - right[0], left[1] - right[1])


def repeat(func, times):
    '''
        runs func times amount of times
        :param func: function
        :param times: int
    '''
    for i in range(times):
        func()
    