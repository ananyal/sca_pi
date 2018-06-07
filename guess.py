#!/usr/bin/env python

import random
n = random.randint(1,10)

guess = 0
while guess != n:
    guess = int(raw_input("Guess a number from 1 to 10:"))
    if guess < n:
        print 'Guess is too low'
    if guess > n:
        print 'Guess is too high'

if guess == n:
    print 'You guessed it'
