import time
import mss

from dirs import Dirs
from mode import Mode


def get_monitor() -> dict:
    with mss.mss() as sct:
        for monitor in sct.monitors:
            if monitor['width'] == 2560 and monitor['height'] == 1440:
                return monitor

        raise ValueError('Unable to find desired monitor')


def grab() -> None:
    monitor = get_monitor()

    monitor['top'] = monitor['top'] + 365
    monitor['left'] = monitor['left'] + 750
    monitor['width'] = 1040
    monitor['height'] = 585

    with mss.mss() as sct:
        shot = sct.grab(monitor)

    if shot is None:
        raise Exception('Unable to take screenshot')

    output = 'sct-{top}x{left}_{width}x{height}.png'.format(**monitor)
    # noinspection PyUnresolvedReferences
    mss.tools.to_png(shot.rgb, shot.size, output=output)


def main():
    mode = Mode()
    dirs = Dirs('img')

    while True:
        if mode.value == Mode.GRAB:
            grab()
        elif mode.value == Mode.ACCEPT or mode.value == Mode.DISMISS:
            dirs.move_items(mode)

        time.sleep(0.5)


if __name__ == '__main__':
    main()