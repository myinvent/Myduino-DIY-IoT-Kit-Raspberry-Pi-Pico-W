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

ssid = os.getenv("WIFI_SSID")
password = os.getenv("WIFI_PASSWORD")

print("""
    ______                       _       __ 
   / ____/___ __   ______  _____(_)___  / /_
  / /_  / __ `/ | / / __ \/ ___/ / __ \/ __/
 / __/ / /_/ /| |/ / /_/ / /  / / /_/ / /_  
/_/    \__,_/ |___/\____/_/  /_/\____/\__/ v3.2.0""" + " (Microcontroller: " + os.uname()[0] + ")\n")

print("Connecting to Wi-Fi '" + ssid + "' ... ", end="")

wifi.radio.connect(ssid, password)

print("connected.")

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=os.getenv("FAVORIOT_MQTT_BROKER_HOST"),
    port=os.getenv("FAVORIOT_MQTT_BROKER_PORT"),
    username=os.getenv("FAVORIOT_DEVICE_ACCESS_TOKEN"),
    password=os.getenv("FAVORIOT_DEVICE_ACCESS_TOKEN"),
    socket_pool=pool
)

# Connect callback handlers to mqtt_client
mqtt_client.on_connect = mqtt.connect
mqtt_client.on_disconnect = mqtt.disconnect
mqtt_client.on_publish = mqtt.publish

print("Connecting to MQTT broker '%s' ... " % mqtt_client.broker, end="")
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
            "device_developer_id": os.getenv('FAVORIOT_DEVICE_DEVELOPER_ID'),
            "data": {
                "temperature": temperature,
                "humidity": humidity
            }
        }
        
        mqtt_topic = "{}/v2/streams".format(os.getenv('FAVORIOT_DEVICE_ACCESS_TOKEN'))
        
        mqtt_client.publish(mqtt_topic, json.dumps(data))
        print()