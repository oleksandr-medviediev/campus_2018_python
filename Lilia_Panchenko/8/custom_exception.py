class MyError(Exception):
	"""common custom error class"""
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message


class MapSizeError(MyError):
	pass


class PlayerInputError(MyError):
	def __init__(self, value):
		self.message = "Player inputed: " + str(value)


class PlayerNameError(MyError):
	def __init__(self, value):
		self.message = "Player inputed as name: " + value
