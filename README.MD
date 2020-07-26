Hello!

This is my first GitHub project ever, and now all the code was changed, now it works smoothly.

Features:

- Open/close screensaver when VLC is running/not running.
- Open/close redshift when VLC is running/not running.
- Optional: If you have mirrored your screen with your TV, and you wish to turn off the monitor screen, when you watching the movie on the TV screen, you could turn off when you configure it.

It should works all UNIX-like system

Packages needed:

- pip install psutil
- pip install pathlib
- pip install time
- pip install os
- pip install schedule

- apt-get install screen
- apt-get install redshift-gtk (for redshift)
- apt-get install xscreensaver xscreensaver-data-extra xscreensaver-gl-extra (for screensaver)

crontab -e as your user, or add to startup

@reboot python /path/to/xscrred-on-vlc-off.py >/dev/null 2>&1

If has any question, feel free to send me a message.

Happy Movie Times!
