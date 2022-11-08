import time
import board
import digitalio

motor = digitalio.DigitalInOut(board.GP3)
motor.direction = digitalio.Direction.OUTPUT

while True:
    motor.value = True
    time.sleep(1)
    motor.value = False
    time.sleep(1)