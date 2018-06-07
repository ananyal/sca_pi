#!/usr/bin/env python

from sense_hat import SenseHat
import time
import random
sense = SenseHat()

r = random.randint(0,225)
g= random.randint(0,225)
b= random.randint(0,225)


sense.show_letter("A", (r,g,b))
time.sleep(1)
r = random.randint(0,225)
g= random.randint(0,225)
b= random.randint(0,225)
sense.show_letter("N", (r,g,b))
time.sleep(1)
r = random.randint(0,225)
g= random.randint(0,225)
b= random.randint(0,225)
sense.show_letter("A", (r,g,b))
time.sleep(1)
r = random.randint(0,225)
g= random.randint(0,225)
b= random.randint(0,225)
sense.show_letter("N", (r,g,b))
time.sleep(1)
r = random.randint(0,225)
g= random.randint(0,225)
b= random.randint(0,225)
sense.show_letter("Y", (r,g,b))
time.sleep(1)
r = random.randint(0,225)
g= random.randint(0,225)
b= random.randint(0,225)
sense.show_letter("A", (r,g,b))
time.sleep(1)

sense.clear()
