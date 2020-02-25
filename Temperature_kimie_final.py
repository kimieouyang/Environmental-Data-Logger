# Add your Python code here. E.g.
from microbit import *
# Please press any btn after you flash the code to microbit
# I don't know why I need to press it in order to trigger the program
# After you press any btn, the display would ask you to tilt the microbit to fill the lights
# I don't know why I have to complete the tilt action, I guess that's something with the compass heading function

# Setup
start_time = running_time()
# capture the current running time
wait_time = 10000
# wait for 10 seconds to print data

with open('data.csv', 'w') as my_file:
# Use the write function here to create an object file that I called it data.csv with a my_file variable name
    while True:
    # setup the loop logic to log the data every 10 seconds or any btn is pressed    
        any_button = button_a.is_pressed() or button_b.is_pressed()
        # Setup no matter which btn being pressed as one condition and set it as variable
        time_passed = running_time() - start_time
        # Setup this variable in order to determine how long since the microbit was started
        enough_time_passed = time_passed >= wait_time
        # This represent a variable as time passed equal or longer than 10 seconds since last time printed the data, 
        if any_button or enough_time_passed:
        # so if any btn is pressed or the time passed equal/longer than 10 seconds since last time printed the data
            temp = temperature()
            # capture current temperature from microbit sensor and name it as a variable 
            heading = compass.heading()
            # capture current heading from microbit sensor and name it as a variable
            csv_text = str(temp) + "," + str(heading)
            # make the temp and heading variables into strings for display/print usage
            display.scroll(csv_text)
            # show the temp and heading data as string and scroll it on microbit display
            my_file.write(csv_text + '\n')
            # write the data we captured into object file with a proper line break
            # so the data in the csv file would not all display in one line
            # it should look like
            # 26,89
            # 27,40
            # xx,xx
            start_time = running_time()
            # capture the current running time as a new start time
