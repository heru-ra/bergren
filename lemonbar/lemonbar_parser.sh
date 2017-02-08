#!/bin/bash
#
# parsing script for lemonbar-launch
#
################################################################################

# load config values
. $HOME/.config/lemonbar/lemonbar.conf

# reformat some of our config variables
bar_horizontal_padding="%{O${bar_horizontal_padding}}"
element_spacing="%{O${element_spacing}}"

# format element decorations and spacing, depending if specified
if [[ ${decoration_start} ]]; then
    decoration_start="%{T3}${decoration_start}%{F- B-}${element_spacing}"
fi

if [[ ${decoration_end} ]]; then
    decoration_end="${element_spacing}%{T3}${decoration_end}%{F- B-}"
fi

if [[ ! ${decoration_separator} ]]; then
    element_separator="${element_spacing}"
else
    element_separator="${element_spacing}%{T3}${decoration_separator}%{F- B-}${element_spacing}"
fi

# fifo parser
while read -r line; do
    case $line in
        DBG*) # for testing and debugging purposes
            dbg="%{B${color_element_background}}%{F${color_icon}%{F- T1}${line#???}%{F- B-}"
        ;;  
        WSN*) # workspace name(s)
            # if active workspace, use highlight font/color
            if [[ ${line:4:1} == "1" ]]; then
                eval wsn[${line:3:1}]="\"%{B${color_element_background}}%{F${color_highlight_foreground}}%{T2}${line#?????}%{F- B-}\""
            else
                eval wsn[${line:3:1}]="\"%{B${color_element_background}}%{F- T1}${line#?????}%{F- B-}\""
            fi
        ;;  
        UPDATES*) # number of package updates available
            if [[ ${line#???????} != 0 && ${line#???????} ]]; then
                updates="%{A3:${right_click_cmd[4]}:}%{B${color_element_background}}%{F${color_icon}}%{T3}${icon_updates}%{F- T1} ${line#???????}%{F- B-}%{A}${element_separator}"
            else
                updates=""
            fi
        ;;
        VOLICON*) # dynamic volume icon
            icon_vol=${line#???????}
        ;;
        VOL*) # volume
            vol="%{A3:${right_click_cmd[1]}:}%{B${color_element_background}}%{F${color_icon}}%{T3}${icon_vol}%{F- T1} ${line#???}%{F- B-}%{A}"
        ;;
        CKY*) # conky array
            # 0 = wday, 1 = mday, 2 = month, 3 = time, 4 = bat, 5 = wifi ssid, 6 = wifi signal
            cky_arr=(${line#???})
            
            # time
            time="%{A3:${right_click_cmd[3]}:}%{F${color_icon} B${color_element_background}}%{T3}${icon_clock}%{F- T1} ${cky_arr[3]}%{F- B-}%{A}"
            
            # battery, dynamic icon
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
            bat="%{A3:${right_click_cmd[2]}:}%{F${color_icon} B${color_element_background}}%{T3}${icon_bat}%{F- T1} ${bat_padded}%{F- B-}%{A}"
            
            # wifi
            if [[ ${cky_arr[5]} != "off/any" ]]; then
                wifi="%{A3:${right_click_cmd[0]}:}%{F${color_icon} B${color_element_background}}%{T3}${icon_wifi}%{F- T1} ${cky_arr[5]} (${cky_arr[6]}%)%{F- B-}%{A}"
            else
                wifi="%{A3:${right_click_cmd[0]}:}%{F${color_icon} B${color_element_background}}%{T3}${icon_wifi}%{F- T1} off%{F- B-}%{A}"
            fi
        ;;
    esac
    
    # count our monitors/workspaces, and if more than one, add each one to the bar
    more_monitors=""
    total_monitors=$((${#wsn[@]}-1))
    for i in $(seq 1 $total_monitors); do
        more_monitors="${more_monitors}%{S$i}%{l}${bar_horizontal_padding}${decoration_start}${wsn[$i]}${decoration_end}"
    done

    # pipe the output
    printf "%s\n" "%{S0}%{l}${bar_horizontal_padding}${decoration_start}${wsn[0]}${decoration_end}%{C}${dbg}%{r}${decoration_start}${updates}${wifi}${element_separator}${vol}${element_separator}${bat}${element_separator}${time}${decoration_end}${bar_horizontal_padding}${more_monitors}"

done
