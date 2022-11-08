import time
import board
import adafruit_dht

dht11 = adafruit_dht.DHT11(board.GP15)

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

    time.sleep(2.0)