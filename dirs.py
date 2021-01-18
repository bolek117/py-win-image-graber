import os
import shutil

from mode import Mode


class Dirs:
    def __init__(self, base_dir: str):
        self.base_dir: str = os.path.abspath(base_dir)
        del base_dir

        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)

        self.temp: str = os.path.join(self.base_dir, 'uncertain')
        self.false_pos = os.path.join(self.base_dir, 'false_pos')
        self.true_pos = os.path.join(self.base_dir, 'true_pos')

        # Init directories if not exists
        dirs = [self.base_dir, self.temp, self.false_pos, self.true_pos]
        for d in dirs:
            if not os.path.exists(d):
                os.mkdir(d)

        # Cleanup unused files from last session
        orphaned_files = os.listdir(self.temp)
        for f in orphaned_files:
            os.remove(os.path.join(self.temp, f))

    def move_items(self, mode: Mode) -> None:
        target_dir = self.true_pos if mode.value == Mode.ACCEPT \
            else self.false_pos

        files = os.listdir(self.temp)
        for f in files:
            shutil.move(os.path.join(self.temp, f), target_dir)