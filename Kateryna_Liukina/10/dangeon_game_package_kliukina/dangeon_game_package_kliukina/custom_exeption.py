class InvalidDirectionError(Exception):
     def __init__(self):
        super().__init__('Invalid direction. Type up/down/left/right.')

		
class InvalidMapSizeError(Exception):
    pass

	
class InvalidSaveDataError(Exception):
    def __init__(self):
        super().__init__('Invalid save data.')