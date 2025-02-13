##from sensor_library import * 
from weatherapi import get_weather
from object_pi import * 

import time
#time will be determined and changed later, for now it is for rolling average 

def Temperature_Sensor():
   return 1

def rolling_average(sensor,pi_status):
    total_temperature = 0
    for i in range (10):
       
       ## i should be replaced with sensor.
       pi.set_raw_temperature(pi_status, i)

       print_status(pi_status)
       time.sleep(1)
    return None

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

def weather_conditon():
   weather_description = get_weather()[1].lower()
   if weather_description == 'sunny' or weather_description == 'cloudy' or weather_description == 'partly cloudy' or weather_description == 'overcast': 
      return True
   else:
      return False




def window_conditon(preferred_temperature, sensor):
   ## checks if the window should be opened or closed 
   print("hello")
   rolling_average(sensor)
   if weather_conditon() == True: 
      print('hello')




def main():
  # ---------------- Intialize variables ------------- # 
  pi_status = pi(False, False, False, None, None)
  sensor = Temperature_Sensor()
  ##print_status(pi_status)

  pi.set_red_led(pi_status,True)
  print_status(pi_status)
  rolling_average(sensor,pi_status)
  outside_temp = get_weather()[0]
  weather_description = get_weather()[1]
  print(outside_temp)
  print(weather_description)
  print(weather_conditon())

main()


    