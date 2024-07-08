import Adafruit_DHT

# Set sensor type : Options are DHT11, DHT22 or AM2302
sensor = Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio = 4

# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
# This is useful because sometimes the sensor can be hard to read
# and a few retries might help.
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor). 
# If this happens try again!
if humidity is not None and temperature is not None:
    print(f'Temperature: {temperature:.1f}°C')
    print(f'Humidity: {humidity:.1f}%')
else:
    print('Failed to get reading. Try again!')
