#!/usr/bin/env python3
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import sys
import os

os.putenv("SPOTIPY_CLIENT_ID", "5c8de412966e4bd399baaba49aab6dd8")
os.putenv("SPOTIPY_CLIENT_SECRET", "e1a850d1f64d423db2f6e76c58b971bb")
os.putenv("SPOTIPY_REDIRECT_URI", "http://localhost")

scope = "user-read-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope, username="Slawek"))

def printDevices():
    res = sp.devices()
    pprint(res)

def PrintPlaybackInfo():
    playback = sp.current_playback()
    pprint(playback)

def isRaspberryActive():
    res = sp.current_playback()
    isActive = res["device"]["name"]=="raspotify (raspberrypi)"
    print("Is rasberry active: {}".format(isActive))
    return isActive


def isMusicPlaying():
    res = sp.current_playback()
    isPlaying = bool(res["is_playing"])
    print("Is music playing: {}".format(isPlaying))
    return isPlaying

def findDevice(name, devices):
    for device in devices:
        if device["name"]==name:
            return device
    return null

if __name__ == '__main__':
    globals()[sys.argv[1]]()
