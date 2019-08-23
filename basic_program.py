from microbit import *
# import all the import bits about a microbit & neopixels into the program

from microbit import *
import neopixel

# Setup the pin and how many LED are used as variable “ring”
# "ring" is just a word to name the variable

ring = neopixel.NeoPixel(pin0, 16)

# The colours are Red,Green,Blue
# Here 75 red with no green or blue
# Zero is no colour, 255 maximum colour brightness

ring[0] = (75, 0, 0)

# ring[0] is the first LED

ring.show()