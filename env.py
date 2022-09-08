from importlib.resources import path
from msilib.schema import Directory
from time import clock_settime
from datetime import datetime
import os

from functions import traffic

class env:
    def __init__(self):
        path = "D:\projects\TPEATLA"
        interface = {"dashboard":"dashboard","login":"login","logout":"logout"}
        gateways = {"light":"lights","camera":"cameras"}
    class dashboard:
        def start(self):
            logs = open("env","w")
            logs.write(1)
            logs.close
            os.system(f"python {path}\home.py")
        def stop(self):
            logs = open("env","w+")
            date = str(datetime.now())
            logs.write(f"System closed at {date}")
            batch = logs.read
            logs.close
            os.system(f"echo {batch} >>logs.txt")

    def update_env(self, new_path):
        self.path = new_path


os.system("echo 'env exited' >>logs.txt")
            