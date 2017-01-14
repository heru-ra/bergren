#!/bin/bash
# ----------
# Autostart routine

if ! ps ax | grep -v grep | grep stalonetray > /dev/null; then
    stalonetray &
    lemonbar-dropdown-toggle stalonetray 1 true &
fi

if ! ps ax | grep -v grep | grep lemonbar-launch > /dev/null; then
    lemonbar-launch &
else
    killall -9 lemonbar && killall -9 lemonbar-launch &
    sleep 1s && lemonbar-launch &
fi

conky -q -d -c ~/.config/conky/gpmdp-conky.conkyrc &
conky -q -d -c ~/.config/conky/gpmdp-conky-lyrics.conkyrc &

sleep 10s && nitrogen --restore
