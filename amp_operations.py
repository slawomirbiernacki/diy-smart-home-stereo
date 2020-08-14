import sys
import os

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
    output = os.popen('ir-ctl -d /dev/lirc0 -S necx:{}'.format(code))
    print(output)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
