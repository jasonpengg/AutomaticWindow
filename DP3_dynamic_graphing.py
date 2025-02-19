
#Creating a graph which overtime shows the temperatue in the room, to communicate to the user how well the room is maintainig their desired temperature 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes 
fig, ax = plt.subplots()
scat = ax.scatter([],[])
line, = ax.plot([],[])

# Gets the data 
def recent_data():
    #put rolling avg function here (delete this comment when you're done with it) 
    new_x = np.random.rand(10)
    new_y = np.random.rand(10)
    return new_x, new_y

### Initialize the scatter and line plot limits 
def init():
    scat.set_offsets(np.c_[[],[]])
    line.set_data([],[])
    return scat, line

# Create the update function
def update(frame):
    # Fetch the latest data
    new_x, new_y = recent_data()
    
    # Update scatter plot
    scat.set_offsets(np.c_[new_x, new_y])
    
    # Update line plot (shows the general trend line over time) 
    line.set_data(new_x, new_y)
    
    # Adjust plot limits to show progression over time - do you want to reset the graph every time the user wants to see it or like should it include all the temp data from all time?idk
    ax.relim()
    ax.autoscale_view()
  
    return scat, line

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=200, init_func=init, blit=True)

# Show the plot
plt.show()



