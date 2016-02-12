# imports
import os
import time
import sqlalchemy
import sched



# connect to temp_sensor on GPIO on rbPI
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_sensor = '/sys/bus/w1/devices/28-000006dee630/w1_slave'

# read temperature

def tempRead():
    t = open(temp_sensor, 'r')
    lines = t.readlines()
    t.close()

    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string)/1000.0
        return round(temp_c, 1)


# print temp and time values
temperature = tempRead()
print(temperature)

datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
print(datetimeWrite)

# schedueled database write
s = sched.scheduler(time.time, time.sleep)