class ActionError(Exception):
    """
    Exception is being raised when unsupported action is detected.
    """
    def __init__(self, message, supported_actions):
        self.message = message
        self.supported_actions = supported_actions


class LogicalError(Exception):
    """
    Exception is being raised on logical inconsistencies.
    """
    def __init__(self, message):
        self.message = message
