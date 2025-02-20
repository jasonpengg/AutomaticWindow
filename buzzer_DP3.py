Import the Buzzer and Motor 
from gpiozero import Buzzer
from gpiozero import Motor
import time
import sys

buzzer_object=Buzzer() #put pin number here
motor=Motor(forward=,backward=) #put pin number here 

def warning(): #Function that is used to alert user of when the window is opening or closing 
    if motor.forward() or motor.backward:#is there a way to know when the actuator is active 
        while True: #do we want the buzzer to buzz for the entire time the actuator is moving, or 
            buzzer_object.on()
            time.sleep(1) #To add delay
            buzzer_object.off()
            time.sleep(1) #To add delay
        
    
