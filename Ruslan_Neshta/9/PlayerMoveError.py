# defines PlayerMoveError
#

 
class PlayerMoveError(Exception):
    """
    Just a world initialization error
    """
    def __init__(self):
        message = 'Player can\'t move in this direction'
        Exception.__init__(self, message)


if __name__ == "__main__":
    try:
        raise PlayerMoveError
    
    except PlayerMoveError as p:
        print(p)
