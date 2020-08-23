import sys
import os
import subprocess

def powerOn():
    print("Powering on amplifier")
    runCode("0x856a97")

def shutDown():
    print("Shutting down amplifier")
    runCode("0x856a93")

def sourceCD():
    print("Changing source to CD")
    runCode('0x856a8c')

def sourceAUX():
    print("Changing source to AUX")
    runCode('0x856a24')

def runCode(code):
    necCommand = 'necx:{}'.format(code)
    #result = subprocess.run(["ir-ctl", "-d","/dev/lirc0","-S", necCommand], capture_output=True, check=True)
    result = subprocess.run(['ir-ctl -d /dev/lirc0 -S necx:{}'.format(code)], shell=True,  capture_output=True, check=True)
    print(result)

if __name__ == '__main__':
    globals()[sys.argv[1]]()
