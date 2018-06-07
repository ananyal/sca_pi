#!/usr/bin/env python

from sense_hat import SenseHat
import time
import random
sense = SenseHat()



    
for x, c in enumerate('ANANYA'):
    r = random.randint(0,225)
    g= random.randint(0,225)
    b= random.randint(0,225)
    sense.show_letter(c,  (r,g,b))
    time.sleep(1)
  

sense.clear()
