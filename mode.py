class Mode:
    STOP: int = 0
    GRAB: int = 1
    ACCEPT: int = 2
    DISMISS: int = 4

    def __init__(self):
        self.value = Mode.STOP
        self.last = Mode.STOP