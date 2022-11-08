import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.GP15)

while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        
        print("Temperature: {} °C, Humidity: {} %RH ".format(temperature, humidity))

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)