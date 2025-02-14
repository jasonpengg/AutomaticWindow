import time
from gpiozero import Button, LED

# Define LEDs
red_led = LED(5)
green_led = LED(7)
yellow_led = LED(6)

# Define button
button = Button(23)

def button_counter(button_press_count):
    """Updates the button press count and loops back to 1 after 3 presses."""
    if button.is_pressed:
        print("button Pressed")
        button_press_count += 1
        time.sleep(0.5)  # Debounce to avoid counting multiple presses
        if button_press_count > 3:  # Reset after the 3rd press
            button_press_count = 1
    return button_press_count

def led_control(button_press_count):
    """Controls which LED is on based on the button press count."""
    if button_press_count == 1:
        red_led.on()
        green_led.off()
        yellow_led.off()
    elif button_press_count == 2:
        red_led.off()
        green_led.on()
        yellow_led.off()
    elif button_press_count == 3:
        red_led.off()
        green_led.off()
        yellow_led.on()

def main():
    button_press_count = 0
    while True:
        button_press_count = button_counter(button_press_count)
        led_control(button_press_count)
        time.sleep(0.1)  # Short delay for responsiveness
