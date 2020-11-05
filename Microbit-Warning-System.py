moisture = 0
ALERT_MODE = False
"""

Welcome to your garden alert system

Author: Matt Berumen

Notes:

"""
# Button A is pressed in order to read moisture data
# and ensure our garden is not past the hydration threshold

def on_button_pressed_a():
    global moisture, ALERT_MODE
    # Power from P2 is taken in order to allow the buzzer to make noise until stopped
    basic.show_number(pins.analog_read_pin(AnalogPin.P1))
    moisture = pins.analog_read_pin(AnalogPin.P1)
    if moisture > 950:
        # Set alert mode to true and start alarm + fan spin
        ALERT_MODE = True
        # Fan turns on indefinitely
        pins.digital_write_pin(DigitalPin.P0, 1)
        while ALERT_MODE:
            pins.digital_write_pin(DigitalPin.P2, 1)
            # Buzzer beeps for half a sec
            basic.pause(500)
            pins.digital_write_pin(DigitalPin.P2, 0)
            basic.pause(500)
    elif moisture >= 500 and moisture <= 950:
        iamHappy = images.icon_image(IconNames.HAPPY)
        iamHappy.show_image(0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P2, 0)
    else:
        i = 0
        while i < 2:
            pins.digital_write_pin(DigitalPin.P2, 1)
            basic.pause(1000)
            pins.digital_write_pin(DigitalPin.P2, 0)
            iamSad = images.icon_image(IconNames.SAD)
            iamSad.show_image(0)
            i += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

# Button B is pressed in order stop alert system

def on_button_pressed_b():
    global ALERT_MODE
    # When the value is set to 0, the buzzer stops making noise until it is turned on again
    # pins.digital_write_pin(DigitalPin.P2, 0)
    # When button B is pressed, the alert system is deactivated, fan and buzzer turn off
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
    ALERT_MODE = False
input.on_button_pressed(Button.B, on_button_pressed_b)
