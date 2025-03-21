import busio
import board
import digitalio
import adafruit_max31856
import time
import circuitpython_csv as csv
import storage

try:
    storage.remount("/", False)  # Ensure filesystem is writable
except AttributeError:
    print("storage module not available, skipping remount.")

SCK = board.GP18  # Change according to your wiring
MOSI = board.GP19  # Change according to your wiring
MISO = board.GP16  # Change according to your wiring
CS = board.GP7  # Change according to your wiring

# GND to GND
# 3V to VIN

# Create SPI bus
spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)

# Allocate a CS pin and set the direction
cs = digitalio.DigitalInOut(CS)
cs.direction = digitalio.Direction.OUTPUT

# Create a thermocouple object
thermocouple = adafruit_max31856.MAX31856(spi, cs)
header = ["Time  ", "  Temperature"]
start_time = time.time()

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
            #csvwriter.writerow(rowdicts: Iterable[Dict[str, Any]])
    except Exception as e:
        seconds = int(time.time() - start_time)
        print(f"Error reading temperature: {e}")

    time.sleep(2)  # Wait 2 seconds before next reading
