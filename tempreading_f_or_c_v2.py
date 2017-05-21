from microbit import *

showf = True  # default to degrees celsius

while True:
    value = temperature()
    if button_a.was_pressed():
        showf = True
    elif button_b.was_pressed():
        showf = False

    if showf is True:
        display.scroll(str(round(value * 1.8) + 32) + " f ")
    else:
        display.scroll(str(value) + " c ")

    for x in range(0, 5):
        display.set_pixel(x, 1, 1)
        sleep(1000)
