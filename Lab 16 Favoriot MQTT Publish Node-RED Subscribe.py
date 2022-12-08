import os
import time
import board
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import adafruit_dht
import json
import mqtt

now = time.monotonic()

dht11 = adafruit_dht.DHT11(board.GP15)

ssid = os.getenv('WIFI_SSID')
password = os.getenv('WIFI_PASSWORD')

print("""
    _   __          __           ____  __________ 
   / | / /___  ____/ /__        / __ \/ ____/ __ \/
  /  |/ / __ \/ __  / _ \______/ /_/ / __/ / / / /
 / /|  / /_/ / /_/ /  __/_____/ _, _/ /___/ /_/ / 
/_/ |_/\____/\__,_/\___/     /_/ |_/_____/_____/  v3.0.2""" + " (Microcontroller: " + os.uname()[0] + ")\n")

print("Connecting to Wi-Fi '" + ssid + "' ... ", end="")

wifi.radio.connect(ssid, password)

print("connected.")

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker="mqtt.favoriot.com",
    port=1883,
    username=os.getenv("FAVORIOT_DEVICE_ACCESS_TOKEN"),
    password=os.getenv("FAVORIOT_DEVICE_ACCESS_TOKEN"),
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

# Connect callback handlers to mqtt_client
mqtt_client.on_connect = mqtt.connect
mqtt_client.on_disconnect = mqtt.disconnect
mqtt_client.on_publish = mqtt.publish

print("Connecting to MQTT broker '{}' ... ".format(mqtt_client.broker), end="")
mqtt_client.connect()

while True:
    
    try:
        temperature = dht11.temperature
        humidity = dht11.humidity
        
        print("Temperature: {} °C, Humidity: {} %RH ".format(temperature, humidity))

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dht11.exit()
        raise error
    
    time.sleep(2)
    
    if (now + 15) < time.monotonic():
        
        now = time.monotonic()
        
        data = {
            "temperature": temperature,
            "humidity": humidity
        }
        
        mqtt_topic = "{}/v2/streams".format(os.getenv('FAVORIOT_DEVICE_ACCESS_TOKEN'))
        
        mqtt_client.publish(mqtt_topic, json.dumps(data))
        print()