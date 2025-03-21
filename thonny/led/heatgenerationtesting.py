import array
import busio
import board
import digitalio
import time
import adafruit_max31856
import neopixel

SCK = board.GP18
MOSI = board.GP19
MISO = board.GP16
CS = board.GP7
spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)
cs = digitalio.DigitalInOut(CS)
cs.direction = digitalio.Direction.OUTPUT
thermocouple = adafruit_max31856.MAX31856(spi, cs)

num_pixels = 60
pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 1

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
white = (255,255,255)
off = (0,0,0)

pixels.set_light_pattern([white])

while True:
    try:
        temperature = thermocouple.temperature
        'print(f"Temperature: {temperature:.2f}°C")'
        print(f"{temperature:.2f}")
    except Exception as e:
        print(f"Error reading temperature: {e}")
    time.sleep(1)