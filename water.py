from microbit import *


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


# Creating 5 drops of water (five instances of a myDrop object)
for i in [0, 1, 2, 3, 4]:
    adrop = myDrop(i, i)

while True:

    for drop in myDrop.dropList:
        drop.update(accelerometer.get_x(), accelerometer.get_y())
        drop.display()

    sleep(10)
