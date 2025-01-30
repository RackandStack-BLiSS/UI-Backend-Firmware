# SPDX-FileCopyrightText: 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""HDC302x simple test"""

# import time
# import board
# import busio
# import adafruit_hdc302x
# 
# scl = board.GP1
# sda = board.GP0
# i2c = busio.I2C(scl,sda)
# sensor = adafruit_hdc302x.HDC302x(i2c)
# 
# while True:
#     print(f"Temperature: {sensor.temperature:0.1f}°C")
#     print(f"Relative Humidity: {sensor.relative_humidity:0.1f}%")
#     print()
#     time.sleep(2)
# SPDX-License-Identifier: Unlicense
import time
import board
import adafruit_scd4x
import adafruit_hdc302x
import adafruit_bmp3xx
import busio

scl = board.GP1
sda = board.GP0
i2c = busio.I2C(scl,sda) # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
scd4x = adafruit_scd4x.SCD4X(i2c)
# hdc302x = adafruit_hdc302x.HDC302x(i2c)
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

# print("Serial number:", [hex(i) for i in scd4x.serial_number])

scd4x.start_periodic_measurement()
print("Waiting for first measurement....")
first = True

while True:
    if scd4x.data_ready:
        current_time = time.time()
        if first:
            start_time = current_time
            first = False
        #print(f"Timestamp: {(current_time - start_time)}")
        #print("CO2: %d ppm" % scd4x.CO2)
        
        #print("Temperature: %0.1f *C" % scd4x.temperature)
        #print("Humidity: %0.1f %%" % scd4x.relative_humidity)
        
        #print(f"Temperature: {hdc302x.temperature:0.1f}°C")
        #print(f"Relative Humidity: {hdc302x.relative_humidity:0.1f}%")
            
        print("Pressure: {:6.1f}".format(bmp.pressure))
        print("Temperature: {:5.2f}".format(bmp.temperature))
        print()
    time.sleep(5)