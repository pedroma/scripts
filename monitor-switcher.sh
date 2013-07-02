#xrandr --prop | grep "{^dis}connected" | cut --delimiter=" " -f1
#xrandr --output DP1 --primary

xrandr --output LVDS1 --off
xrandr --output DP1 --mode 1680x1050 --refresh 74.9
