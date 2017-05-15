from microbit import *

showc = True  # default to degrees celsius

while True:
    value = temperature()
    if button_a.is_pressed():
        showc = False
    elif button_b.is_pressed():
        showc = True

    if showc is True:
        display.scroll(str(value) + " c ")
    else:
        display.scroll(str(round(value * 1.8) + 32) + " f ")

    for x in range(0, 5):
        display.set_pixel(x, 1, 5)
        sleep(1000)
