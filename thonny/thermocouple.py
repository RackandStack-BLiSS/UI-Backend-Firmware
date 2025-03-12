import busio
import board
import digitalio
import adafruit_max31856
import time

SCK = board.GP18  # Change according to your wiring
MOSI = board.GP19  # Change according to your wiring
MISO = board.GP16  # Change according to your wiring
CS = board.GP7  # Change according to your wiring

# Create SPI bus
spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)

# Allocate a CS pin and set the direction
cs = digitalio.DigitalInOut(CS)
cs.direction = digitalio.Direction.OUTPUT

# Create a thermocouple object
thermocouple = adafruit_max31856.MAX31856(spi, cs)

while True:
    try:
        temperature = thermocouple.temperature
        print(f"Temperature: {temperature:.2f}°C")
    except Exception as e:
        print(f"Error reading temperature: {e}")
    
    time.sleep(2)  # Wait 2 seconds before next reading