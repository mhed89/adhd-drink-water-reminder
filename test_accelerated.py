# TESTING VERSION: Accelerated Water Reminder with RGB LED and Reset Button
# For Seeed Studio XIAO RP2040 + KY-009 RGB LED + KY-004 Button
# CircuitPython version
# Accelerated timers for easy testing

import time
import board
import pwmio
import digitalio

# Set up the RGB LED pins (using PWM)
red_pin = pwmio.PWMOut(board.D0, frequency=1000, duty_cycle=0)
green_pin = pwmio.PWMOut(board.D1, frequency=1000, duty_cycle=0)
blue_pin = pwmio.PWMOut(board.D2, frequency=1000, duty_cycle=0)

# Set up the button pin
button_pin = digitalio.DigitalInOut(board.D3)
button_pin.direction = digitalio.Direction.INPUT
button_pin.pull = digitalio.Pull.UP  # Enable pull-up resistor

# Define color setting function (65535 = full brightness, 0 = off)
def set_color(r, g, b):
    red_pin.duty_cycle = r
    green_pin.duty_cycle = g
    blue_pin.duty_cycle = b

# Turn off LED
def led_off():
    set_color(0, 0, 0)

# ACCELERATED TESTING settings (fast timers)
REMINDER_INTERVAL = 10  # 10 seconds (instead of 1 hour)
REMINDER_DURATION = 5   # 5 seconds (instead of 1 minute)
BUTTON_DEBOUNCE_TIME = 0.2

# Display startup sequence
print("*** ACCELERATED TEST MODE ***")
print("Water Reminder System Testing...")
for _ in range(3):
    set_color(65535, 0, 0)    # Red
    time.sleep(0.2)
    set_color(0, 65535, 0)    # Green
    time.sleep(0.2)
    set_color(0, 0, 65535)    # Blue
    time.sleep(0.2)
    led_off()
    time.sleep(0.2)

print("TEST MODE: Reminder every 10 seconds")
print("Press the button to reset the timer")

# Setup for button debouncing
last_button_press = time.monotonic()
button_state = False
prev_button_state = False

# Main loop variables
last_reminder_time = time.monotonic()
reminder_active = False
reminder_end_time = 0
water_count = 0  # Count how many glasses of water

# Countdown timer display
def display_countdown(seconds):
    print(f"Next reminder in {seconds} seconds")

while True:
    current_time = time.monotonic()
    
    # Read button state with debounce
    prev_button_state = button_state
    button_state = not button_pin.value  # Button is active LOW with pull-up
    
    # Check if button was just pressed (with debounce)
    if button_state and not prev_button_state and (current_time - last_button_press) > BUTTON_DEBOUNCE_TIME:
        last_button_press = current_time
        
        # Button pressed - reset timer and show confirmation
        last_reminder_time = current_time
        water_count += 1
        print(f"Timer reset! You've had {water_count} glasses of water.")
        
        # Show green confirmation flash
        for _ in range(3):
            set_color(0, 65535, 0)  # Green flash for confirmation
            time.sleep(0.1)
            led_off()
            time.sleep(0.1)
        
        # If reminder was active, turn it off
        if reminder_active:
            reminder_active = False
            print("Reminder canceled by button press")
    
    # Display countdown (only in test mode)
    time_since_last = current_time - last_reminder_time
    time_until_next = max(0, REMINDER_INTERVAL - time_since_last)
    if int(time_until_next) % 2 == 0 and not reminder_active:
        set_color(10000, 0, 0)  # Very dim red to show it's running
    else:
        led_off()
    
    # Check if it's time for a new reminder
    if not reminder_active and time_since_last >= REMINDER_INTERVAL:
        print("TIME TO DRINK WATER!")
        reminder_active = True
        reminder_end_time = current_time + REMINDER_DURATION
    
    # Handle active reminder (blinking blue)
    if reminder_active:
        if current_time > reminder_end_time:
            # End of reminder duration
            reminder_active = False
            led_off()
            print("Reminder ended")
        else:
            # Blink the LED during reminder
            if int(current_time * 2) % 2 == 0:
                set_color(0, 0, 65535)  # Blue light for water
            else:
                set_color(0, 65535, 65535)  # Cyan light
    
    # Small delay to prevent CPU hogging
    time.sleep(0.1)
