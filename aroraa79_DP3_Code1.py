
#import math
import math

#import linear actuator 
from gpiozero import Motor
import time

motor=Motor(forward=#pinnumber, backward=#pinnumber) 

#import LED 
from gpiozero import LED
import time
import sys

#LEDs by color 
red_led=LED(#pinnumber)
green_led=LED(#pinnumber)
yellow_led=LED(#pinnumber)


button=Button(#pinnumber)
    
def button_counter():
    button_number=0
    if button.is_pressed:
        button_number+=
    if button_number=4:
        button_number=1
    return button_number

def force_open():
    motor.forward() 

def force_close():
    motor.backward()

def det_degrees():
    ##function which converts info from linear actuator to determine the number of degrees a certain time/distance equates to
    ##potentially use MM5 code from lab?
    ##need to convert time -> distance -> degrees 

def settings():
    if button_number=1:
        red.led.off()
        green.led.on() 
        yellow.led.off()
        #force_open()

    elif button_number=2:
        red.led.off()
        green.led.off()
        yellow.led.on()
        #automatic 

    elif button_number=3:
        red.led.on()
        green.led.off()
        yellow.led.off()
        #force_close()
