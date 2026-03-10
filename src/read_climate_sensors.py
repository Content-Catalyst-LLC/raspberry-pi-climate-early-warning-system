import time
import board
import busio
import adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

while True:
    print("Temperature:", bme280.temperature)
    print("Humidity:", bme280.humidity)
    print("Pressure:", bme280.pressure)
    print("---")
    time.sleep(10)
