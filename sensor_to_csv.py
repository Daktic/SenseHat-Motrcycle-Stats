from sense_hat import SenseHat
from datetime import datetime
from csv import writer
from time import sleep
from random import randint

sense = SenseHat()

timestamp = datetime.now()
delay = 1



def get_sense_data():
    sense_data = []

    
    orientation = sense.get_orientation()
    sense_data.append(orientation["yaw"])
    sense_data.append(orientation["pitch"])
    sense_data.append(orientation["roll"])
    
    mag = sense.get_compass_raw()
    sense_data.append(mag["x"])
    sense_data.append(mag["y"])
    sense_data.append(mag["z"])
    
    acc = sense.get_accelerometer_raw()
    sense_data.append(mag["x"])
    sense_data.append(mag["y"])
    sense_data.append(mag["z"])
    
    gyro = sense.get_gyroscope_raw()
    sense_data.append(gyro["x"])
    sense_data.append(gyro["y"])
    sense_data.append(gyro["z"])
    
    sense_data.append(datetime.now())
        
    return sense_data

now = datetime.now()
date_now = now.strftime("%m%d%y")

with open('sense_data'+ date_now +'.csv', 'w', newline='') as f:
    data_writer  = writer(f)
    
    data_writer.writerow([
                      'yaw','pitch','roll','mag_x','mag_y','mag_z',
                      'acc_x','acc_y','acc_z',
                      'gyro_x', 'gyro_y', 'gyro_z',
                      'date','time'])
    
    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    sense.show_message("Tracking")
                    while True:
                        num_1 = randint(0,255)
                        num_2 = randint(0,255)
                        num_3 = randint(0,255)
                        r_colour = (num_1,num_2,num_3)
                        data = get_sense_data()
                        dt = data[-1] - timestamp
                        if dt.seconds > delay:
                            data_writer.writerow(data)
                            timestamp = datetime.now()
                            f.flush()
                            sense.show_message("-",text_colour = r_colour, scroll_speed=.005)
                        '''if event.action == "pressed":
                            if event.direction == "down":
                                break
                    sense.show_message("Session Ended")'''
                        #how do i get this to stop once pressed?
                else:
                    sense.show_message("Begin? Press Up.")
                    sleep(3)
                    sense.clear()
                    
