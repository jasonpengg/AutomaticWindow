# imports from different files in the folder. 
from sensor_library import * 
# used to access the API key to get realtime updates of weather 
from src.weatherapi import get_weather
# used to create a pi object to keep track of all processes 
from src.object_pi import *
# used to control the linear actuator 
from gpiozero import Motor 
import time  
motor = Motor(forward=16, backward=12) 

# this is a function that updates the temperature immediately in real time 
def update_average(sensor,pi_status):
   pi.set_raw_temperature(pi_status, sensor.avg_temp())
   print_status(pi_status)
   return None

# this prints all the pi object's properties 
def print_status(pi_status):
   green_led = return_string(pi.get_green_led(pi_status))
   yellow_led = return_string(pi.get_yellow_led(pi_status))
   red_led = return_string(pi.get_red_led(pi_status))
   Motor_status = return_string(pi.get_motor_status(pi_status))
   temperature_raw = pi.get_raw_temperature(pi_status)
   temperature_avg = pi.get_avg_temperature(pi_status)
   Window_state = pi.get_window_status(pi_status)
   print(f'{"Temperature Raw":<15} {"Temperature Avg":<15} {"Green Led":<10} {"Yellow Led":<10} {"Red Led":<8} {"Motor Status":<12} {"Window Status":<15}')
   print(f'{temperature_raw[0]:<15} {temperature_avg:<15} {green_led:<10} {yellow_led:<10} {red_led:<8} {Motor_status:<12} {Window_state:<12}')

# this function turns the boolean True/False into string values 
def return_string(input):
   if input == True:
      return "ON"
   else:
      return "OFF"

# ----------------------------------------------- THIS IS WHERE THE WINDOW LOGIC BEGINS --------------------------------------------------------#

# this function determines if the weather outside is appropriate to open the window 
def weather_conditon():
   weather_description = get_weather()[1].lower()
   if weather_description == 'sunny' or weather_description == 'cloudy' or weather_description == 'partly cloudy' or weather_description == 'overcast': 
      return True
   else:
      return False

# function checks if the room is hotter inside than outside
def is_hotter_inside(pi_status):
   if float(pi.get_avg_temperature(pi_status)) > float(get_weather()[0]):
      return True
   else: 
      return False


# Main logic of the device, determines if the window show open and by how much 
def window_conditon(preferred_temperature, pi_status):
  
   inside_temp = float(pi.get_avg_temperature(pi_status))
   preferred_temperature = int(preferred_temperature)
   ## checks if the window should be opened or closed 
   if weather_conditon() == True: 
      # REMOVE
      print("weather is nice")
      
      ## if the room is hotter than outside then the device should only open if the user wants the room to be colder 
      if is_hotter_inside(pi_status) == True: 
         
         #REMOVE 
         print("inside is hotter than outside")

         ## if the room is hotter than preferred temperature (within 1C range) the window should open
         if inside_temp > preferred_temperature and abs(inside_temp - preferred_temperature ) > 1:
            open_window(degrees_of_opening(preferred_temperature, pi_status), pi_status) 

         ## if the room is colder than preferred temperature (within 1C range ) the window should be closed 
         elif inside_temp < preferred_temperature and abs(inside_temp - preferred_temperature )> 1:
            close_window(pi_status)
         else:

            ##do nothing 
            return None
      
      ## if the room is colder than outside then the window should only open if user wants the room to be warmer 
      elif is_hotter_inside(pi_status) == False: 
         print("inside is colder")
         ## if the room is colder than preferred temperature then the window should open to make the room hotter 
         if inside_temp < preferred_temperature and abs((inside_temp - preferred_temperature )) > 1:
            open_window(degrees_of_opening(preferred_temperature, pi_status),pi_status) 
         ## if the room is hotter than preferred temperature then window should stay closed to prevent the room from getting colder since outside is colder.
         elif inside_temp > preferred_temperature and abs(inside_temp - preferred_temperature ) > 1:
            close_window(pi_status)
         else:
            ## do nothing
            return None

   # if the window can't be opened then it should be closed.    
   else: 
      close_window(pi_status)
# this section determines how much the window shouold open 

def degrees_of_opening(preferred_temperature, pi_status):
   ## two settings 
   ## 0: closed
   ## 1: Half way opened
   ## 2: fully opened 
   temperature_difference = abs(float(preferred_temperature) - float(pi.get_avg_temperature(pi_status)))
   # if the temperature is within 2 degrees, it can open half way to minimize temperature changes 
   # if the temerpature is greater, then the window should be fully opened so that it allows maximum airflow 
   if temperature_difference > 2:
      return 0
   else: 
      return 1


