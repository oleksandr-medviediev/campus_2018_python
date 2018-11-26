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


class StateError(Exception):
    """
    Exception is being raised when state is not allowed in
    this context or there is no handler.
    """
    def __init__(self, message, handled_states):
        self.message = message
        self.handled_states = handled_states
