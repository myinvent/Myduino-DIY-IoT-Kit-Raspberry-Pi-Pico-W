import os
import ssl
import time
import wifi
import json
import mqtt
import board
import busio
import displayio
import socketpool
import terminalio
import adafruit_display_text.label as label
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import adafruit_displayio_ssd1306
import adafruit_dht
import favoriot_ca
import digitalio
import pwmio

displayio.release_displays()

i2c_oled = busio.I2C(scl=board.GP5, sda=board.GP4)
oled_bus = displayio.I2CDisplay(i2c_oled, device_address=0x3C)
oled = adafruit_displayio_ssd1306.SSD1306(oled_bus, width=128, height=64)

dht11 = adafruit_dht.DHT11(board.GP15)

now = time.monotonic()

red = digitalio.DigitalInOut(board.GP2)
red.direction = digitalio.Direction.OUTPUT

yellow = digitalio.DigitalInOut(board.GP3)
yellow.direction = digitalio.Direction.OUTPUT

green = pwmio.PWMOut(board.GP4)

ssid = os.getenv("WIFI_SSID")
password = os.getenv("WIFI_PASSWORD")

print('''
    ______                       _       __ 
   / ____/___ __   ______  _____(_)___  / /_
  / /_  / __ `/ | / / __ \/ ___/ / __ \/ __/
 / __/ / /_/ /| |/ / /_/ / /  / / /_/ / /_  
/_/    \__,_/ |___/\____/_/  /_/\____/\__/ v3.0.0''' + ' (Microcontroller: ' + os.uname()[0] + ')\n')

print("Connecting to Wi-Fi '" + ssid + "' ... ", end="")

wifi.radio.connect(ssid, password)

print('connected.')

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)
context = ssl.create_default_context()
context.load_verify_locations(cadata=favoriot_ca.cert)

def pwm_map(x, a, b, c, d):
    x = int(x)
    y=(x-a)/(b-a)*(d-c)+c
    return int(y)

def mqtt_message(client, topic, message):
    # Method called when a client's subscribed feed has a new value.
    command = json.loads(message)
    print(command)
    
    if "red" in command:
        red.value = True if command["red"] == "ON" else False
    
    if "yellow" in command:
        yellow.value = True if command["yellow"] == "ON" else False
    
    if "green" in command:
        green.duty_cycle = pwm_map(command["green"], 0, 100, 0, 65535)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=os.getenv("FAVORIOT_MQTT_BROKER_HOST"),
    port=os.getenv("FAVORIOT_MQTT_BROKER_PORT"),
    username=os.getenv("FAVORIOT_DEVICE_ACCESS_TOKEN"),
    password=os.getenv("FAVORIOT_DEVICE_ACCESS_TOKEN"),
    socket_pool=pool,
    ssl_context=context,
)

# Connect callback handlers to mqtt_client
mqtt_client.on_connect = mqtt.connect
mqtt_client.on_disconnect = mqtt.disconnect
mqtt_client.on_subscribe = mqtt.subscribe
mqtt_client.on_publish = mqtt.publish
mqtt_client.on_message = mqtt_message

print("Connecting to MQTT broker '%s' with secure port ... " % mqtt_client.broker, end="")
mqtt_client.connect()

mqtt_client.subscribe("{}/v2/rpc".format(os.getenv("FAVORIOT_DEVICE_ACCESS_TOKEN")), qos=1)

while True:
    mqtt_client.loop(timeout=1)

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

    # time.sleep(2.0)

    if (now + 15) < time.monotonic():
        
        now = time.monotonic()
        
        data = {
            'device_developer_id': os.getenv('FAVORIOT_DEVICE_DEVELOPER_ID'),
            'data': {
                'temperature': temperature,
                'humidity': humidity
            }
        }
        
        mqtt_topic = '{}/v2/streams'.format(os.getenv('FAVORIOT_DEVICE_ACCESS_TOKEN'))
        
        mqtt_client.publish(mqtt_topic, json.dumps(data))
        print()