#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()

blue = (0, 0,225)
raspberry = (225, 0, 125)

speed = 0.1

message = "Anu Lingineni"

sense.show_message(message, speed, text_colour = raspberry, back_colour = blue)

sense.clear()
