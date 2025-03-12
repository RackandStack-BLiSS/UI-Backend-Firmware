import adafruit_bmp3xx
import time
import board
import busio

scl = board.GP1
sda = board.GP0
i2c = busio.I2C(scl,sda)

bmp_sensor = adafruit_bmp3xx.BMP3XX_I2C(i2c) 

uart = busio.UART(board.GP16, None, baudrate=9600, timeout=5)

UPDATE_INTERVAL = 3.0
last_time_sent = 0

# Wait for the beginning of a message.

while True:
    # Send light sensor value only every UPDATE_INTERVAL seconds.
    now = time.monotonic()
    if now - last_time_sent >= UPDATE_INTERVAL:
        pressure = bmp_sensor.pressure
        uart.write(bytes(f"<{pressure}>", "ascii"))
        print(bytes(f"<{pressure}>", "ascii"))
        print("sending pressure value", pressure)
        last_time_sent = now