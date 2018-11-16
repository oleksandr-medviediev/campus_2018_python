import functools
import logging
from Constants import DEBUG

def log_decorator_factory(logger):
	"""
	Function returns decorater that output debug info in logger
	Args:
		logger(logging.Logger): logger where logs will be printed
	Returns:
		 decorater that output debug info in logger
	"""
	def log_decorator(func):
		"""
		Decorator that returns wrapper that prints info in logger before and after start of the func
		Args:
			logger(logging.Logger): logger where logs will be printed
			func(function): function that will be decorated
		Returns:
			 wrapper that prints info in logger before and after start of the func
		"""
		@functools.wraps(func)
		def log_wrapper(*args, **kwargs):
			"""Prints info before and after start of the function"""		
			list_of_args = [str(arg) for arg in args]
			list_of_kwargs = [str(name) + ':' + str(arg) for name, arg in kwargs]

			debug_string = "Start of " + func.__name__ + " function with args: "\
						   + ','.join(list_of_args) + "; and kwargs: " + ','.join(list_of_kwargs)

			logger.log(logging.DEBUG, debug_string)

			result = func(*args, **kwargs)

			logger.log(logging.DEBUG, "End of " + func.__name__ + " function.")
			
			return result
		if DEBUG:
			return log_wrapper
		else:
			return func
	return log_decorator