import os


class Mode:
    STOP: int = 0
    GRAB: int = 1
    ACCEPT: int = 2
    DISMISS: int = 4

    def __init__(self):
        self.value = Mode.STOP
        self.last = Mode.STOP

    def update(self) -> int:
        var_name = 'ED_SCREENSHOT_MODE'
        if var_name not in os.environ:
            os.environ.setdefault(var_name, f'{Mode.STOP}')

        try:
            mode = int(os.environ.get('ED_SCREENSHOT_MODE'))
        except ValueError:
            print(f'Invalid mode (found `{os.environ.get(mode)}` of type {type(mode)}. '
                  f'Defaulting to STOP ({Mode.STOP})')
            mode = Mode.STOP

        # Handle: mode is not power of 2
        if (mode & (mode-1) == 0) and mode != 0:
            mode = Mode.STOP

        self.value = mode
        return self.value

    def __str__(self):
        for k, v in Mode.__dict__.items():
            if v == self.value:
                return k

        return f'{self.value} (Unknown)'

    def __repr__(self):
        return f'Val: {self.value} ({self.__str__()})'
