import time
import board
import digitalio

pushbutton = digitalio.DigitalInOut(board.GP15)
pushbutton.direction = digitalio.Direction.INPUT
pushbutton.pull = digitalio.Pull.DOWN

led = digitalio.DigitalInOut(board.GP2)
led.direction = digitalio.Direction.OUTPUT

while True:
    print(pushbutton.value)
    
    if pushbutton.value:
        led.value = True
    else:
        led.value = False