
from microbit import *
import random

#
# Special Effects Code - making use of the 5x5 pixels
#


class mySFX:
    def __init__(self):
        self.sfxNumber = 1
        self.sfxMax = 2
        self.speed = 100

    def wildBlink(self):
        display.set_pixel(random.randint(0, 4), random.randint(0, 4), random.randint(0, 8))
        sleep(20)

    def warpSpeed(self):
        points = {
            0: [0, 0],
            1: [1, 1],
            2: [2, 2]
            }
        display.clear()

        b_on = 9
        b_off = 0

        value = accelerometer.get_y()
        if value < -20:
            self.speed -= min(50, abs(value))
            if self.speed < 20: self.speed = 20
        elif value > 20:
            self.speed += min(50, value)
            if self.speed > 300: self.speed = 300

        for i in range(0, 3):
            display.set_pixel(2+points[i][0], 2+points[i][1], b_on-i)
            display.set_pixel(2-points[i][0], 2+points[i][1], b_on-i)
            display.set_pixel(2+points[i][0], 2-points[i][1], b_on-i)
            display.set_pixel(2-points[i][0], 2-points[i][1], b_on-i)
            sleep(self.speed)

        for i in range(0, 3):
            display.set_pixel(2+points[i][0], 2+points[i][1], b_off)
            display.set_pixel(2-points[i][0], 2+points[i][1], b_off)
            display.set_pixel(2+points[i][0], 2-points[i][1], b_off)
            display.set_pixel(2-points[i][0], 2-points[i][1], b_off)
            sleep(self.speed)

        sleep(100)

    def fadeX(self):
        points = {
            0: [0, 0],
            1: [1, 1],
            2: [2, 2]
            }
        display.clear()

        for b in range(8, -1, -1):
            for i in range(0, 3):
                display.set_pixel(2+points[i][0], 2+points[i][1], b)
                display.set_pixel(2-points[i][0], 2+points[i][1], b)
                display.set_pixel(2+points[i][0], 2-points[i][1], b)
                display.set_pixel(2-points[i][0], 2-points[i][1], b)
                sleep(10)
            sleep(50)
        sleep(500)

    def cycle(self, direction):
        self.sfxNumber += direction
        if self.sfxNumber > self.sfxMax: self.sfxNumber = self.sfxMax
        if self.sfxNumber < 0: self.sfxNumber = 0

    def runSfx(self):
        if self.sfxNumber == 0:
            self.wildBlink()
        elif self.sfxNumber == 1:
            self.warpSpeed()
        elif self.sfxNumber == 2:
            self.fadeX()


sfx = mySFX()
while True:
    sfx.runSfx()
    if button_b.was_pressed():
        sfx.cycle(1)
    elif button_a.was_pressed():
        sfx.cycle(-1)
