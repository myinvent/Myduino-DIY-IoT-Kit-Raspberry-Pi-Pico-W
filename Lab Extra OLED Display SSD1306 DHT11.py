import time
import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
import adafruit_dht
from adafruit_display_text import label

displayio.release_displays()

i2c_oled = busio.I2C(scl=board.GP5, sda=board.GP4)
oled_bus = displayio.I2CDisplay(i2c_oled, device_address=0x3C)
oled = adafruit_displayio_ssd1306.SSD1306(oled_bus, width=128, height=64)

dht11 = adafruit_dht.DHT11(board.GP15)

while True:
    try:
        temperature = dht11.temperature
        humidity = dht11.humidity
        
        print("Temperature: {} °C, Humidity: {} %RH ".format(temperature, humidity))
        
        screen = displayio.Group()
        
        text = "DHT11 SENSOR"
        text_font = terminalio.FONT
        text_color = 0xFFFFFF

        text_area = label.Label(text_font, text=text, color=text_color, x=0, y=10)
        screen.append(text_area)
        
        text = "Temperature: {} *C".format(temperature)
        text_area = label.Label(text_font, text=text, color=text_color, x=0, y=25)
        screen.append(text_area)

        text = "Humidity   : {} %RH".format(humidity)
        text_area = label.Label(text_font, text=text, color=text_color, x=0, y=37)
        screen.append(text_area)
        
        oled.show(screen)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dht11.exit()
        raise error

    time.sleep(2.0)