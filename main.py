import os
import time
import mss
import uuid

from dirs import Dirs
from mode import Mode


def get_monitor() -> dict:
    with mss.mss() as sct:
        for monitor in sct.monitors:
            if monitor['width'] == 2560 and monitor['height'] == 1440:
                return monitor

        raise ValueError('Unable to find desired monitor')


def grab(output_dir: str) -> None:
    monitor = get_monitor()

    monitor['top'] = monitor['top'] + 365
    monitor['left'] = monitor['left'] + 750
    monitor['width'] = 1040
    monitor['height'] = 585

    with mss.mss() as sct:
        shot = sct.grab(monitor)

    if shot is None:
        raise Exception('Unable to take screenshot')

    monitor['id'] = uuid.uuid4()
    filename = 'sct-{top}x{left}_{width}x{height}-{id}.png'.format(**monitor)
    output_path = os.path.join(output_dir, filename)

    # noinspection PyUnresolvedReferences
    mss.tools.to_png(shot.rgb, shot.size, output=output_path)


def log(msg: str) -> None:
    print(f'[{time.time():.1f}] {msg}')


def main():
    mode = Mode()
    dirs = Dirs('img')

    while True:
        mode.update()
        log(f'Detected mode: {mode}')

        if mode.value == Mode.GRAB:
            log(f'Grabbing image to {dirs.temp} directory')
            grab(dirs.temp)
        elif mode.value == Mode.ACCEPT or mode.value == Mode.DISMISS:
            log('Moving items to target folder')
            dirs.move_items(mode)

        time.sleep(0.5)


if __name__ == '__main__':
    main()
