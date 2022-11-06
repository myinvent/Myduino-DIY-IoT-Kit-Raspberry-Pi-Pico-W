import time
import board
import pwmio

led = pwmio.PWMOut(board.GP3)

while True:
    # Increment value from 0 to 65535 with 1000 steps of number.
    for brightness in range(0, 65535, 1000):
        led.duty_cycle = brightness
        time.sleep(0.01)
        
    # Decrement value from 65535 to 0 with 1000 steps of number.
    for brightness in range(65535, 0, -1000):
        led.duty_cycle = brightness
        time.sleep(0.01)