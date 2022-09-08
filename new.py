from codeop import CommandCompiler
from db import getinfo,conn
import env
from os import system as sys
def pushdashboard():
    env.dashboard.start()
def pushlogin():
    command = "env.login"
    sys("Wrong credentials!")
    sys(f"{command}")

def login(usr,pswd):
    # query
    log=False
    if log:
        pushdashboard()
    else:
        pushlogin()