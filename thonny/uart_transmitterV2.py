import board
import busio
import digitalio
import adafruit_bmp3xx
import adafruit_scd4x
import adafruit_hdc302x
import apds9960
from DFRobot_Oxygen import *
import time

# Initializing i2c ports
scl = board.GP1
sda = board.GP0
i2c = busio.I2C(scl,sda)
# Starting sensors at i2c ports
scd4x = adafruit_scd4x.SCD4X(i2c)
scd4x.start_periodic_measurement()
hdc302x = adafruit_hdc302x.HDC302x(i2c)
bmp3xx = adafruit_bmp3xx.BMP3XX_I2C(i2c)
bmp3xx.sea_level_pressure = 1019
prox = apds9960.APDS9960(i2c)
prox.enable_proximity = True

# Further initializations for oxygen sensor
ADDRESS_3    = 0x73
COLLECT_NUMBER   = 10              # collect number, the collection range is 1-100
IIC_MODE         = 0x01            # default use IIC1
oxygen = DFRobot_Oxygen_IIC(IIC_MODE, ADDRESS_3);

# Enable uart connection
uart = busio.UART(board.GP16, board.GP17, baudrate=9600, timeout=0)
# setting up intervals to send UART buffer every 5 seconds
UPDATE_INTERVAL = 5.0
last_time_sent = 0

# setting GPIO pins as RYG output 
redSwitch_pin = digitalio.DigitalInOut(board.GP15)
redSwitch_pin.direction = digitalio.Direction.OUTPUT
yellowSwitch_pin = digitalio.DigitalInOut(board.GP14)
yellowSwitch_pin.direction = digitalio.Direction.OUTPUT
greenSwitch_pin = digitalio.DigitalInOut(board.GP13)
greenSwitch_pin.direction = digitalio.Direction.OUTPUT

# inquiring status of rack from rpi4 through UART
message_started = False
message = []

while True:
    try:
        # reading payload status to display RYG lights only every UPDATE_INTERVAL seconds.
        now = time.monotonic()
        if uart.in_waiting > 0:  # Check if data is available in the buffer
            byte_read = uart.read(1)  # Read one byte
            if byte_read == b"<":
                    # Start of message. Start accumulating bytes, but don't record the "<".
                message = []
                message_started = True
                continue
            if message_started:
                 if byte_read == b"g": # if status is good display green light
                    redSwitch_pin.value = False
                    yellowSwitch_pin.value = False
                    greenSwitch_pin.value = True  
                 if byte_read == b"r": # if status is bad display red light
                    redSwitch_pin.value = True
                    yellowSwitch_pin.value = False
                    greenSwitch_pin.value = False  
                 if byte_read == b"y": # if status is ok display yellow light
                    redSwitch_pin.value = False
                    yellowSwitch_pin.value = True
                    greenSwitch_pin.value =  False 
            else:
                # Accumulate message byte.
                message.append(byte_read.decode("utf-8"))
        else:
             time.sleep(5)  # Wait before checking again
             print(f"No Message Received...")
        # sending telemetry to rpi4 through UART
        if now - last_time_sent >= UPDATE_INTERVAL:
            uart.write(bytes(f"<p{bmp3xx.pressure}>","ascii"))
            uart.write(bytes(f"<t{hdc302x.temperature}>", "ascii"))
            uart.write(bytes(f"<h{hdc302x.relative_humidity}>", "ascii"))
            uart.write(bytes(f"<d{scd4x.CO2}>", "ascii"))
            uart.write(bytes(f"<x{prox.proximity}>", "ascii"))
            uart.write(bytes(f"<o{oxygen.get_oxygen_data(COLLECT_NUMBER)}>", "ascii"))

            print("Sending sensor values from Pico 1!")
            last_time_sent = now
    except KeyboardInterrupt:
        redSwitch_pin.value = False  # This sets the pin to 0V
        yellowSwitch_pin.value = False  # This sets the pin to 0V
        greenSwitch_pin.value = False  # This sets the pin to 0V
        print("Code execution interrupted by user")
        break

    

