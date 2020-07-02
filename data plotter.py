import matplotlib.pyplot as plt
import csv
from datetime import datetime

now = datetime.now()
date_now = now.strftime("%m%d%y")

yaw = []
pitch = []
roll = []
time = []


with open('sense_data'+ date_now +'.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        yaw.append(row[0])
        #pitch.append(row[1])
        #roll.append(row[2])
        time.append(row[12])
        
plt.plot(time,yaw, label = 'yaw over time')
plt.xlabel('time')
plt.ylabel('yaw')
plt.title('interesting graph')
plt.legend()
plt.show()