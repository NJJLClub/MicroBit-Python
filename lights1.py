from microbit import *

x, y = 0, 0
brightness = 2
doset = True

while True:
    if (doset is True):
        display.set_pixel(x, y, brightness)
    else:
        display.set_pixel(x, y, 0)
        
    x += 1
    if (x > 4):
        x = 0
        y += 1

    if (y > 4):
        y = 0
        doset = not doset

    sleep(20)
