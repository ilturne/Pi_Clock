# Pi_Clock Project

## Introduction
The Pi_Clock project combines a real-time clock and multi-functional timer into a single device, built using a Raspberry Pi 3. It features a user-friendly interface with an LCD for display, buttons for mode selection, and a rotary encoder for setting times. This device can function as a clock, alarm, or timer, providing both visual and audible notifications.

## Hardware Requirements
- Raspberry Pi 3
- LCD screen with Hardware Driver
- Rotary Encoder
- Push Buttons (for mode selection and confirmation)
- LED (for visual indication of alarms)
- Speaker (for audio output)
- Breadboard and connecting wires
- External power supply for Raspberry Pi

## Software Requirements
- Python 3.x installed on Raspberry Pi
- RPi.GPIO library for interfacing with GPIO pins
- `drivers` library for handling the LCD

## Installation Instructions
1. **Setup the Raspberry Pi**: Ensure your Raspberry Pi 3 is set up with the latest version of Raspberry Pi OS and connected to the internet.
2. **Connect the hardware components**: Following the schematic provided in the project documentation, connect the LCD, rotary encoder, buttons, LED, and speaker to the designated GPIO pins on the Raspberry Pi.
3. **Install Python Libraries**:
   - Update the package list: `sudo apt update`
   - Install Python GPIO library: `sudo apt install python3-rpi.gpio`
4. **Deploy the Code**:
   - Transfer the provided `Pi_Clock.py` file to your Raspberry Pi using a USB drive or over SSH.
   - Ensure that all paths to custom libraries and scripts in your Python code are correctly set.

## Usage Instructions
- **Starting the Clock**: Run the script using the command `python3 Pi_Clock.py` from the terminal.
- **Switching Modes**: Use the "MODE" button to toggle between Clock, Alarm, and Timer modes.
- **Setting the Alarm/Timer**:
  - In Alarm or Timer mode, use the rotary encoder to adjust the time.
  - Press the "ENTER" button to confirm the time setting.
- **Monitoring and Outputs**:
  - The LCD will display the current time or countdown timer based on the selected mode.
  - When the alarm or timer reaches the set time, the speaker will emit an alarm sound and the LED will flash.

## Code Overview
The provided script `Pi_Clock.py` controls the operation of the clock, timer, and alarm functionalities:
- **GPIO Setup**: Configures the pins for input from buttons and the rotary encoder, and output to the speaker and LED.
- **Timer and Alarm Functions**: Includes functions to handle the countdown timer, check the current time, and trigger the alarm with sound and light.
- **Main Loop**: Runs continuously, updating the display based on the selected mode and checking for user interactions via buttons and the encoder to set or reset times.

## Troubleshooting and Support
- **Common Issues**:
  - If the LCD does not display, check all connections and ensure the `drivers` library is correctly installed.
  - If the alarm or timer does not trigger, verify the GPIO pin connections and ensure the script has the correct pin numbers configured.

## Credits and Acknowledgements
This project was developed by Ryan Kulasekara and Ilya Turner as part of the ECE381 course under the guidance of Dr. Klingensmith. Special thanks to the Raspberry Pi community for the extensive resources and libraries which made this project possible.
