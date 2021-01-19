import os


class Mode:
    STOP: int = 0
    GRAB: int = 1
    ACCEPT: int = 2
    DISMISS: int = 4

    def __init__(self):
        self.__mode = Mode.STOP
        self.last = Mode.STOP

        self.__var_name = 'mode'

    def update(self) -> int:
        with open('config.ini', 'r') as f:
            for line in f:
                if line.startswith(self.__var_name):
                    _, mode = line.split('=')

                    mode = self.__parse_mode(mode)
                    if self.__mode == mode:
                        return self.__mode

                    self.set(mode)
                    return self.__mode

        # Failsafe
        self.set(Mode.STOP)
        return Mode.STOP

    def __str__(self):
        for k, v in Mode.__dict__.items():
            if v == self.get_mode():
                return k

        return f'{self.__mode} (Unknown)'

    def __repr__(self):
        return f'Val: {self.get_mode()} ({self.__str__()})'

    def __parse_mode(self, mode: int) -> int:
        default_value = Mode.STOP

        try:
            mode = int(mode)
        except ValueError:
            print(f'Unable to cast to int (found `{mode}` of type {type(mode)}). Defaulting')
            return default_value

        return mode

    def set(self, mode):
        mode = self.__parse_mode(mode)

        content = [
            '[ed]\r\n',
            f'mode={mode}'
        ]

        with open('config.ini', 'w') as f:
            f.writelines(content)

        self.__mode = mode

    def get_mode(self) -> int:
        values = Mode.__dict__.values()
        for v in values:
            if v == self.__mode:
                return v

        # Failsafe
        self.set(Mode.STOP)
        return self.get_mode()
