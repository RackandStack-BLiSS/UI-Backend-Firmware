"""HDC302x simple test with formatted table output including temperature in Fahrenheit"""

import time
from time import sleep
import board
import busio
import adafruit_hdc302x
from sparkfun_serlcd import Sparkfun_SerLCD_I2C


scl = board.GP1
sda = board.GP0
scl2 = board.GP3
sda2 = board.GP2
i2c = busio.I2C(scl, sda)
i2c2 = busio.I2C(scl2, sda2)

temp_sensor = adafruit_hdc302x.HDC302x(i2c2)
serlcd = Sparkfun_SerLCD_I2C(i2c)

print(f"{'Time (s)':<10}{'Temperature (°C)':<20}{'Temperature (°F)':<20}{'Humidity (%)'}")
#f"{elapsed_time:<10.1f}{temperature_celsius:<20.1f}{temperature_fahrenheit:<20.1f}"
print("=" * 60)

start_time = time.time()
serlcd.set_backlight_rgb(200,200,200)
while True:
    serlcd.clear()
    elapsed_time = time.time() - start_time
    temperature_celsius = temp_sensor.temperature
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    humidity = temp_sensor.relative_humidity
    serlcd.write(f"temp: {temperature_fahrenheit} \n humidity:{humidity}")
    time.sleep(5)
