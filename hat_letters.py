#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()
import time

raspberry = (225 , 0, 125)
white = (225,225,225)
cyan = (0,225,225)


sense.show_letter("A", text_colour = raspberry, back_colour = cyan)
time.sleep(1)
sense.show_letter("N", text_colour = white, back_colour = raspberry)
time.sleep(1)
sense.show_letter("A", text_colour = cyan, back_colour = white)
time.sleep(1)
sense.show_letter("N", text_colour = raspberry, back_colour = cyan)
time.sleep(1)
sense.show_letter("Y", text_colour = white, back_colour = raspberry)
time.sleep(1)
sense.show_letter("A", text_colour = cyan, back_colour = white)
time.sleep(1)

sense.clear()
