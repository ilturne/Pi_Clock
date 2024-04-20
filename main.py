#!/usr/bin/env python3

import drivers
import time
from datetime import datetime, timedelta
import RPi.GPIO as GPIO

# GPIO setup
BUTTON_PIN = 17  # Mode switch button
OPTION_BUTTON_PIN = 27  # Start/Stop/Reset button for Stopwatch and Timer
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
    modes = ["Clock", "Timer", "Stopwatch"]
    new_index = (modes.index(current_mode) + 1) % len(modes)
    return modes[new_index]

def format_timedelta(td):
    """Format timedelta to HH:MM:SS."""
    # Calculate total seconds in the timedelta
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def main():
    current_mode = "Clock"  # Start with Clock mode
    last_button_state = GPIO.HIGH
    stopwatch_running = False
    stopwatch_start = None
    stopwatch_elapsed = timedelta(0)
    timer_set = timedelta(minutes=5)  # Default timer setting
    timer_active = False
    timer_start_time = None

    try:
        while True:
            current_time = get_current_time()

            if current_mode == "Clock":
                display.lcd_display_string(current_time, 1)
            elif current_mode == "Stopwatch":
                if stopwatch_running:
                    current_elapsed = datetime.now() - stopwatch_start
                    stopwatch_display = format_timedelta(current_elapsed + stopwatch_elapsed)
                else:
                    stopwatch_display = format_timedelta(stopwatch_elapsed)
                display.lcd_display_string(stopwatch_display, 1)
            elif current_mode == "Timer":
                if timer_active:
                    elapsed = datetime.now() - timer_start_time
                    remaining_time = timer_set - elapsed
                    if remaining_time.total_seconds() <= 0:
                        timer_active = False
                        display.lcd_display_string("00:00:00", 1)  # Timer expired
                    else:
                        display.lcd_display_string(format_timedelta(remaining_time), 1)
                else:
                    display.lcd_display_string(format_timedelta(timer_set), 1)  # Display preset time

            # Handling button states and mode switching
            button_state = GPIO.input(BUTTON_PIN)
            if button_state == GPIO.LOW and last_button_state == GPIO.HIGH:
                current_mode = cycle_mode(current_mode)
                stopwatch_running = False
                stopwatch_elapsed = timedelta(0)
                timer_active = False  # Reset timer on mode switch
                sleep(0.1)  # Debounce delay

            option_button_state = GPIO.input(OPTION_BUTTON_PIN)
            if option_button_state == GPIO.LOW and last_option_button_state == GPIO.HIGH:
                if current_mode == "Stopwatch":
                    if stopwatch_running:
                        stopwatch_elapsed += datetime.now() - stopwatch_start
                        stopwatch_running = False
                    else:
                        stopwatch_start = datetime.now()
                        stopwatch_running = True
                elif current_mode == "Timer":
                    if not timer_active:
                        timer_start_time = datetime.now()
                        timer_active = True
                    else:
                        timer_active = False
                sleep(0.1)  # Debounce delay

            last_button_state = button_state
            last_option_button_state = option_button_state

            mode_display_text = f"Mode: {current_mode}"
            display.lcd_display_string(mode_display_text, 2)

            sleep(0.1)  # Short delay to reduce CPU usage

    except KeyboardInterrupt:
        display.lcd_clear()
        GPIO.cleanup()

if __name__ == '__main__':
    main()