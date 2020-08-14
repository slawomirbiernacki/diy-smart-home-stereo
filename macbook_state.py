#!/usr/bin/env python3
import telnetlib
import socket, errno
import subprocess

ip = subprocess.check_output("sudo arp-scan --localnet --interface=wlan0 | grep 192.168.0.9 | awk '{print $1}'", shell=True)
ip = ip.strip()

def checkMacState():
    try:
        tn = telnetlib.Telnet(ip, timeout=3)
    except socket.timeout as error:
        print("Mac ip: {},  state: off/sleeping".format(ip))
        return False
    except socket.error as error:
        if error.errno == errno.ECONNREFUSED:
            print("Mac ip: {}, state: on".format(ip))
            return True
        else:
            raise

if __name__ == "__main__":
    checkMacState()
