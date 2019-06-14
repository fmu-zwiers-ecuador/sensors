# sensors
Scripts and libraries used to read the sensors and store data in a usable format

To use WaveShare BME280 and Adafruit TSL2591:
(Sensor Connection then Raspberry pi pin)

Connect TSL2591 to Raspberry Pi:
1. Connect VIn to Pin 1 (3v3)
2. Connect GND to Pin 6 (Ground)
3. Connect SCL to Pin 5 (I2C SCL)
4. Connect SDA to Pin 3 (I2C SDA)

Connect BME280 to Raspberry Pi (Uses SPI because I2C is in use by the TSL2591 and this is easier than readdressing):
1. Connect VCC to Pin 1 (3v3)
2. Connect GND to Pin 6 (Ground)
3. Connect SDA/MOSI to Pin 19 (SPI MOSI)
4. Connect SCL/SCK to Pin 23 (SPI SCLK)
5. Connect ADDR/MISO to Pin 21 (SPI MISO)
6. Connect CS to Pin 29 (GPIO Pin 5; This is changeable, but my script uses it like this)
