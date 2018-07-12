import matplotlib.pyplot as plt
import datetime
import numpy as np

data = []
sensor1 = []
sensor2 = []
time = []

with open("output.txt","r") as f:
    data = f.readlines()

first_sensor_len = len(data[0])

for var in data:
    if var[2:7] == "First" and len(var) == first_sensor_len:
        sensor1.append(var[28:33])
        sensor2.append(var[75:80])
        time.append(datetime.datetime.strptime(var[36:44], "%H:%M:%S"))
    elif var[2:8] == "Second" and len(var) == first_sensor_len:
        sensor2.append(var[29:34])
        sensor1.append(var[75:80])
        time.append(datetime.datetime.strptime(var[83:91], "%H:%M:%S"))

newday_marker = np.append(False, np.diff(time) < datetime.timedelta(0))
day_offset = np.cumsum(newday_marker)
date_offset = [datetime.timedelta(int(dt)) for dt in day_offset]
dtime = [t + dos for t, dos in zip(time, date_offset)]

figPres = plt.figure(figsize=(10,7.5))
axPres  = figPres.add_subplot(211)
axPres2 = figPres.add_subplot(212)

plt.subplot(2,1,1)
plt.plot(dtime,sensor1)
plt.title("Temperature Sensor 1")
axPres.yaxis.set_label_coords(-0.035,1.05)
axPres.xaxis.set_label_coords(1.05, -0.01)
plt.ylabel("[*C]", fontsize=14, rotation=0)
plt.xlabel("[t]", fontsize=14)

plt.subplot(2,1,2)
plt.plot(dtime,sensor2)
plt.title("Temperature Sensor 2")
axPres2.yaxis.set_label_coords(-0.035,1.05)
axPres2.xaxis.set_label_coords(1.05,-0.01)
plt.ylabel("[*C]", fontsize=14, rotation=0)
plt.xlabel("[t]", fontsize=14)

plt.savefig("diagram.png")
