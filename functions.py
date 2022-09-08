from datetime import datetime
from os import system as sys
from db import *
from camera import getcameras
from traffic import getlights
def take_logs():
    logtime = str(datetime.now())
    log = "button clicked at {logtime}".format
    cmd = "echo {log}>>> logfiles.txt"
    sys(cmd)

def dashbod():
    print("Dashbard")

def traffic():
    print("TRaffic lights absent")

def camera():
    print("CAmera")

def incidents():
    print("incidents")
    
def culprit():
    print("culprit")
    
def report():
    print("report")
    
def logout():
    print("logout")

def getnumber(value):
    if value == "incidents":
        return getincidents()
    elif value == "culprits":
        return getculprits()
    elif value == "cameras":
        return getcameras()
    elif value == "lights":
        return getlights()
    return 0
