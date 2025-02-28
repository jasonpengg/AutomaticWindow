# import the folder where the main logic takes place 
from src import *

import matplotlib.pyplot as plt

# gets the data, used for x axis  
def recent_data(pi_status, start_time):
    return round(time.time() - start_time), float(pi.get_avg_temperature(pi_status))

# Graph will update in live time, 
def update_graph(time_data, temperature_data, line, ax, pi_status, start_time):
    new_x, new_y = recent_data(pi_status, start_time)
    time_data.append(new_x)
    temperature_data.append(new_y)

    # keeps only the last 100 points (around 100s)
    if len(time_data) > 100:
        time_data.pop(0)
        temperature_data.pop(0)

    # handle x-axis limits, updates the limits so it is adaptable 
    if len(time_data) > 1:
        ax.set_xlim(min(time_data), max(time_data))
    # set limit to 0 and 5 to initialize the graph 
    else:
        ax.set_xlim(time_data[0], time_data[0] + 5)  

    # handle y-axis limits, makes the graph +/-1 of the temperature 
    if len(temperature_data) > 1:
        ax.set_ylim(min(temperature_data) - 1, max(temperature_data) + 1)
    # sets limit to +/-1 of the original data so there are no identical limits
    else:
        ax.set_ylim(temperature_data[0] - 1, temperature_data[0] + 1)  # Add buffer

    line.set_data(time_data, temperature_data)
    
    #allows GUI to update
    plt.pause(1)  

# method to initialize graph 
def setup_graph():
    fig, ax = plt.subplots()
    ax.set_title("Room Temperature Over Time")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Temperature (°C)")
    
    # makes the line red
    line, = ax.plot([], [], 'r-', label="Avg Temp")
    ax.legend()
    
    return fig, ax, line

 
def main(): 

    ## ----- INTIALIZE VARIABLES ------##
    button_press_count = 0 
    pi_status = pi(False, False, False, None, None, False, 0)
    sensor = Temperature_Sensor()
    start_time = time.time()
    intialize_LED()
    initialize_motor()

    # Set up the figure and axes 
    fig, ax, line = setup_graph()
    time_data, temperature_data = [], []
    
    # asks user for preferred temperature 
    preferred_temperature = int(input("What is your preferred temperature"))
    print("To change your temperature press the button")

    while(True):

        # checks for button press
        button_press_count = button_counter(button_press_count)
        led_control(button_press_count, pi_status)
        
        #updates and prints the rolling average 
        update_average(sensor, pi_status)

        try:
            update_graph(time_data, temperature_data, line, ax, pi_status, start_time)
        except:
            print("graph is closed, restart program")

        if text_input() == True:
            print("Program is Stopped")
            preferred_temperature = int(input("What is your preferred temperature"))
            print("To change again, press the button")
        
        if button_press_count == 1:
            close_window(pi_status)
        
        elif button_press_count == 2: 
            force_open_window(pi_status)
        
        elif button_press_count == 3:
            # every 5 seconds, it checks if the window should be manipulated 
            if (round(time.perf_counter()) % 5) == 0:
                print(time.perf_counter())
                window_condition(preferred_temperature, pi_status)
        time.sleep(1)
main()
