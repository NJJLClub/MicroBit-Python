#
# Written by: Jim Laderoute
# Date: 5/12/2017
#
from microbit import *
#  sleep, display, accelerometer, button_a, button_b, temperature
#  import Image
import random
import music
# import speech -- NOTE: using speech takes up too much memory


class myDrop:
    dropList = []

    def __init__(self, x, y):
        self.xreal = x * 1.0
        self.yreal = y * 1.0
        self.xpos = x
        self.ypos = y
        self.oldx = x
        self.oldy = y
        myDrop.dropList.insert(0, self)

    def occupied(me, x, y):
        for drop in myDrop.dropList:
            if (me != drop) and (drop.xpos == x) and (drop.ypos == y):
                return True
        return False

    def display(self):
        display.set_pixel(self.oldx, self.oldy, 0)
        display.set_pixel(self.xpos, self.ypos, 5)

    def update(self, rx, ry):
        x, y = self.xreal, self.yreal
        x = x + rx / 1000.0
        if x > 4.0:
            x = 4.0
        elif x < 0.0:
            x = 0.0

        y = y + ry / 1000.0
        if y > 4.0:
            y = 4.0
        elif y < 0.0:
            y = 0.0

        if not myDrop.occupied(self, int(x), int(y)):
            self.oldx, self.oldy = self.xpos, self.ypos
            self.xpos = int(x)
            self.ypos = int(y)
            self.xreal, self.yreal = x, y

#
# Create an object, a special effects object with many different effects
# methods.
#


class mySfx():

    def __init__(self):
        self.doFill = True
        self.doPlay = True
        self.mode = 0
        self.x = 0
        self.y = 0
        self.LASTMODE = 6
        self.dictionary = {}
        for num in range(0, 5):
            self.dictionary[num] = random.randint(0, 4)
        # Creating 5 drops of water (five instances of a myDrop object)
        for i in [0, 1, 2, 3, 4]:
            myDrop(i, i)

    def showTemp(self):
        display.scroll(str(round(temperature() * 1.8) + 32) + " f ")
        sleep(50)

    def playMusic(self):
        if self.doPlay:
            music.play(music.POWER_DOWN)
            # DADADADUM PRELUDE ENTERTAINER ODE NYAN RINGTONE FUNK BLUES
            # WEDDING FUNERAL PUNCHLINE PYTHON BADDY CHASE BA_DING WAWAWAWAA
            # BIRTHDAY JUMP_UP JUMP_DOWN POWER_UP POWER_DOWN
            self.doPlay = False
            display.set_pixel(0, 0, 8)

    def playTune(self):
        if self.doPlay:
            tune = ["C4:4", "D", "E", "C", "C", "D", "E"]
            music.play(tune)
            self.doPlay = False
            display.set_pixel(0, 0, 8)

    def playSiren(self):
        if self.doPlay:
            for freq in range(880, 1760, 16):
                music.pitch(freq, 6)
            for freq in range(1760, 880, -16):
                music.pitch(freq, 6)
            self.doPlay = False
            display.set_pixel(0, 0, 8)

#    def talk(self):
        #  You need to hook up a speaker to pins 0 and 1 for this to work
#        if self.doPlay:
#            speech.say("EXTERMINATE", speed=120, pitch=100, throat=100, mouth=200)
#            display.show(Image.MEH)  # can't run , not enough memory
#            self.doPlay = False
#            display.set_pixel(0, 0, 8)

    def waterDrops(self):
        for drop in myDrop.dropList:
            drop.update(accelerometer.get_x(), accelerometer.get_y())
            drop.display()
        sleep(10)

    def flashingStars(self):
        for tx in range(0, 5):
            self.y = self.dictionary[tx]
            display.set_pixel(tx, self.y, random.randint(0, 8))
            self.dictionary[tx] = random.randint(0, 4)
        sleep(50)
        display.clear()

    def fillAndEmpty(self):
        if self.doFill is True:
            display.set_pixel(self.x, self.y, 4)
        else:
            display.set_pixel(self.x, self.y, 0)

        self.x += 1
        if self.x > 4:
            self.x = 0
            self.y += 1

        if self.y > 4:
            self.y = 0
            self.doFill = not self.doFill

        sleep(20)

    def nextMode(self):
        if self.mode < self.LASTMODE:
            self.mode += 1
            if self.mode == 3:
                display.scroll("Music")
                self.doPlay = True
            elif self.mode == 4:
                display.scroll("Tune")
                self.doPlay = True
            elif self.mode == 5:
                display.scroll("Siren")
                self.doPlay = True

    def previousMode(self):
        if self.mode > 0:
            self.mode -= 1

    def runSfx(self):
        if self.mode == 0:  # flashingStars
            self.flashingStars()
        elif self.mode == 1:  # fillAndEmpty
            self.fillAndEmpty()
        elif self.mode == 2:  # waterDrops
            self.waterDrops()
        elif self.mode == 3:  # play music
            self.playMusic()
        elif self.mode == 4:  # play created tune
            self.playTune()
        elif self.mode == 5:  # play siren
            self.playSiren()
        elif self.mode == 6:  # show temperature
            self.showTemp()
        else:
            display.scroll("Illegal Mode " + str(self.mode))


#
# Here comes the setup code
#
sfx = mySfx()  # creating a special effects instance; runs it's __init__ method
random.seed(33)

while True:
    sfx.runSfx()

    if button_a.is_pressed():
        sfx.previousMode()
        display.clear()
        sleep(500)
    elif button_b.is_pressed():
        sfx.nextMode()
        display.clear()
        sleep(500)
