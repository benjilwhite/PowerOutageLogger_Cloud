import requests
import json
import serial 
import urllib.request
import time

# establishes a serial connection with the arduino
# run the command "ls /dev/tty*" on the raspberry pi to see what port the logger is connected to. insert the address into the first parameter
if __name__ == '__main__': 
    ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout=1)

a = "" #empty string to take serial data

# waits for the logger to send the outage data and stores it in the variable a.
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('ascii').rstrip()
        print(line)
        a = line
        break

# converts the single string read by the serial function to three variables
downTime = a[0:10]
upTime = a[10:20]
maxTemp = a[20:]

# tests for internet connecting
def connect():
    try:
        response = urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

# checks for internet every 2 seconds until a connection can be established
while connect() == False:
    time.sleep(2)

# sends the data to the API once an internet connection is established    
if connect():
    url = 'api' #put the invoke link for the API here
    myobj = {'downTime': downTime, 'upTime': upTime, 'maxTemp': maxTemp}
    y = json.dumps(myobj)

    requests.post(url, data = y)

