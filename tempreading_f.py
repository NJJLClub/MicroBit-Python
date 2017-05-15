from microbit import *


while True:
    
    value = temperature()
    if button_a.is_pressed():
        display.scroll( str(value) + " c ")
    else:
        display.scroll( str( value * 1.8 + 32) + " f " )
        
    sleep(3000)
