import inspect
import os
import subprocess
import sys
from sys import platform as _platform

from tqdm import tqdm

# import ui_loader


def module_path():
    # return os.path.dirname(inspect.getfile(ui_loader))
    return os.getcwd() + "/ui_interfaces/"


class Loader:
    def __init__(self, path="./"):
        self.path = path
        self.count = True
        print("Loading UIs at : {0}".format(self.path))
        self.update_Ui_Interfaces()

    def update_Ui_Interfaces(self):
        repository = self.path
        uipathes = sorted([f for f in os.listdir(repository) if f.endswith(".ui")])
        if not _platform == "linux" or _platform == "linux2":
            for f in tqdm(uipathes):
                pyfilename = f.split(".ui")[0] + "_ui_mod.py"
                command = ["pyuic5.bat", "-x", f, "-o", pyfilename]
                query = subprocess.Popen(
                    command,
                    cwd=repository,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                (out_txt, error) = query.communicate()
                out_txt = out_txt.decode("utf-8")
        else:
            for f in tqdm(uipathes):
                pyfilename = f.split(".ui")[0] + "_ui_mod.py"
                command = ["pyuic5", "-x", f, "-o", pyfilename]
                query = subprocess.Popen(
                    command,
                    cwd=repository,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                (out_txt, error) = query.communicate()
                out_txt = out_txt.decode("utf-8")


Loader(path=module_path())
