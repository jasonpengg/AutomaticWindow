##from sensor_library import * 
from weatherapi import get_weather
from object_pi import * 

import time
#time will be determined and changed later, for now it is for rolling average 

def Temperature_Sensor():
   return 1

def rolling_average(sensor):
    total_temperature = 0
    for i in range (10):
       print(i)
       total_temperature = total_temperature + sensor.avg_temp()
       average_temp = total_temperature/i
       time.sleep(1)
    return average_temp

def print_status(pi_status):
   green_led = pi.get_green_led(pi_status)
   yellow_led = pi.get_yellow_led(pi_status)
   red_led = pi.get_red_led(pi_status)
   Motor_status = None
   temperature_raw = pi.get_raw_temperature(pi_status)
   temperature_avg = pi.get_avg_temperature(pi_status)
   print (green_led)
   print (yellow_led)
   print (red_led)
   print (temperature_raw)
   print (temperature_avg)



def main():
  # ---------------- Intialize variables ------------- # 
  pi_status = pi(False, False, False, None, None)
  
  print_status(pi_status)

  pi.set_red_led(pi_status,True)
  print_status(pi_status)
  sensor = Temperature_Sensor()
  outside_temp = get_weather()[0]
  weather_description = get_weather()[1]
  print(outside_temp)
  print(weather_description)



main()


    