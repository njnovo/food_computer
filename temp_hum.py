import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 21
instance = dht11.DHT11(pin = 21)
result = instance.read()

if result.is_valid():
    print(f"Temperature: {((9/5)*result.temperature)+32}")
    print("Humidity: %-3.1f %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)