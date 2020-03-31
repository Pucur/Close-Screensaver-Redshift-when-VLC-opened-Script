import psutil
import os
import pathlib

def find_name(name):
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            if pinfo['name'] == name:
#                return True
                os.system("pkill redshift")
                os.system("touch .vlcwasopened")
                os.system("redshift -l 19.04:47.49 -t 6498:6498 -g 0.8 -m randr -v &")
                print(command.read())
                print(command.close())
            else:
                continue
        except psutil.NoSuchProcess:
            pass
    if pathlib.Path(".vlcwasopened").exists ():
        os.system("pkill redshift")
        os.system("rm .vlcwasopened")
        os.system("redshift -l 19.04:47.49 -t 6450:3450 -g 0.8 -m randr -v &")
#    return False


#print(find_name('redshift'))
print(find_name('vlc'))
