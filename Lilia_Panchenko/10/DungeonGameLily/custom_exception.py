class MyError(Exception):
	"""
	Common custom error class for DungeonGame project
	"""
	def __init__(self, message):
		"""Constructor for MyError class"""
		self.message = message

	def __str__(self):
		return self.message


class MapSizeError(MyError):
	"""
	Exception class. This exception raises if player inputed something wrong as a game map size (integer less than 8,
	for example, or non-integer value)
	"""
	pass


class PlayerInputError(MyError):
	"""
	Exception class. This exception raises if player inputed something wrong as his next game choice.
	"""
	def __init__(self, value):
		"""Constructor for PlayerInputError class"""
		self.message = "Player inputed: " + str(value)


class PlayerNameError(MyError):
	"""
	Exception class. This exception raises if player inputed space, newline or tab as name.
	"""
	def __init__(self, value):
		"""Constructor for PlayerNameError class"""
		self.message = "Player inputed as name: " + value
