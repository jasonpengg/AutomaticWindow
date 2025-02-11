#from sensor_library import * 
#sensor = Temperature_Sensor()
from weatherapi import get_weather
#time will be determined and changed later, for now it is for rolling average 

time = 1 

def rolling_average():
    total_temperature = 0
    for i in range (10):
       print(i)
       total_temperature = total_temperature 




def main():
  temperature = get_weather()[0]
  weather_description = get_weather()[1]
  print(temperature)
  print(weather_description)

main()


    