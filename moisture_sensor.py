# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import RPi.GPIO as GPIO
import time
import board
import copy
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


# GPIO pin number where the relay is connected
RELAY_PIN = 20

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
# you can specify an I2C adress instead of the default 0x48
# ads = ADS.ADS1115(i2c, address=0x49)

# Create single-ended input on channel 0

# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)


try:
    while True:
        
        ai0 = AnalogIn(ads, ADS.P0)
        ai1 = AnalogIn(ads, ADS.P1)
        ai2 = AnalogIn(ads, ADS.P2)
        #print(str(ai0.value) + " " + str(ai1.value) + " " + str(ai2.value))        
        m0 = round((30-(round(ai0.value/1000)))*(100/30))
        m1 = round((30-(round(ai1.value/1000)))*(100/30))
        m2 = round((30-(round(ai2.value/1000)))*(100/30))
        #print(str(m0) + " " + str(m1) + " " + str(m2))
        time.sleep(2)
        
        avg = round((m0 + m1 + m2)/3)
        print(avg)
        if(avg <= 20):
            while (avg <= 50):
                GPIO.output(RELAY_PIN, GPIO.LOW)
                print("Relay is ON")
                print(avg)
                ai0 = AnalogIn(ads, ADS.P0)
                ai1 = AnalogIn(ads, ADS.P1)
                ai2 = AnalogIn(ads, ADS.P2)
                m0 = round(ai0.value/1000)
                m1 = round(ai1.value/1000)
                m2 = round(ai2.value/1000)
                avg = round((m0 + m1 + m2)/3)
                #print(str(m0) + " " + str(m1) + " " + str(m2))
                time.sleep(10)
            GPIO.output(RELAY_PIN, GPIO.HIGH)
        
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Cleaning up GPIO...")
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    GPIO.cleanup()

finally:
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    GPIO.cleanup()    
    #print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    #time.sleep(0.5)
