from time import time
import dungeon_logger


file_debug_enabled = True
file_time_debug_enabled = False
console_debug_enabled = False


def debug_decor(func):
    
    def debug_wrapper(*args, **kwargs):

        result = 1
        if file_debug_enabled == False and console_debug_enabled == False:
            
            result = func(*args, **kwargs)
            
        elif file_debug_enabled:

            if console_debug_enabled:

                dungeon_logger.logger.info(f"{func.__name__}, args = {args}: began")
                dungeon_logger.logger.debug(f"{func.__name__}, args = {args}: began")
                result = func(*args, **kwargs)
                dungeon_logger.logger.debug(f'{func.__name__}, args = {args}: finished')
                dungeon_logger.logger.info(f'{func.__name__}, args = {args}: finished')

            else:

                dungeon_logger.logger.debug(f"{func.__name__}, args = {args}: began")
                result = func(*args, **kwargs)
                dungeon_logger.logger.debug(f'{func.__name__}, args = {args}: finished')

        return result

    return debug_wrapper


def debug_time_decor(func):

    def time_wrapper(*args, **kwargs):

        if file_time_debug_enabled == False and console_debug_enabled == False:
            
            result = func(*args, **kwargs)

        elif file_time_debug_enabled:

            if console_debug_enabled:
                
                start_time = time()
                result = func(*args, **kwargs)
                dungeon_logger.logger.debug(f'function time: {time() - start_time}')
                dungeon_logger.logger.info(f'function time: {time() - start_time}')

            else:

                start_time = time()
                result = func(*args, **kwargs)
                dungeon_logger.logger.debug(f'function time: {time() - start_time}')
            
        return result

    return time_wrapper
        

