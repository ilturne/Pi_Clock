#!/usr/bin/env python3

import drivers
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

# GPIO setup
BUTTON_PIN = 11  # Change this based on your wiring
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LCD setup
display = drivers.Lcd()

def test_button():
    """Test the button and print a message when it is pressed."""
    while True:
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == GPIO.LOW:
            print("Button has been pressed!")
            sleep(0.1)  # Debounce delay
        sleep(0.1)  # Short delay to reduce CPU usage

test_button()

def get_current_time():
    """Retrieve and format the current time."""
    return datetime.now().strftime("%H:%M:%S")

def cycle_mode(current_mode):
    """Cycle through the mode options."""
    modes = ["Clock", "Timer", "Stopwatch", "Alarm"]
    new_index = (modes.index(current_mode) + 1) % len(modes)
    return modes[new_index]

def main():
    current_mode = "Clock"  # Start with Clock mode
    last_button_state = GPIO.HIGH

    try:
        while True:
            # Display the current time on the first line
            current_time = get_current_time()
            display.lcd_display_string(current_time, 1)

            # Check for button press (change of state)
            button_state = GPIO.input(BUTTON_PIN)
            if button_state == GPIO.LOW and last_button_state == GPIO.HIGH:
                # Button has been pressed
                current_mode = cycle_mode(current_mode)
                sleep(0.1)  # Debounce delay

            # Update the last button state
            last_button_state = button_state

            # Display the current mode on the second line
            display.lcd_display_string(f"Mode: {current_mode}", 2)

            sleep(0.1)  # Short delay to reduce CPU usage

    except KeyboardInterrupt:
        # Cleanup the display and GPIO on Ctrl-C exit
        display.lcd_clear()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
