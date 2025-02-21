from Logic import *
#Creating a graph which overtime shows the temperatue in the room, to communicate to the user how well the room is maintainig their desired temperature 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

start_time = time.time()

# Gets the data 
def recent_data(pi_status):
    return round(time.time() - start_time), float(pi.get_avg_temperature(pi_status))


# Create the update function
def update_graph(time_data, temperature_data, line, ax, pi_status):
    new_x, new_y = recent_data(pi_status)
    time_data.append(new_x)
    temperature_data.append(new_y)

    # Keep only the last 100 points
    if len(time_data) > 100:
        time_data.pop(0)
        temperature_data.pop(0)

    # Handle x-axis limits
    if len(time_data) > 1:
        ax.set_xlim(min(time_data), max(time_data))
    else:
        ax.set_xlim(time_data[0] - 5, time_data[0] + 5)  # Add buffer to prevent identical limits

    # Handle y-axis limits
    if len(temperature_data) > 1:
        ax.set_ylim(min(temperature_data) - 1, max(temperature_data) + 1)
    else:
        ax.set_ylim(temperature_data[0] - 1, temperature_data[0] + 1)  # Add buffer

    line.set_data(time_data, temperature_data)
    plt.pause(1)  # Allow GUI to update

def setup_graph():
    fig, ax = plt.subplots()
    ax.set_title("Room Temperature Over Time")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Temperature (°C)")
    
    line, = ax.plot([], [], 'r-', label="Avg Temp")
    ax.legend()
    
    return fig, ax, line
# Create the animation

# Show the plot

 
def main(): 
    print ("hi")


    ## ----- INTIALIZE VARIABLES ------### 
    button_press_count = 0 
    pi_status = pi(False, False, False, None, None, False, 0)
    sensor = Temperature_Sensor()

    
    
    # Set up the figure and axes 
    fig, ax, line = setup_graph()
    time_data, temperature_data = [], []
    
    # input("What is your preferred temperature")
    preferred_temperature = 23
    
    while(True):

        button_press_count = button_counter(button_press_count)
        led_control(button_press_count, pi_status)
        update_average(sensor, pi_status)

        update_graph(time_data, temperature_data, line, ax, pi_status)
        
        if button_press_count == 1:
            close_window(pi_status)
            print("window is closed")
           
        elif button_press_count == 2: 
            force_open_window(pi_status)
            print("window is open")
        
        elif button_press_count == 3:
            if (round(time.perf_counter()) % 5) == 0:
                print(time.perf_counter())
                window_conditon(preferred_temperature, pi_status)
        time.sleep(1)
main()
