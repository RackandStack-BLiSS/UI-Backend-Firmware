import time
import board
import adafruit_scd4x
import adafruit_hdc302x
import adafruit_bmp3xx
import apds9960
import busio

# Initialize i2c ports on board
scl = board.GP1
sda = board.GP0
i2c = busio.I2C(scl,sda) # uses board.SCL and board.SDA

# Initialize UART with other picos - This is master so only recieves and no TX
#int baudrate = 9600;
#uart = busio.UART(None, board.RX, baudrate,)

# Starting sensors at i2c ports

scd4x = adafruit_scd4x.SCD4X(i2c)
scd4x.start_periodic_measurement()
hdc302x = adafruit_hdc302x.HDC302x(i2c)
bmp3xx = adafruit_bmp3xx.BMP3XX_I2C(i2c)
bmp3xx.sea_level_pressure = 1019
prox = apds9960.APDS9960(i2c)

print("Proximity Sensor: '0' indicates farthest away '255' is closest")
prox.enable_proximity = True
print("Waiting for first measurements hold on!....")
# Using first to setup timestamps for sensor readings
first = True

# Printing all sensor readings
while True:
    current_time = time.time()
    if first:
        start_time = current_time
        print(f"Timestamp: {(current_time - start_time)}")
        print(f"proximity: {prox.proximity}")
        print("bmp Temperature: {:5.2f} °C".format(bmp3xx.temperature))
        print(f"hdc Temperature: {hdc302x.temperature:0.1f}°C")
        print(f"Relative Humidity: {hdc302x.relative_humidity:0.1f}%")
        if scd4x.data_ready:
            print("Temperature: %0.1f *C" % scd4x.temperature)
            print("Humidity: %0.1f %%" % scd4x.relative_humidity)
            print("CO2: %d ppm" % scd4x.CO2)
        print("Pressure: {:6.1f}".format(bmp3xx.pressure))
        print("Altitude: {} meters".format(bmp3xx.altitude))
        time.sleep(5)

        # Printing out any UART sensor readings RX from other picos
#          data = uart.read(32)  # read up to 32 bytes
#         # print(data)  # this is a bytearray type
# 
#         if data is not None:
#             # convert bytearray to string
#             data_string = ''.join([chr(b) for b in data])
#             print(data_string, end="")