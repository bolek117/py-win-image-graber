import os


class Mode:
    STOP: int = 0
    GRAB: int = 1
    ACCEPT: int = 2
    DISMISS: int = 4

    def __init__(self):
        self.__mode = Mode.STOP
        self.last = Mode.STOP

        self.__var_name = 'ED_SCREENSHOT_MODE'

    def update(self) -> int:
        if self.__var_name not in os.environ:
            os.environ.setdefault(self.__var_name, f'{Mode.STOP}')

        mode = os.environ.get(self.__var_name)
        self.set(mode)
        return self.get_mode()

    def __str__(self):
        for k, v in Mode.__dict__.items():
            if v == self.get_mode():
                return k

        return f'{self.__mode} (Unknown)'

    def __repr__(self):
        return f'Val: {self.get_mode()} ({self.__str__()})'

    @staticmethod
    def __parse_mode(mode: int) -> int:
        default_value = Mode.STOP

        try:
            mode = int(mode)
        except ValueError:
            print(f'Unable to cast to int (found `{mode}` of type {type(mode)}). Defaulting')
            return default_value

        return mode

    def set(self, mode):
        mode = self.__parse_mode(mode)
        os.environ[self.__var_name] = f'{mode}'
        self.__mode = mode

    def get_mode(self) -> int:
        values = Mode.__dict__.values()
        for v in values:
            if v == self.__mode:
                return v

        self.set(Mode.STOP)
        return self.get_mode()
