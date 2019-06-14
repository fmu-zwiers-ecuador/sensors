import board
import digitalio
import busio
import time
import adafruit_tsl2591
import adafruit_bme280
import datetime

# Open the file with the date as it's name in append mode so as not to overwrite existing data
file = open("/home/pi/Desktop/" + open("Node_ID").read() + ": " + datetime.datetime.now().strftime("%m-%d-%y") + ".json", "a")


# Create the objects needed to instantiate the sensors
i2c = busio.I2C(board.SCL, board.SDA)
spi = busio.SPI(board.SCK, MOSI = board.MOSI, MISO = board.MISO)
cs = digitalio.DigitalInOut(board.D5)

# Declare light sensing variables
lux = -1.0
ir = -1.0
fs = -1.0
vis = -1.0

# Declare environmental sensing variables
hum = -1.0
temp = -1.0
press = -1.0

try:
	sensor = adafruit_tsl2591.TSL2591(i2c)
	lux = sensor.lux
	ir = sensor.infrared
	fs = sensor.full_spectrum
	vis = sensor.visible
	
except:
	lux = lux

try:
	bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)
	hum = bme280.humidity
	temp = bme280.temperature
	press = bme280.pressure
except:
	hum = hum

# Actually write the data to the file
file.write("{\n")
file.write("\t\"time\": \"" + datetime.datetime.now().strftime("%H:%M:%S") + "\",\n")
file.write("\t\"temperature\": %0.1f" % temp + ",\n")
file.write("\t\"humidity\": %0.1f" % hum + ",\n")
file.write("\t\"pressure\": %0.1f" % press + ",\n")

file.write("\t\"lux\": {}".format(lux) + ",\n")
file.write("\t\"visible\": {}".format(vis) + ",\n")
file.write("\t\"infrared\": {}".format(ir) + ",\n")
file.write("\t\"fullSpectrum\": {}".format(fs) + "\n")
file.write("}\n")
