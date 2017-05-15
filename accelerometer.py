from microbit import *

bright = 5
x, y = 0.0, 0.0
oldx, oldy = 0, 0


while True:
    readingx = accelerometer.get_x()
    readingy = accelerometer.get_y()

    # display.scroll( str( reading ))

    x = x + readingx / 1000.0
    if x > 4.0:
        x = 4.0
    elif x < 0.0:
        x = 0.0

    y = y + readingy / 1000.0
    if y > 4.0:
        y = 4.0
    elif y < 0.0:
        y = 0.0

    display.set_pixel(oldx, oldy, 0)
    display.set_pixel(int(x), int(y), bright)
    oldx, oldy = int(x), int(y)
#    display.scroll( str(int(x)) + ":" + str(int(y)) )
    sleep(10)
