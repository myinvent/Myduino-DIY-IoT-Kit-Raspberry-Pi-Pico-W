import time
import board
import analogio
import pwmio

analog_A0 = analogio.AnalogIn(board.GP26_A0)

led = pwmio.PWMOut(board.GP2)

while True:
    adc = analog_A0.value
    print(f"ADC Value: {adc}")
    
    voltage = (adc * 3.3) / 65536
    print(f"Voltage: {voltage:.2f} V")
    
    led.duty_cycle = adc
    
    print()
    time.sleep(0.1)