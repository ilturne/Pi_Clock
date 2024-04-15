#! /usr/bin/env python

# Import necessary libraries for communication and display use
import drivers
from time import sleep
from datetime import datetime

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first

display = drivers.Lcd()

#Function calls for system settings
current_time = datetime.now()
time_formatted = current_time.strftime("%H:%M")

try:
    print("Writing to display")
    while True:
        # Write just the time to the display
        display.lcd_display_string(str(time_formatted), 1)
        sleep(1)
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
