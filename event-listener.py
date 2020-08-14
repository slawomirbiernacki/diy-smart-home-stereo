#!/usr/bin/env python3
import os
from amp_operations import *
import time

def listen():
    print("Reacting to event...")
    print(os.environ['PLAYER_EVENT'])
    event = os.environ['PLAYER_EVENT']
    if event == "start":
        powerOn()
        time.sleep(3)
        sourceAUX()

    if event == "stop":
        sourceCD()

if __name__ == "__main__":
    listen()
