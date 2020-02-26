#app.py
import os
import time

#we're basically opening a file that is responsible for displaying current CPU temperature. it's much quicker to execute .py scrypt
#rather than entering file's path every time.

def CPUtemp():
        temperature = os.popen("vcgencmd measure_temp").readline()
        return temperature

#3 secs refreshing time.
while True:
        print(CPUtemp())
        time.sleep(3)
