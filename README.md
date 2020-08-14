# diy-smart-home-stereo

This runs on Raspberry 4 - no need for LIRC!

1. Install Spocon https://github.com/spocon/spocon
2. Register service:

        sudo ln -s /home/pi/projects/diy-smart-home-stereo/smart-stereo.service /lib/systemd/system/smart-stereo.service
        systemctl start smart-stereo
        systemctl enable smart-stereo
    


# TODO
1. Logs
2. Beter volume control - wider loudness range
