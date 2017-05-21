
from microbit import *
import random

#
# Special Effects Code - making use of the 5x5 pixels
#


class mySFX:
    def __init__(self):
        self.sfxNumber = 3
        self.sfxMax = 3
        self.speed = 100

        self.counter = 0
        self.im_dead = False
        self.me_x = 2
        self.me_y = 2

        self.alien_x = 2
        self.alien_y = 0
        self.alien_vx = 0
        self.alien_vy = 0
        self.alien_bright = 9


        self.sweep_x = 0
        self.sweep_y = 0
        self.dim_step = 0
        self.fader = 9
        self.sweep_step = 0
        self.alienBoard = Image(
            "00000:"
            "00000:"
            "00000:"
            "00000:"
            "00000:")

    def captured_presses(self):
        return ( self.sfxNumber == 3)

    def wildBlink(self):
        display.set_pixel(random.randint(0, 4), random.randint(0, 4),
                random.randint(0, 8))
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
            if self.speed < 20:
                self.speed = 20
        elif value > 20:
            self.speed += min(50, value)
            if self.speed > 300:
                self.speed = 300

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

    def alienHunt(self):

        if button_a.is_pressed() and button_b.is_pressed():
            self.cycle(1)

        if self.im_dead is True:
            self.fadeX()
            self.counter += 1
            if self.counter < 10:
                return
            else:
                self.alien_x = 0
                self.alien_y = 0
                self.me_x = 2
                self.me_y = 2
                self.im_dead = False

        if self.alien_x == self.me_x and self.alien_y == self.me_y:
            self.im_dead = True
            self.counter = 0        

        if button_a.was_pressed():
            self.me_x -= 1
            if self.me_x < 0:
                self.me_x = 4
        if button_b.was_pressed():
            self.me_x += 1
            if self.me_x > 4:
                self.me_x = 0

        display.show(self.alienBoard)
        display.set_pixel( self.me_x, self.me_y, 9)
        self.counter += 1
        self.sweep_step += 1
        self.dim_step += 1
        if self.sweep_step % 4 == 0:
            self.sweep_x += 1
            if self.sweep_x > 4:
                self.sweep_x = 0
                self.sweep_y += 1
                if self.sweep_y > 4:
                    self.sweep_y = 0
                    self.sweep_x = 0

        if self.sweep_x != self.me_x or self.sweep_y != self.me_y:
            display.set_pixel(self.sweep_x, self.sweep_y, 1)

        if self.alien_bright > 0:
            display.set_pixel(self.alien_x, self.alien_y, self.alien_bright)
            if self.dim_step & 8 == 0:  # slowly dim the object
                self.alien_bright -= 1

        if self.sweep_x == self.alien_x and self.sweep_y == self.alien_y:
            self.alien_bright = 9

        if self.counter % 40 == 0:
            self.alien_x += random.randint(-1, 1)
            self.alien_y += random.randint(-1, 1)
            if self.alien_x < 0:
                self.alien_x = 0
            if self.alien_x > 4:
                self.alien_x = 4
            if self.alien_y < 0:
                self.alien_y = 0
            if self.alien_y > 4:
                self.alien_y = 4

        sleep(20)

    def fadeX(self):
        points = {
            0: [0, 0],
            1: [1, 1],
            2: [2, 2]
            }
        display.clear()

        for b in range(9, 0, -1):
            for i in range(0, 3):
                display.set_pixel(2+points[i][0], 2+points[i][1], b)
                display.set_pixel(2-points[i][0], 2+points[i][1], b)
                display.set_pixel(2+points[i][0], 2-points[i][1], b)
                display.set_pixel(2-points[i][0], 2-points[i][1], b)
                sleep(10)
            sleep(50)
        sleep(100)

    def cycle(self, direction):
        self.sfxNumber += direction
        if self.sfxNumber > self.sfxMax:
            self.sfxNumber = 0
        if self.sfxNumber < 0:
            self.sfxNumber = self.sfxMax

    def runSfx(self):
        if self.sfxNumber == 0:
            self.wildBlink()
        elif self.sfxNumber == 1:
            self.warpSpeed()
        elif self.sfxNumber == 2:
            self.fadeX()
        elif self.sfxNumber == 3:
            self.alienHunt()


sfx = mySFX()
while True:
    sfx.runSfx()
    
    if not sfx.captured_presses():
        if button_b.was_pressed():
            sfx.cycle(1)
        elif button_a.was_pressed():
            sfx.cycle(-1)
