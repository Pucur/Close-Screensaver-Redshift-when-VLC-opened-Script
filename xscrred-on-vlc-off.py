import schedule
import time, os
import psutil
import pathlib
 
def check_process():
    PROCNAME = "vlc"
    for proc in psutil.process_iter():
        if proc.name() == 'vlc':
            return True
    else:
        return False
 
def check_run():
    if check_process():
        if not pathlib.Path(".vlcwasopened").exists (): #Needs to change path here!
#Optional, it turns off your monitor screen        	os.system("xrandr --output DP-3 --off") #Needs to change monitor turn-on or off outputs! Optional Feature
        	os.system("pkill xscreensaver")
		os.system("pkill redshift-gtk")
		os.system("touch .vlcwasopened")
    else:
	if pathlib.Path(".vlcwasopened").exists (): #Needs to change path here!
#Optional, it turns back the monitor screen     os.system("xrandr --output DP-3 --mode 1920x1080 --rate 75 --same-as LVDS-1 --mode 1920x1080 --output HDMI-2 --mode 1920x1080 --same-as DP-3") #Needs to change monitor turn-on or off outputs! Optional feature
		os.system("rm .vlcwasopened")
		os.system("screen -S xscrn -X quit")
		os.system("screen -S xscrn -d -m sh startscreensaver.sh") #Needs to change path here!
 
schedule.every(.10).minutes.do(check_run)
while True:
    schedule.run_pending()
    time.sleep(1)
