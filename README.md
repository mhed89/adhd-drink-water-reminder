# Water Reminder for XIAO RP2040

This CircuitPython project helps you remember to drink water using an RGB LED and a button on a Seeed Studio XIAO RP2040.

## What it does

- Blinks an LED every hour as a reminder.
- Press the button after drinking to reset the timer and count your water intake.

## Parts Needed

- Seeed Studio XIAO RP2040
- KY-009 RGB LED
- KY-004 Button
- Breadboard & Jumper Wires

## Wiring

| XIAO Pin | Connects To           |
|----------|-----------------------|
| D0       | KY-009 R (Red)        |
| D1       | KY-009 G (Green)      |
| D2       | KY-009 B (Blue)       |
| D3       | KY-004 S (Signal)     |
| 3.3V     | KY-004 VCC (+)        |
| GND      | Common Ground (-)     |

## How to Use

- **Startup:** You'll see a quick Red-Green-Blue flash sequence.
- **Reminder:** Every hour, the LED blinks blue/cyan for one minute. Time to drink!
- **Button Press:** After drinking, press the button.
    - The timer resets for another hour.
    - Your water count goes up by one (check the serial console if connected).
    - The LED flashes green a few times to confirm.

## Customize

You can change the timing in `code.py`:

```python
REMINDER_INTERVAL = 60 * 60  # How often to remind (seconds). Default: 1 hour
REMINDER_DURATION = 60       # How long the reminder blink lasts (seconds). Default: 1 minute
```

## Quick Test Mode

Want to test it faster?
1. Rename `test_accelerated.py` to `code.py`.
2. Copy it to your XIAO.
This version uses a 10-second interval and a 5-second reminder blink.

## LED Colors

- **Blue/Cyan Blink:** Drink water reminder.
- **Green Flashes:** Button pressed, timer reset.
- **Red -> Green -> Blue:** System starting up.

![Photo of the setup](/images/front.jpeg)
