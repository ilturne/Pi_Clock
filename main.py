#!/usr/bin/env python3

import drivers
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

# GPIO setup
BUTTON_PIN = 17  # GPIO 17 corresponds to physical pin 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LCD setup
display = drivers.Lcd()

def button_callback(channel):
    print("Button pressed!")

# Adding a debounce directly in the hardware interrupt setup
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=200)

def get_current_time():
    """Retrieve and format the current time."""
    return datetime.now().strftime("%H:%M:%S")

def main():
    try:
        while True:
            # Display the current time on the first line
            current_time = get_current_time()
            display.lcd_display_string(current_time, 1)

            # Use sleep to reduce CPU usage, button presses are handled by the callback
            sleep(0.1)

    except KeyboardInterrupt:
        # Cleanup the display and GPIO on Ctrl-C exit
        print("Cleaning up!")
        display.lcd_clear()
        GPIO.cleanup()

if __name__ == '__main__':
    main()