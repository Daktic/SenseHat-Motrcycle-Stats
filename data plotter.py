import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

now = datetime.now()
date_now = now.strftime("%m%d%y")

df = pd.read_csv("/home/pi/Documents/SenseHat/Bike Proj/CSV files/sense_data071920.csv").round(2)

#converts time column into datetime
df.time = pd.to_datetime(df.time)
#create hour/minutecolumns
df['hour'] = df.time.dt.hour
df['minute'] = df.time.dt.minute

#print(df.head)

df.plot(x='time', y='acc_z', kind='line')
plt.show()