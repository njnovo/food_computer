import RPi.GPIO as GPIO
import time

# GPIO pin number where the relay is connected
RELAY_PIN = 20

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    while True:
        # Turn on the relay (assuming the relay is active LOW)
        GPIO.output(RELAY_PIN, GPIO.LOW)
        print("Relay is ON")
        time.sleep(5)  # 5 seconds delay
        
        # Turn off the relay
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        print("Relay is OFF")
        time.sleep(5)  # 5 seconds delay

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Cleaning up GPIO...")
    GPIO.cleanup()

finally:
    GPIO.cleanup()
