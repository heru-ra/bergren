#!/bin/sh
# ----------
# Toggle compton compositor

if [ `pidof compton` ]; then
    # kill compton
    killall compton
    # display OSD notification
    notify-send -t 1000 'Compton: Disabled'
else
    # start compton, daemonized
    compton -b
    # display OSD notification
    notify-send -t 2000 'Compton: Enabled'
fi
