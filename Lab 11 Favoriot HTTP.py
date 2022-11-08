import os
import time
import board
import ssl
import wifi
import socketpool
import microcontroller
import adafruit_requests as requests
import adafruit_dht

dht11 = adafruit_dht.DHT11(board.GP15)

ssid = os.getenv('WIFI_SSID')
password = os.getenv('WIFI_PASSWORD')

print("Connecting to '" + ssid + "' ... ", end="")

wifi.radio.connect(ssid, password)

print("connected.")
print()

pool = socketpool.SocketPool(wifi.radio)
http = requests.Session(pool, ssl.create_default_context())

now = time.monotonic()

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
        dhtDevice.exit()
        raise error
    
    time.sleep(2)
    
    if (now + 10) < time.monotonic():
        
        now = time.monotonic()
    
        headers = {
            "content-type": "application/json",
            "apikey": os.getenv('FAVORIOT_DEVICE_ACCESS_TOKEN')
        }
        
        json = {
            "device_developer_id": os.getenv('FAVORIOT_DEVICE_DEVELOPER_ID'),
            "data": {
                "temperature": temperature,
                "humidity": humidity
            }
        }

        request = http.request(
            "POST",
            "http://apiv2.favoriot.com/v2/streams",
            timeout = 5,
            headers = headers,
            json = json
        )
        
        response = request.json()

        if response["statusCode"] == 20150:
            print("HTTP Success: " + response["message"])
        else:
            print("HTTP Error: " + response["message"])
                
        request.close()