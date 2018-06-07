#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

GPIO.setup(buzz_pin, GPIO.OUT)

Buzz = GPIO.PWM(buzz_pin, 1000)
Buzz.ChangeFrequency(400)

led_pin = 11

#set Auto Flash mode as output
GPIO.setup(led_pin, GPIO.OUT)

#turn on LED

import random
n = random.randint(1,10)

guess = 0
while guess != n:
    guess = int(raw_input("Guess a number from 1 to 10:"))
    if guess < n:
        print 'Guess is too low'
        Buzz.start(30)
        time.sleep(1)
        Buzz.stop()
    if guess > n:
        print 'Guess is too high'
        Buzz.start(30)
        time.sleep(1)
        Buzz.stop()

if guess == n:
    print 'You guessed it'
    GPIO.output(led_pin, True)
    time.sleep(10)
    GPIO.output(led_pin, False)


GPIO.cleanup()
