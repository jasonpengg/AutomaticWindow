from gpiozero import Button, LED
from src.object_pi import *

# define LEDs
red_led = LED(5)
green_led = LED(7)
yellow_led = LED(6)

# define buttons
button = Button(23)
text_button = Button(14)

# updates the button press count and loops back to 1 after 3 presses 
def button_counter(button_press_count):
    if button.is_pressed:
        button_press_count += 1  
        if button_press_count > 3:  
            button_press_count = 1
    return button_press_count

#Controls which LED is on based on the button press count 
def led_control(button_press_count, pi_status):
    if button_press_count == 1:
        red_led.on()
        green_led.off()
        yellow_led.off()
        pi.set_red_led(pi_status, True)
        pi.set_green_led(pi_status, False)
        pi.set_yellow_led(pi_status, False)
    elif button_press_count == 2:
        red_led.off()
        green_led.on()
        yellow_led.off()
        pi.set_red_led(pi_status, False)
        pi.set_green_led(pi_status, True)
        pi.set_yellow_led(pi_status, False)
    elif button_press_count == 3:
        red_led.off()
        green_led.off()
        yellow_led.on()
        pi.set_red_led(pi_status, False)
        pi.set_green_led(pi_status, False)
        pi.set_yellow_led(pi_status, True)

def text_input():
    if text_button.is_pressed:
        return True
    
def intialize_LED():
    red_led.off()
    green_led.off()
    yellow_led.off()
