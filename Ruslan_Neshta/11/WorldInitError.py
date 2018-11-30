# defines WorldInitError
#

 
class WorldInitError(Exception):
    """
    Just a world initialization error
    """
    def __init__(self):
        message = 'Invalid world size'
        Exception.__init__(self, message)


if __name__ == "__main__":
    try:
        raise WorldInitError
    
    except WorldInitError as w:
        print(w)
