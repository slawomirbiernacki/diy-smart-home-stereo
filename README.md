# diy-smart-home-stereo

Set of scripts to smartify my home amplifier. I use raspberry Pi 4 with IR emitter sticked to my TEAC amplifier. 
Functionality:
1. Turns on amplifier and selects input source when Spotify output device is updated. I use [spocon](https://github.com/spocon/spocon) as a spotify client (wrapper on [liberespot-java](https://github.com/librespot-org/librespot-java)).


# Installation
1. Install Spocon https://github.com/spocon/spocon
2. Register service:

        sudo ln -s /home/pi/projects/diy-smart-home-stereo/smart-stereo.service /lib/systemd/system/smart-stereo.service
        systemctl start smart-stereo
        systemctl enable smart-stereo
    


# TODO
2. Beter volume control - wider loudness range
