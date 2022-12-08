import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

i2c_oled = busio.I2C(scl=board.GP5, sda=board.GP4)
oled_bus = displayio.I2CDisplay(i2c_oled, device_address=0x3C)
oled = adafruit_displayio_ssd1306.SSD1306(oled_bus, width=128, height=64)

screen = displayio.Group()

# Hello World!
text = "Hello World!"
text_font = terminalio.FONT
text_color = 0xFFFFFF

text_area = label.Label(text_font, text=text, color=text_color, x=28, y=15)
screen.append(text_area)

oled.show(screen)

while True:
    pass