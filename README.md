# Water Reminder System

A CircuitPython-based water reminder that uses an RGB LED to remind you to drink water every hour. Press a button after drinking water to reset the timer and track your daily water intake. Plug it in to your computer/power supply, and have it beside you while working or studying.

## Components

- Seeed Studio XIAO RP2040 microcontroller
- KY-009 RGB LED module
- KY-004 Button module
- Small breadboard
- Jumper wires

## Features

- 🚰 Hourly water intake reminders
- 🔵 Visual reminders using blue/cyan LED pattern
- ✅ Button to log each glass of water consumed
- 🧮 Tracks daily water intake count
- 📊 Serial console output for monitoring

## Wiring

Connect components to your XIAO RP2040 as follows:

| XIAO RP2040 Pin | Component Connection          |
|-----------------|-------------------------------|
| D0              | KY-009 R (Red) pin            |
| D1              | KY-009 G (Green) pin          |
| D2              | KY-009 B (Blue) pin           |
| D3              | KY-004 S (Signal) pin         |
| 3.3V            | KY-004 VCC pin                |
| GND             | Common ground (breadboard)    |

### Ground Sharing (Breadboard Setup)

Since the XIAO has limited ground pins, use a breadboard to create a common ground:
1. Connect GND from XIAO to breadboard
2. Connect GND from KY-009 to same breadboard row
3. Connect GND from KY-004 to same breadboard row

## Installation

1. Install CircuitPython on your XIAO RP2040 if not already installed ([guide](https://wiki.seeedstudio.com/XIAO-RP2040-with-CircuitPython/))
2. Connect the board to your computer
3. Copy the `code.py` file to the root directory of the CircuitPython drive that appears
4. The program will start automatically

## Usage

- The system starts with a RGB test sequence
- Every hour, the LED will blink blue/cyan for 1 minute to remind you to drink water
- Press the button after drinking water to:
  - Reset the timer
  - Add 1 to your water count
  - Get green confirmation flashes

## Customization

Edit these values in the code to customize behavior:

```python
REMINDER_INTERVAL = 60 * 60  # Seconds between reminders (default: 1 hour)
REMINDER_DURATION = 60       # How long each reminder lasts (default: 1 minute)
```

## Testing Mode

To quickly test functionality, use the included `test_accelerated.py`:
1. Rename `test_accelerated.py` to `code.py`
2. Upload to your device
3. This version uses 10-second intervals and 5-second reminders

## Color Meanings

- **Blue/Cyan alternating**: Time to drink water
- **Green flashes**: Button press confirmed, timer reset
- **Red → Green → Blue sequence**: System startup check
