#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()
import time

i = 0.1
sense.show_message("Anu", i)
w = str(i)


guess = " "
while guess != "Anu":
    guess = str(raw_input("Guess the word: "))
    if guess != "Anu":
        i = i +0.1
        w = str(i)
        sense.show_message("Anu", i)
   
if guess == "Anu":
    sense.show_message ("Win - ")
    sense.show_message(w)

sense.clear()
