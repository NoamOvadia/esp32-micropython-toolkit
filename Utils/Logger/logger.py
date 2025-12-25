class Logger:

    INFO = 'INFO'
    DEBUG = 'DEBUG'
    WARNING = 'WARNING'
    ERROR = 'ERROR'

    def __init__(self, parent: str = ''):
        self.parent = parent

    def info(self, msg: str) -> None:

        if self.parent:
            msg_out = f'[{self.INFO}][{self.parent}]: {msg}'
        else:
            msg_out = f'[{self.INFO}]: {msg}'

        print(msg_out)

    def debug(self, msg: str) -> None:

        if self.parent:
            msg_out = f'[{self.DEBUG}][{self.parent}]: {msg}'
        else:
            msg_out = f'[{self.DEBUG}]: {msg}'

        print(msg_out)

    def warning(self, msg: str) -> None:

        if self.parent:
            msg_out = f'[{self.WARNING}][{self.parent}]: {msg}'
        else:
            msg_out = f'[{self.WARNING}]: {msg}'

        print(msg_out)

    def error(self, msg: str) -> None:

        if self.parent:
            msg_out = f'[{self.ERROR}][{self.parent}]: {msg}'
        else:
            msg_out = f'[{self.ERROR}]: {msg}'

        print(msg_out)