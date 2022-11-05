import time
import board
import digitalio

red = digitalio.DigitalInOut(board.GP2)
red.direction = digitalio.Direction.OUTPUT

yellow = digitalio.DigitalInOut(board.GP3)
yellow.direction = digitalio.Direction.OUTPUT

green = digitalio.DigitalInOut(board.GP4)
green.direction = digitalio.Direction.OUTPUT

while True:
    green.value = True
    time.sleep(6)
    green.value = False
    
    yellow.value = True
    time.sleep(1)
    yellow.value = False
    
    red.value = True
    time.sleep(6)
    red.value = False
    
    