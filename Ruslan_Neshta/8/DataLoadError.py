# defines DataLoadError


class DataLoadError(Exception):
    """
    Loading data error
    """

    def __init__(self):
        message = 'Invalid file'
        Exception.__init__(self, message)


if __name__ == "__main__":
    try:
        raise DataLoadError
    
    except DataLoadError as d:
        print(d)
