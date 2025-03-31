import array
import busio
import board
import digitalio
import time
import adafruit_max31856
import neopixel
import circuitpython_csv as csv
import storage

SCK = board.GP18
MOSI = board.GP19
MISO = board.GP16
CS = board.GP7
spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)
cs = digitalio.DigitalInOut(CS)
cs.direction = digitalio.Direction.OUTPUT
thermocouple = adafruit_max31856.MAX31856(spi, cs)
header = ["Time  ", "  Temperature"]
start_time = time.time()

num_pixels = 60
pixels = neopixel.NeoPixel(board.GP4, num_pixels)
pixels.brightness = 0.45

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
white = (255,255,255)
off = (0,0,0)

pixels.set_light_pattern([white])

with open("thermocouple_data.csv", "w") as writablefile:
            csvwriter = csv.DictWriter(writablefile, header)
            csvwriter.writeheader()

while True:
    try:
        temperature = thermocouple.temperature
        seconds = int(time.time() - start_time)
        print(f"Time: {seconds} secs")
        print(f"Temperature: {temperature:.2f}°C\n")
        with open("thermocouple_data.csv", "a") as writablefile:
            csvwriter = csv.DictWriter(writablefile, header)
            csvwriter.writerow({"Time  ": str(seconds) + "  ", "  Temperature": "  " + str(temperature)})
    except Exception as e:
        seconds = int(time.time() - start_time)
        print(f"Error reading temperature: {e}")
    time.sleep