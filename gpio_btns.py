#!/usr/bin/env python3

"""
Setup/handle Raspberry PI GPIO input
"""

PIN_NEXT = 10
PIN_PREV = 8
PIN_VOLUME_DOWN = 5
PIN_VOLUME_UP = 7

PIN_CMDS = {
    10 : "next",
    8 : "previous",
    11 : "volume down 5",
    13 : "volume up 5",
    7 : "pause"
}

def button_pressed(pin):
    """
    Callback function for button press event
    """
    from spotify_if import spotify_cmd
    ret = spotify_cmd(PIN_CMDS[pin])
    print("Pin:{} - {}".format(pin, PIN_CMDS[pin]))
    if ret != 0:
        print("Command next not successfull")


def init_gpio_buttons():
    """
    Initialize GPIO buttons from to pins from PIN_CMDS
    """
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD) #set physical pin numbering
    for pin in PIN_CMDS:
        print("Setting GPIO pin {} to command {}".format(pin, PIN_CMDS[pin]))
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=button_pressed)
