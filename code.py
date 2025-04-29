# Water Reminder System
# For Seeed Studio XIAO RP2040 with KY-009 RGB LED and KY-004 Button (6mm x 6mm tactile button on the soldered version)
# Reminds you to drink water every hour with customizable visual alerts
# Author: mhed89
# Created: 2025-04-24

import time
import board
import pwmio
import digitalio

# Hardware setup - RGB LED pins (PWM)
red_pin = pwmio.PWMOut(board.D0, frequency=1000, duty_cycle=0)
green_pin = pwmio.PWMOut(board.D1, frequency=1000, duty_cycle=0)
blue_pin = pwmio.PWMOut(board.D2, frequency=1000, duty_cycle=0)

# Hardware setup - Button pin
button_pin = digitalio.DigitalInOut(board.D3)
button_pin.direction = digitalio.Direction.INPUT
button_pin.pull = digitalio.Pull.UP

# Configuration
REMINDER_INTERVAL = 60 * 60  # Reminder frequency (seconds) - 1 hour
REMINDER_DURATION = 60       # How long reminder lasts (seconds) - 1 minute
BUTTON_DEBOUNCE_TIME = 0.2   # Prevent multiple triggers from one press

# LED control function - takes 0-65535 values for RGB
def set_color(r, g, b):
    red_pin.duty_cycle = r
    green_pin.duty_cycle = g
    blue_pin.duty_cycle = b

# Turn off all LED colors
def led_off():
    set_color(0, 0, 0)

# Startup sequence - visual indicator system is working
print("Water Reminder System Starting...")
for _ in range(3):
    set_color(65535, 0, 0)    # Red
    time.sleep(0.2)
    set_color(0, 65535, 0)    # Green
    time.sleep(0.2)
    set_color(0, 0, 65535)    # Blue
    time.sleep(0.2)
    led_off()
    time.sleep(0.2)

print("Water Reminder Active - Will remind you every HOUR")
print("Press the button after drinking water to reset the timer")

# Button state tracking
last_button_press = time.monotonic()
button_state = False
prev_button_state = False

# Reminder state tracking
last_reminder_time = time.monotonic()
reminder_active = False
reminder_end_time = 0
water_count = 0  # Daily water intake counter

while True:
    current_time = time.monotonic()
    
    # Read button with debounce protection
    prev_button_state = button_state
    button_state = not button_pin.value  # Active LOW with pull-up
    
    # Button press detection
    if button_state and not prev_button_state and (current_time - last_button_press) > BUTTON_DEBOUNCE_TIME:
        last_button_press = current_time
        
        # Reset timer and increment water count
        last_reminder_time = current_time
        water_count += 1
        print(f"Timer reset! You've had {water_count} glasses of water today.")
        
        # Visual confirmation - green flashes
        for _ in range(3):
            set_color(0, 65535, 0)  # Green
            time.sleep(0.1)
            led_off()
            time.sleep(0.1)
        
        # Cancel active reminder if present
        if reminder_active:
            reminder_active = False
    
    # Check if reminder time has been reached
    if not reminder_active and (current_time - last_reminder_time) >= REMINDER_INTERVAL:
        print("Time to drink water!")
        reminder_active = True
        reminder_end_time = current_time + REMINDER_DURATION
    
    # Handle active reminder - blue/cyan blinking pattern
    if reminder_active:
        if current_time > reminder_end_time:
            # Auto-turn off after duration expires
            reminder_active = False
            led_off()
        else:
            # Create alternating blue/cyan pattern
            if int(current_time * 2) % 2 == 0:
                set_color(0, 0, 65535)  # Blue
            else:
                set_color(0, 65535, 65535)  # Cyan
    
    # Prevent CPU overuse
    time.sleep(0.05)
