import os
import time
import board
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import digitalio
import pwmio
import json
import mqtt
import favoriot_ca

red = digitalio.DigitalInOut(board.GP2)
red.direction = digitalio.Direction.OUTPUT

yellow = digitalio.DigitalInOut(board.GP3)
yellow.direction = digitalio.Direction.OUTPUT

green = pwmio.PWMOut(board.GP4)

now = time.monotonic()

ssid = os.getenv('WIFI_SSID')
password = os.getenv('WIFI_PASSWORD')

print("""
    ______                       _       __ 
   / ____/___ __   ______  _____(_)___  / /_
  / /_  / __ `/ | / / __ \/ ___/ / __ \/ __/
 / __/ / /_/ /| |/ / /_/ / /  / / /_/ / /_  
/_/    \__,_/ |___/\____/_/  /_/\____/\__/ v3.0.0""" + " (Microcontroller: " + os.uname()[0] + ")\n")

print("Connecting to Wi-Fi '" + ssid + "' ... ", end="")

wifi.radio.connect(ssid, password)

print("connected.")

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
    broker="mqtt.favoriot.com",
    port=8883,
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