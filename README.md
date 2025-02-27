Purpose 

Due to the number of features, and for the sake of organization, we separated the code into appropriate files and folders. The purpose of this document is to explain further each output, and file (in addition to the code comments, and the print statements on IDLE) and justify/clarify the use case of each feature.  

Overview of Files + How to Run Them  

The main function can be found in main.py, and the logic functions can be found in the source folder, src. The whole program is run through the main function, so there is no need to open the files in the logic folder to make the device work.  

The premise of our device is to compare outside and inside temperatures, and if the temperature outside is closer to the desired temperature (inputted by the user) than inside, the window will open. 
This device is for people who struggle with hand strength and mobility, and who cannot operate the crank on casement windows.  

Primary Features  

There are two distinct output devices, that operate on differently processed data; they are outlined as follows:  

Linear Actuator   

The linear actuator is activated based on the function that compares temperature data from the sensor, window_condition(), and temperature provided from the weather API (Application Programming Interface) file (which includes Hamilton weather data, for the prototype). The API enables the code to communicate with an external software that tracks weather data, to provide the most accurate outcome. This API is sourced from WeatherStack API  

By extension, the “Degrees_of_Opening” function determines how much to open the window, based on the temperature difference inside and outside. The greater the difference, the more the linear actuator opens, the more the window opens. For the prototype, we have simplified it to 3 modes the motor can bring the window to: fully closed, half open, fully opened.  

Additionally, the logic includes code that checks weather conditions, so the window will not open regardless if there is inclement weather.  

Dynamic Graph  

The dynamic graph updates using the rolling average data to show the user how well the room is maintaining its desired temperature. The graph displays the temperature with respect to time.  

The rolling average is obtained by averaging the temperature values collected by the sensor over the last 30 inputs. The rolling average ensures the device is not over-sensitive to the incoming data since it has a variety of data points to refer to.  

Additional Features 

These features were added to ensure that the device was user friendly, and better mimic what it would look like if it were to be in the market. They are outlined as follows:  

Button & LEDs  

The “Settings” function is exactly as its name implies and is for the user to decide what setting they want the device on. The “Button Counter” function keeps track of the number of times the button has been pressed, and then that data is put into the “Settings” function to determine what setting the user wants. 
If the button has been pressed 1x, the device is put into “Force Open” mode, meaning the actuator moves forward and opens the window, regardless of indoor/outdoor temperatures. If pressed 2x, then it triggers the main part of our code (the automated function; previously discussed under “Primary Features; Linear Actuator”). 
If pressed 3x, it triggers “Force Close” mode, which like “Force Open”, moves the actuator backwards, keeping the window closed regardless of indoor/outdoor temperatures. The “Button Counter” resets press 4, to 1, and will loop between 1-3 to be in line with the device features.  

The LEDs are put in place to ensure the setting the device is on is completely clear to the user and increases the accessibility by providing easy-to-understand indications of the device. Briefly, here are the LEDs, colors, and what they indicate:  

Green – Force Open Mode 

Yellow – Automatic Mode 

Red – Force Close Mode  

We used colors intuitive to each setting for further ease of understanding.  

 
