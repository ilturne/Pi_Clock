#!/usr/bin/env python3

import drivers
from time import sleep, strftime
from datetime import datetime, timedelta
import RPi.GPIO as GPIO

# GPIO setup
BUTTON_PIN = 17  # Mode switch button
OPTION_BUTTON_PIN = 27  # Start/Stop/Reset button for Stopwatch and Timer
<<<<<<< HEAD
=======
SPEAKER_BUTTON_PIN = 13 # PIN With PWM availability
ENCODER_CH_A = 23
ENCODER_CH_B = 22
R_LED_PIN = 26  # Define the GPIO pin number for the Red LED


>>>>>>> alarm
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(OPTION_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SPEAKER_BUTTON_PIN, GPIO.OUT)
GPIO.setup(ENCODER_CH_A, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ENCODER_CH_B, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R_LED_PIN, GPIO.OUT)  # Setup the Red LED pin as an output

def timer_alarm():
    pwm.start(50)  # Start PWM for the speaker if it's a PWM speaker
    GPIO.output(R_LED_PIN, GPIO.HIGH)  # Turn on the LED
    try:
		for _ in range(5):
			for frequency in [392, 523, 784, 1046]:  # Different frequencies for the alarm
				pwm.ChangeFrequency(frequency)
				GPIO.output(R_LED_PIN, GPIO.HIGH)  # Ensure LED is on during sound
				sleep(0.2)  # Time period between frequency changes
				GPIO.output(R_LED_PIN, GPIO.LOW)  # Turn off LED briefly
				sleep(0.2)
    except KeyboardInterrupt:
        pwm.stop()
        pwm.ChangeDutyCycle(0)
        GPIO.cleanup()

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
    """Format timedelta to MM:SS:MS."""
<<<<<<< HEAD
    # Calculate total seconds in the timedelta
=======
>>>>>>> alarm
    total_seconds = int(td.total_seconds())
    minutes, seconds = divmod(total_seconds, 60)
    milliseconds = td.microseconds // 1000
    return "{:02}:{:02}:{:03}".format(minutes, seconds, milliseconds)

<<<<<<< HEAD
=======
def update_timer(encoder_a):
    global timer_set
    if GPIO.input(ENCODER_CH_B) != GPIO.input(ENCODER_CH_A):
        timer_set += timedelta(seconds=5)  # Increase by 5 seconds
    else:
        timer_set -= timedelta(seconds=5)  # Decrease by 5 seconds
        if timer_set.total_seconds() < 0:
            timer_set = timedelta(seconds=0)  # Prevent negative timer

timer_set = timedelta(minutes=5)
pwm = GPIO.PWM(SPEAKER_BUTTON_PIN, 1000)  # Initialize PWM on the speaker pin at 1000 Hz
pwm.start(50)  # Start PWM with 50% duty cycle


>>>>>>> alarm
def main():
    pwm.stop()
    global timer_set
    current_mode = "Clock"
    last_button_state = GPIO.HIGH
    stopwatch_running = False
    stopwatch_start = None
    stopwatch_elapsed = timedelta(0)
    timer_set = timedelta(minutes=5)  # Default timer setting
    timer_active = False
    timer_start_time = None
<<<<<<< HEAD
=======
    remaining_time = timedelta()  # Initialize remaining_time
>>>>>>> alarm

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
<<<<<<< HEAD
=======
                        timer_alarm() 
                        pwm.stop()
>>>>>>> alarm
                    else:
                        display.lcd_display_string(format_timedelta(remaining_time), 1)
                else:
                    display.lcd_display_string(format_timedelta(timer_set), 1)  # Display preset time

<<<<<<< HEAD
            # Handling button states and mode switching
=======
>>>>>>> alarm
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
<<<<<<< HEAD
=======
                        if (datetime.now() - timer_start_time).total_seconds() < 1:
                            timer_set = timedelta(minutes=5)  # Reset to default or a stored value
                            display.lcd_display_string(format_timedelta(timer_set), 1)
>>>>>>> alarm
                sleep(0.1)  # Debounce delay

            last_button_state = button_state
            last_option_button_state = option_button_state

            mode_display_text = "Mode: {}".format(current_mode)
            display.lcd_display_string(mode_display_text, 2)

            sleep(0.1)  # Short delay to reduce CPU usage

    except KeyboardInterrupt:
        display.lcd_clear()
        pwm.ChangeDutyCycle(0)
        pwm.stop()
        GPIO.cleanup()
        

GPIO.add_event_detect(ENCODER_CH_A, GPIO.BOTH, callback=update_timer, bouncetime=6)

if __name__ == '__main__':
    main()
