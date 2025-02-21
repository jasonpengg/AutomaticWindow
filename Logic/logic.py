from sensor_library import * 
from Logic.weatherapi import get_weather
from Logic.object_pi import * 
import time

#time will be determined and changed later, for now it is for rolling average 

def update_average(sensor,pi_status):
   ## i should be replaced with sensor.avg_temp.
   pi.set_raw_temperature(pi_status, sensor.avg_temp())
   print_status(pi_status)
   time.sleep(1)
   return None

def print_status(pi_status):
   green_led = return_string(pi.get_green_led(pi_status))
   yellow_led = return_string(pi.get_yellow_led(pi_status))
   red_led = return_string(pi.get_red_led(pi_status))
   Motor_status = return_string(None)
   temperature_raw = pi.get_raw_temperature(pi_status)
   temperature_avg = pi.get_avg_temperature(pi_status)
   Window_state = pi.get_window_status(pi_status)
   print(f'{"Temperature Raw":<15} {"Temperature Avg":<15} {"Green Led":<10} {"Yellow Led":<10} {"Red Led":<8} {"Motor Status":<12} {"Window Status":<15}')
   print(f'{temperature_raw[0]:<15} {temperature_avg:<15} {green_led:<10} {yellow_led:<10} {red_led:<8} {Motor_status:<12} {Window_state:<12}')

def return_string(input):
   if input == True:
      return "ON"
   else:
      return "OFF"

def weather_conditon():
   weather_description = get_weather()[1].lower()
   if weather_description == 'sunny' or weather_description == 'cloudy' or weather_description == 'partly cloudy' or weather_description == 'overcast': 
      return True
   else:
      return False

def is_hotter_inside(pi_status):
   ## function checks if the room is hotter inside than outside 
   if float(pi.get_avg_temperature(pi_status)) > float(get_weather()[0]):
      return True
   else: 
      return False


def window_conditon(preferred_temperature, pi_status):
   ## checks if the window should be opened or closed 
   inside_temp = float(pi.get_avg_temperature(pi_status))
   preferred_temperature = int(preferred_temperature)
   if weather_conditon() == True: 
      print("weather is nice")
      ## if the room is hotter than outside 
      if is_hotter_inside(pi_status) == True: 
         print("inside is hotter than outside")
         ## if the room is hotter than preferred temperature (within 1C range)
         if inside_temp > preferred_temperature and abs(inside_temp - preferred_temperature ) > 1:
            open_window(degrees_of_opening(preferred_temperature, pi_status), pi_status) 

         ## if the room is colder than preferred temperature (within 1C range )
         elif inside_temp < preferred_temperature and abs(inside_temp - preferred_temperature )> 1:
            close_window(pi_status)
         else:

            ##do nothing 
            return False
      
      ## if the room is colder than outside 
      elif is_hotter_inside(pi_status) == False: 
         print("inside is colder")
         ## if the room is colder than preferred temperature (want room to be hotter bc outside is hot)
         if inside_temp < preferred_temperature and abs((inside_temp - preferred_temperature )) > 1:
            open_window(degrees_of_opening(preferred_temperature, pi_status),pi_status) 
         ## if thr room is hotter than preferred temperature (want room to stay cold bc outside is hot)
         elif inside_temp > preferred_temperature and abs(inside_temp - preferred_temperature ) > 1:
            close_window(pi_status)
         else:
            ## do nothing
            return False
         
   else: 
      close_window()
   
def open_window(window_setting, pi_status):
   if window_setting == 1 and pi.get_window_status(pi_status) == 0: 
      print("opening window from closed to half way ")
      close_to_half()
      pi.set_window_status(pi_status,window_setting)
   elif window_setting == 1 and pi.get_window_status(pi_status) == 1: 
      print("do nothing")
      pi.set_window_status(pi_status,window_setting)
   elif window_setting == 1 and pi.get_window_status(pi_status) == 2: 
      print("closing window from open to half way")
      open_to_half()
      pi.set_window_status(pi_status,window_setting)
   elif window_setting == 0 and pi.get_window_status(pi_status) == 0: 
      print("opening window from closed to full")
      close_to_open()
      pi.set_window_status(pi_status, 2)
   elif window_setting == 0 and pi.get_window_status(pi_status) == 1: 
      print("opening window from half way to full")
      half_to_open()
      pi.set_window_status(pi_status, 0)
   elif window_setting == 0 and pi.get_window_status(pi_status) == 2: 
      print("do nothing")
      pi.set_window_status(pi_status, 2)

def close_to_open():
   print("close_to_open")

def close_to_half():
   print("close_to_half")

def half_to_close():
   print("half_to_close")

def half_to_open():
   print("half_to_open")

def open_to_close():
   print("open_to_close")

def open_to_half():
   print("open_to_half")


def force_open_window(pi_status):
   if pi.get_window_status(pi_status) == 0:
      print("open from closed to full")
      close_to_open()
   elif pi.get_window_status(pi_status) == 1:
      print("open from half to full")
      half_to_open()
   elif pi.get_window_status(pi_status) == 2:
      print("do nothing")
   pi.set_window_status(pi_status,2)

def close_window(pi_status):
   if pi.get_window_status(pi_status) == 0:
      print("do nothing")
   elif pi.get_window_status(pi_status) == 1:
      print("close from half way")
      half_to_close()
   elif pi.get_window_status(pi_status) == 2:
      print("close from fully opened")
      open_to_close()
   pi.set_window_status(pi_status,0)

def degrees_of_opening(preferred_temperature, pi_status):
   ## two settings 
   ## 0: closed
   ## 1: Half way opened
   ## 2: fully opened 
   temperature_difference = abs(float(preferred_temperature) - float(pi.get_avg_temperature(pi_status)))

   if temperature_difference > 2:
      return 0
   else: 
      return 1
   


    