import time
import board
import analogio
import digitalio

analog_A0 = analogio.AnalogIn(board.GP26_A0)

led = digitalio.DigitalInOut(board.GP2)
led.direction = digitalio.Direction.OUTPUT

while True:
    adc = analog_A0.value
    print(f"ADC Value: {adc}")
    
    voltage = (adc * 3.3) / 65536
    print(f"Voltage: {voltage:.2f} V")
    
    if voltage < 1.5:
        led.value = True
    else:
        led.value = False
        
    print()
    time.sleep(0.1)