import busio
import board
import digitalio
import adafruit_max31856
import time
import analogio

# SPI pins
SCK = board.GP18
MOSI = board.GP19
MISO = board.GP16

# Chip Select pins
CS1 = board.GP7
CS2 = board.GP3

# Create SPI bus (shared)
spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)

# Setup CS pins
cs1 = digitalio.DigitalInOut(CS1)
cs1.direction = digitalio.Direction.OUTPUT

cs2 = digitalio.DigitalInOut(CS2)
cs2.direction = digitalio.Direction.OUTPUT

# Create thermocouple objects
thermo1 = adafruit_max31856.MAX31856(spi, cs1)
thermo2 = adafruit_max31856.MAX31856(spi, cs2)

sensor = analogio.AnalogIn(board.A0)

# returns 16 bit value from 0 - 65535

start_time = time.time()

while True:
    try:
        temp1 = thermo1.temperature
    except Exception as e:
        temp1 = f"Error: {e}"

    try:
        temp2 = thermo2.temperature
    except Exception as e:
        temp2 = f"Error: {e}"
    
    try:
        sensor_level = sensor.value
    # converts bit values to voltage with Vref = 3.3 V
        volts = (sensor_level/65535)*(3.3)
    except Exception as e:
        volts = f"Error: {e}"

    elapsed = int(time.time() - start_time)

    
    print(f"[{elapsed}s] Probe: {temp1} °C | Surface: {temp2} °C | Transducer: {volts} V\n")
    
    time.sleep(2)