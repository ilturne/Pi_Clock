#!/usr/bin/env python3

# Import necessary libraries for communication and display use
import drivers
from time import sleep
from datetime import datetime

def get_current_time():
    """Retrieve current time and format it to display hours and minutes."""
    current_time = datetime.now()
    return current_time.strftime("%H:%M")

def main():
    # Initialize the LCD display
    display = drivers.Lcd()
    print("Writing to display")

    try:
        while True:
            # Fetch and format the current time
            time_formatted = get_current_time()

            # Write just the time to the display
            display.lcd_display_string(time_formatted, 1)

            # Refresh every second
            sleep(1)

    except KeyboardInterrupt:
        # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()

if __name__ == '__main__':
    main()
