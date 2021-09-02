# Overview

This program on the Raspberry pi reads in the serial data sent from the arduino and sends it to a REST API. 


It should be configured to run when the Raspberry Pi starts up following a power outage using autostart


To do this, run the following commands in the Raspberry Pi command line:

```
mkdir /home/pi/.config/autostart
nano /home/pi/.config/autostart/logger.desktop
```
Inside the logger.desktop file, insert this code:
```
[Desktop Entry]
Type=Application
Name=OutageLogger
Exec=/usr/bin/python3 /home/pi/logger.py
```
Now the program should be executed on startup
