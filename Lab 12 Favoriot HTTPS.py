import os
import time
import board
import ssl
import wifi
import socketpool
import adafruit_requests as requests
import adafruit_dht
import favoriot_ca

dht11 = adafruit_dht.DHT11(board.GP15)

ssid = os.getenv("WIFI_SSID")
password = os.getenv("WIFI_PASSWORD")

print("""
    ______                       _       __ 
   / ____/___ __   ______  _____(_)___  / /_
  / /_  / __ `/ | / / __ \/ ___/ / __ \/ __/
 / __/ / /_/ /| |/ / /_/ / /  / / /_/ / /_  
/_/    \__,_/ |___/\____/_/  /_/\____/\__/ v3.2.0""" + " (Microcontroller: " + os.uname()[0] + ")\n")

print("Connecting to '" + ssid + "' ... ", end="")

wifi.radio.connect(ssid, password)

print("connected.")
print()

pool = socketpool.SocketPool(wifi.radio)
context = ssl.create_default_context()
context.load_verify_locations(cadata=favoriot_ca.cert)
https = requests.Session(pool, context)

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
        dht11.exit()
        raise error
    
    time.sleep(2)
    
    if (now + 15) < time.monotonic():
        
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

        request = https.request(
            os.getenv("FAVORIOT_HTTPS_METHOD"),
            os.getenv("FAVORIOT_HTTPS_API"),
            timeout = 5,
            headers = headers,
            json = json
        )
        
        response = request.json()
        print("Favoriot HTTPS Request: ", end="")

        if response["statusCode"] == 201:
            print("Success: " + response["message"])
        else:
            print("Error: " + response["message"])
                
        request.close()
        
        print()