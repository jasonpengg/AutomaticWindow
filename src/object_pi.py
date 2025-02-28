# this class is used to initialize the pi as an object to store all its properties 
class pi:
    #constructor method for the object
    def __init__ (self, green_led, red_led, yellow_led, raw_temperature, avg_temperature, motor_status, window_status):
        self.green_led = green_led
        self.red_led = red_led
        self.yellow_led = yellow_led
        self.raw_temperature = []
        self.avg_temperature = avg_temperature
        self.motor_status = False
        self.window_status = 0

    def set_green_led(self, green_status):
        self.green_led = green_status

    def set_red_led(self, red_status):
        self.red_led = red_status
 
    def set_yellow_led(self, yellow_status):
        self.yellow_led = yellow_status

    def get_green_led(self):
        return self.green_led
    
    def get_red_led(self):
        return self.red_led
    
    def get_yellow_led(self):
        return self.yellow_led

    def update_avg_temperature(self):
        self.avg_temperature = (format(sum(self.raw_temperature)/len(self.raw_temperature), '.2f'))

    def get_avg_temperature(self):
        return self.avg_temperature
    
    def get_raw_temperature(self):
        return self.raw_temperature

    # raw temperature is an array that houses 30 items for the rolling average 
    def set_raw_temperature(self, current_temperature):
        self.raw_temperature.insert(0, current_temperature)  
        if len(self.raw_temperature) > 30:
            self.raw_temperature.pop()
        self.update_avg_temperature(self)

    def set_motor_status(self, motor_status):
        self.motor_status = motor_status
    
    def get_motor_status(self):
        return self.motor_status
    
    def set_window_status(self, window_status):
        self.window_status = window_status
    
    def get_window_status(self):
        return self.window_status