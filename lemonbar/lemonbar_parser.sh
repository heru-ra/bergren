#!/bin/bash
#

# load config values
. $HOME/.config/lemonbar/lemonbar.conf

# fifo parser
while read -r line; do
    case $line in
        DBG*)
            # for testing and debugging purposes
            dbg="%{B${color_sec_b1}}%{F${color_icon}%{F- T1}${stab}${line#???}${stab}%{F- B-}"
        ;;  
        WSN*)
            # workspace name(s)
            eval wsn[${line:3:1}]="\"%{B${color_sec_b1}}%{F${color_icon}%{F- T1}${stab}${line#????}${stab}%{F- B-}\""
        ;;  
        UPDATES*)
            # number of package updates available
            if [[ ${line#???????} != 0 ]]; then
                updates="%{A3:${right_click_cmd[4]}:}%{B${color_sec_b1}}%{F${color_icon}}${stab}%{T3}${icon_updates}%{F- T1} ${line#???????}%{F- B-}%{A}"
            else
                updates=""
            fi
        ;;
        VOLICON*)
            icon_vol=${line#???????}
        ;;
        VOL*)
            # Volume
            vol="%{A3:${right_click_cmd[1]}:}%{B${color_sec_b1}}%{F${color_icon}}%{T3}${icon_vol}%{F- T1} ${line#???}${stab}%{F- B-}%{A}"
        ;;
        CKY*)
            # conky array: 0 = wday, 1 = mday, 2 = month, 3 = time, 4 = bat, 5 = wifi ssid, 6 = wifi signal
            cky_arr=(${line#???})
            
            # time
            time="%{A3:${right_click_cmd[3]}:}%{F${color_icon} B${color_sec_b1}}%{T3}${icon_clock}%{F- T1} ${cky_arr[3]}${stab}%{F- B-}%{A}"
            
            # battery
            if [[ ${cky_arr[4]} -ge 75 ]] || [[ ${cky_arr[4]} == 100 ]]; then    
                icon_bat=${icon_bat_full}
            elif [[ ${cky_arr[4]} -ge 50 ]]; then    
                icon_bat=${icon_bat_high}
            elif [[ ${cky_arr[4]} -ge 25 ]]; then    
                icon_bat=${icon_bat_half}
            elif [[ ${cky_arr[4]} < 25 ]]; then    
                icon_bat=${icon_bat_low}
            fi
            bat_padded=$(printf "%3s\n" "${cky_arr[4]}")
            bat="%{A3:${right_click_cmd[2]}:}%{F${color_icon} B${color_sec_b1}}%{T3}${icon_bat}%{F- T1} ${bat_padded}%${stab}%{F- B-}%{A}"
            
            # wifi
            if [[ ${cky_arr[5]} != "off/any" ]]; then
                wifi="%{A3:${right_click_cmd[0]}:}%{F${color_icon} B${color_sec_b1}}${stab}%{T3}${icon_wifi}%{F- T1} ${cky_arr[5]} (${cky_arr[6]}%)${stab}%{F- B-}%{A}"
            else
                wifi="%{A3:${right_click_cmd[0]}:}%{F${color_icon} B${color_sec_b1}}${stab}%{T3}${icon_wifi}%{F- T1} off${stab}%{F- B-}%{A}"
            fi
        ;;
    esac
    
    # count our monitors/workspaces, and if more than one, add each one to the bar
    more_monitors=""
    total_monitors=$((${#wsn[@]}-1))
    for i in $(seq 1 $total_monitors); do
        more_monitors="${more_monitors}%{S$i}%{l}%{O20}${wsn[$i]}"
    done

    # pipe the output
    printf "%s\n" "%{S0}%{l}%{O20}${wsn[0]}%{C}${dbg}%{r}${updates}${wifi}${vol}${bat}${time}%{O20}${more_monitors}"

done
