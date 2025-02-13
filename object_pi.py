class pi:
    def __init__ (self, green_led, red_led, yellow_led, raw_temperature, avg_temperature):
        self.green_led = green_led
        self.red_led = red_led
        self.yellow_led = yellow_led
        self.raw_temperature = []
        self.avg_temperature = avg_temperature

    def set_green_led(self, green_status):
        self.green_led = green_status
        return self.green_led
    
    def set_red_led(self, red_status):
        self.red_led = red_status
        return self.red_led
    
    def set_yellow_led(self, yellow_status):
        self.yellow_led = yellow_status
        return self.yellow_led
    
    def get_green_led(self):
        return self.green_led
    
    def get_red_led(self):
        return self.red_led
    
    def get_yellow_led(self):
        return self.yellow_led

    def update_avg_temperature(self):
        self.avg_temperature = (format(sum(self.raw_temperature)/len(self.raw_temperature), '.2f'))
        return self.avg_temperature

    def get_avg_temperature(self):
        return self.avg_temperature
    
    def get_raw_temperature(self):
        return self.raw_temperature

    def set_raw_temperature(self, current_temperature):
        self.raw_temperature.insert(0, current_temperature)  # Inserts at the beginning
        if len(self.raw_temperature) > 10:
            self.raw_temperature
        self.update_avg_temperature()
        return self.raw_temperature