#-------------------------------------------------- THIS SECTION MANIPULATES THE LINEAR ACTUATOR --------------------------------------------# 

# determines how the linear actuator should move depending on previous function 
def open_window(window_setting, pi_status):
   # window needs to be opened half way, and current status is closed 
   if window_setting == 1 and pi.get_window_status(pi_status) == 0: 
      print("opening window from closed to half way ")
      close_to_half(pi_status)
      pi.set_window_status(pi_status,window_setting)
   # window needs to halfway but is already there 
   elif window_setting == 1 and pi.get_window_status(pi_status) == 1: 
      #do nothing 
      pi.set_window_status(pi_status,window_setting)
   # window needs to close to half from the open position 
   elif window_setting == 1 and pi.get_window_status(pi_status) == 2: 
      print("closing window from open to half way")
      open_to_half(pi_status)
      pi.set_window_status(pi_status,window_setting)
   # window needs to open from closed position to full. 
   # they are both 0 because the 0 from window_setting only returns a value if degrees_of_opening runs and that only runs if the window needs to be opened 
   elif window_setting == 0 and pi.get_window_status(pi_status) == 0: 
      print("opening window from closed to full")
      close_to_open(pi_status)
      pi.set_window_status(pi_status, 2)
   # window needs to open to full from half 
   elif window_setting == 0 and pi.get_window_status(pi_status) == 1: 
      print("opening window from half way to full")
      half_to_open(pi_status)
      pi.set_window_status(pi_status, 0)
   # window needs to open to full but is already there 
   elif window_setting == 0 and pi.get_window_status(pi_status) == 2: 
      print("do nothing")
      pi.set_window_status(pi_status, 2)

# opens the window depending on previous positon 
def force_open_window(pi_status):
   if pi.get_window_status(pi_status) == 0:
      print("open from closed to full")
      close_to_open(pi_status)
   elif pi.get_window_status(pi_status) == 1:
      print("open from half to full")
      half_to_open(pi_status)
   elif pi.get_window_status(pi_status) == 2:
      print("do nothing")
   pi.set_window_status(pi_status,2)

#closed window based on previous position 
def close_window(pi_status):
   if pi.get_window_status(pi_status) == 0:
      print("do nothing")
   elif pi.get_window_status(pi_status) == 1:
      print("close from half way")
      half_to_close(pi_status)
   elif pi.get_window_status(pi_status) == 2:
      print("close from fully opened")
      open_to_close(pi_status)
   pi.set_window_status(pi_status,0)

#------------------------------------------------------- THESE ARE THE PHYSICAL OPERATIONS TO MANIPULATE THE LINEAR ACTUATOR --------------------------------#
def close_to_open(pi_status):
   print("close_to_open")
   pi.set_motor_status(pi_status,True)
   print_status(pi_status)
   motor.forward()
   time.sleep(10)
   motor.stop()
   pi.set_motor_status(pi_status,False)

def close_to_half(pi_status):
   print("close_to_half")
   pi.set_motor_status(pi_status,True)
   print_status(pi_status)
   motor.forward()
   time.sleep(10)
   motor.stop()
   pi.set_motor_status(pi_status,False)

def half_to_close(pi_status):
   print("half_to_close")
   pi.set_motor_status(pi_status,True)
   print_status(pi_status)
   motor.forward()
   time.sleep(10)
   motor.stop()
   pi.set_motor_status(pi_status,False)

def half_to_open(pi_status):
   print("half_to_open")
   pi.set_motor_status(pi_status,True)
   print_status(pi_status)
   motor.forward()
   time.sleep(10)
   motor.stop()
   pi.set_motor_status(pi_status,False)

def open_to_close(pi_status):
   print("open_to_close")
   pi.set_motor_status(pi_status,True)
   print_status(pi_status)
   motor.forward()
   time.sleep(10)
   motor.stop()
   pi.set_motor_status(pi_status,False)

def open_to_half(pi_status):
   print("open_to_half")
   pi.set_motor_status(pi_status,True)
   print_status(pi_status)
   motor.forward()
   time.sleep(10)
   motor.stop()
   pi.set_motor_status(pi_status,False)

   


    