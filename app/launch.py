from pywinauto.application import Application
from conf import Conf
import os


class Launch:
    def __init__(self, extract_dir):
        self.extract_dir = extract_dir

    def max_item(self):
        list_dir = os.listdir(self.extract_dir)
        return max(list_dir)

    def run_max(self):
        exe_path = self.extract_dir + self.max_item() + '\\Audacity.exe'
        exe = Application(backend="uia").start(exe_path)
        return exe

    def halt(self):
        pass



# if __name__ == '__main__':
#
#     # Launch the latest Audacity version in the directory
#     Launch(Conf.EXTRACT_DIR).run_max()
