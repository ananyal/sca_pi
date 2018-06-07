#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

#breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin code
led_pin = 11

#set Auto Flash mode as output
GPIO.setup(led_pin, GPIO.OUT)

#turn on LED
GPIO.output(led_pin, True)
time.sleep(10)

#turn off
GPIO.output(led_pin, False)

#reset GPIO
GPIO.cleanup
