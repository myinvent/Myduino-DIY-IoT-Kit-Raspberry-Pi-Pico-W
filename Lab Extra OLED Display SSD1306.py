import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

i2c = busio.I2C(scl=board.GP5, sda=board.GP4)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Make the display context
screen = displayio.Group()
display.show(screen)

# Hello World!
text = "Hello World!"
text_font = terminalio.FONT
text_color = 0xFFFFFF

text_area = label.Label(text_font, text=text, color=text_color)

text_area.x = 28
text_area.y = 15

screen.append(text_area)

while True:
    pass