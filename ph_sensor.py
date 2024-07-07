import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
# you can specify an I2C adress instead of the default 0x48
# ads = ADS.ADS1115(i2c, address=0x49)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P1)

# Replace with your actual offset value
Offset = 0.0

# Start an iterator thread so serial buffer doesn't overflow

def read_ph_sensor():
    buf = []  # buffer for reading analog values
    for _ in range(10):  # Get 10 sample values from the sensor to smooth the value
        buf.append(chan.voltage)
        time.sleep(0.01)

    # Sort the analog values from small to large
    buf.sort()

    avg_value = sum(buf[2:8]) / 6  # Take the average value of 6 center samples
    ph_value = avg_value * 5.0 / 1024 / 6  # Convert the analog value into voltage
    ph_value = 3.5 * ph_value + Offset  # Convert the voltage into pH value
    return ph_value

while True:
    ph_value = read_ph_sensor()
    print(f"pH: {ph_value:.2f}")