#!/usr/bin/env python3

import drivers
from time import sleep, strftime
from datetime import datetime
import RPi.GPIO as GPIO

# GPIO setup
BUTTON_PIN = 17  # Mode switch button
OPTION_BUTTON_PIN = 27  # Alarm time setting option button
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(OPTION_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LCD setup
display = drivers.Lcd()

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
    last_option_button_state = GPIO.HIGH
    alarm_time = "00:00:00"
    alarm_setting_option = "H"

    try:
        while True:
            current_time = get_current_time()

            # Display the current time or alarm time on the first line
            if current_mode == "Clock":
                display.lcd_display_string(current_time, 1)
            elif current_mode == "Alarm":
                display.lcd_display_string(alarm_time, 1)
                # Additional functionality to set the alarm will go here

            # Check for mode switch button press (change of state)
            button_state = GPIO.input(BUTTON_PIN)
            if button_state == GPIO.LOW and last_button_state == GPIO.HIGH:
                current_mode = cycle_mode(current_mode)
                sleep(0.1)  # Debounce delay

            # Check for option button press (change of state)
            option_button_state = GPIO.input(OPTION_BUTTON_PIN)
            if option_button_state == GPIO.LOW and last_option_button_state == GPIO.HIGH:
                # Here you'll cycle between H, M, and S and update alarm_setting_option
                if alarm_setting_option == "H":
                    alarm_setting_option = "M"
                elif alarm_setting_option == "M":
                    alarm_setting_option = "S"
                else:
                    alarm_setting_option = "H"
                sleep(0.1)  # Debounce delay
                # Implementation of setting the alarm option will be added later

            # Update the last button states
            last_button_state = button_state
            last_option_button_state = option_button_state

            # Display the current mode on the second line
            mode_display_text = "Mode: {} {}".format(current_mode, alarm_setting_option if current_mode == "Alarm" else "")
            display.lcd_display_string(mode_display_text, 2)

            sleep(0.1)  # Short delay to reduce CPU usage

    except KeyboardInterrupt:
        # Cleanup the display and GPIO on Ctrl-C exit
        display.lcd_clear()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
