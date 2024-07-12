import os
import subprocess
import sys

from tqdm import tqdm

# update ui
"""
repository = os.getcwd()
uifilename = 'serenity.ui'
pyfilename = 'serenity_ui_mod.py'
print("#update uic")
command = ['pyuic5', '-x', uifilename, '-o', pyfilename]
query = subprocess.Popen(command, cwd=repository,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out_txt, error) = query.communicate()
out_txt = out_txt.decode("utf-8")
"""


def run():
    repository = os.getcwd()
    uipathes = sorted([f for f in os.listdir(repository) if f.endswith(".ui")])
    print(uipathes)
    for f in tqdm(uipathes):
        pyfilename = f.split(".ui")[0] + "_ui_mod.py"
        command = ["pyuic5.bat", "-x", f, "-o", pyfilename]
        query = subprocess.Popen(
            command, cwd=repository, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        (out_txt, error) = query.communicate()
        out_txt = out_txt.decode("utf-8")


if __name__ == "__main__":
    run()
