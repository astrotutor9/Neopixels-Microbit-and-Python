from microbit import *
import neopixel

ring = neopixel.NeoPixel(pin0, 16)

# set some variables for colours
red = (75, 0, 0)
green = (0, 75, 0)
blue = (0, 0, 75)
off = (0, 0, 0)

# define (def) a function and give it a clear, simple name.
# Here the colours are sent from the call at the bottom
# and renamed as use_this_colour.

def chase(use_this_colour):
    for led_number in range(0, 16):
        ring[led_number] = use_this_colour
        ring[led_number - 2] = off
        ring.show()
        sleep(50)

while True:
    chase(red)
    chase(green)
    chase(blue)