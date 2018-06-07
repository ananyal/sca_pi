#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

touch_pin=31

led_pin = 11

GPIO.setup(led_pin, GPIO.OUT)

GPIO.setup(touch_pin, GPIO.IN)

while True:
    if GPIO.input(touch_pin) == 0:
        GPIO.output(led_pin, False)
    if GPIO.input(touch_pin) == 1:
        GPIO.output(led_pin, True)
      

GPIO.cleanup()
