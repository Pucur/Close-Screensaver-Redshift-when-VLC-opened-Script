Hello!

This is my first GitHub project ever, i was angry about the redshift doesn't change itself back when some player is opened (in my case the one of the best media player, VLC), so i created a python script which automatically does it.

It should works all UNIX-like system

Packages needed:

pip install psutil
pip install pathlib

crontab -e cronjob as root:

* * * * * python /path/to/redshift-vlc-off.py >/dev/null 2>&1

I'm accepting all suggestion about this project, i still testing it.
