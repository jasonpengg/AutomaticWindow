from sensor_library import * 
import time 
sensor = Temperature_Sensor()

print (sensor.avg_temp())

while True:
    print(sensor.avg_temp)
    time.sleep (1000)
