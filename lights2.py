# I call this FLASHING STARS
# Written by: Jim Laderoute
#
from microbit import *
import random

class mySfx():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dictionary = {}
        for num in range(0, 5):
            self.dictionary[num] = random.randint(0, 4)

    def flashingStars(self):
        for x in range(0, 5):
            self.y = self.dictionary[x]
            display.set_pixel(x, self.y, random.randint(0, 8))
            self.dictionary[x] = random.randint(0, 4)
        sleep(20)
        display.clear()


sfx = mySfx()
random.seed(33)

while True:
    sfx.flashingStars()
