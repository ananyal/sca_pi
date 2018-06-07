#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

i = 1
while i < 101:
    x = random.randint(0,7)
    y =random.randint(0,7)
    r = random.randint(0,225)
    g= random.randint(0,225)
    b= random.randint(0,225)
    sense.set_pixel(x, y, (r,g,b))
    time.sleep(0.25)
    i = i+1
    sense.clear()

sense.clear()


