import serial
import time
# import gpiozero
# import board
# import busio
import time
from picamera2 import Picamera2, Preview
from picamera2.outputs import FfmpegOutput
from picamera2.encoders import H264Encoder
# Open serial port on GPIO14 (TX) and GPIO15 (RX) with 9600 baud rate (GPIO0 (TX)/GPIO1 (RX) for Pico)
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=5)  # "/dev/serial0" is used for Raspberry Pi's UART (14TX/15RX)
uart2 = serial.Serial("/dev/ttyAMA2", baudrate=9600, timeout=5)  # "/dev/serial0" is used for Raspberry Pi's UART (0TX/1RX)
# uart = serial.Serial("/dev/ttyAMA3", baudrate=9600, timeout=5)  # "/dev/serial0" is used for Raspberry Pi's UART (4TX/5RX)
print("UART Serial Port Opened: ", uart.name)
print("UART Serial Port Opened: ", uart2.name)


# Senosor types
PRESSURE = 1
TEMPERATURE = 2
HUMIDITY = 3
OXYGEN = 4
CO = 5
CO2 = 6
PROXIMITY = 7
NONE = 0

Sensor = NONE

message_started = False

message = []

# while True:
#     print(uart.in_waiting)
#     print(uart.read(1))

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)
picam2.start_preview(Preview.QTGL)
encoder = H264Encoder(10000000)
picam2.start()

#video_output = FfmpegOutput("test3.mp4")
#print("starting")

#picam2.start_recording(encoder, output = video_output)
# time.sleep(10)
updateInterval = 10
lastTime = 0

while True:
    now = time.monotonic()
    if (now - lastTime) >= updateInterval:
        picam2.capture_file(f"test_capture{now}.jpg")
                        #picam2.stop_recording()
        lastTime = now
        # ~ picam2.close()
    if uart.in_waiting > 0:  # Check if data is available in the buffer
        byte_read = uart.read(1)  # Read one byte
            
        if byte_read == b"<":
                # Start of message. Start accumulating bytes, but don't record the "<".
            message = []
            message_started = True
            continue

        if message_started:
                
            if Sensor == NONE:
                if byte_read == b"p":
                    print("Reading pressure data...")
                    Sensor = PRESSURE
                elif byte_read == b"t":
                    print("Reading temperature data...")
                    Sensor = TEMPERATURE
                elif byte_read == b"h":
                    print("Reading humidity data...")
                    Sensor = HUMIDITY
                elif byte_read == b"o":
                    print("Reading oxygen data...")
                    Sensor = OXYGEN
                elif byte_read == b"m":
                    print("Reading carbon monoxide data...")
                    Sensor = CO
                elif byte_read == b"d":
                    print("Reading carbon dioxide data...")
                    Sensor = CO2
                elif byte_read == b"x":
                    print("Reading proximity data...")
                    Sensor =  PROXIMITY
                else:
                    print(f'Sensor {byte_read.decode("utf-8")} not recognized. Stopping program.')
                    exit(1)
                continue
            
            if Sensor != NONE:
                    
                if byte_read == b">":
                    # End of message. Convert it to a string and split it.
                    message_str = "".join(message)
                    message_parts = message_str.split(",")
                    message_parts = float(message_parts[0])
                    
                    if Sensor == TEMPERATURE:
                        print(f"Received temperature data: {message_parts} F")
                    elif Sensor == PRESSURE:
                        print(f"Received pressure data: {message_parts}")
                    elif Sensor == HUMIDITY:
                        print(f"Received humidity data: {message_parts}")
                    elif Sensor == OXYGEN:
                        print(f"Received oxygen data: {message_parts}")
                    elif Sensor == CO:
                        print(f"Received carbon monoxide data: {message_parts}")
                    elif Sensor == CO2:
                        print(f"Received carbon dioxide data: {message_parts}")
                    elif Sensor == PROXIMITY:
                        print(f"Received proximity data: {message_parts}")
                    else:
                        print(f"Received unknown data: {message_parts}")
                            
#                     print("Received message:", message_parts)
                    message_started = False
                    Sensor = NONE
                    message = []
            
                else:
                    # Accumulate message byte.
                    message.append(byte_read.decode("utf-8"))
                    
    if uart2.in_waiting > 0:  # Check if data is available in the buffer
        byte_read = uart2.read(1)  # Read one byte
            
        if byte_read == b"<":
                # Start of message. Start accumulating bytes, but don't record the "<".
            message = []
            message_started = True
            continue

        if message_started:
                
            if Sensor == NONE:
                if byte_read == b"p":
                    print("Reading pressure data...")
                    Sensor = PRESSURE
                elif byte_read == b"t":
                    print("Reading temperature data...")
                    Sensor = TEMPERATURE
                elif byte_read == b"h":
                    print("Reading humidity data...")
                    Sensor = HUMIDITY
                elif byte_read == b"o":
                    print("Reading oxygen data...")
                    Sensor = OXYGEN
                elif byte_read == b"m":
                    print("Reading carbon monoxide data...")
                    Sensor = CO
                elif byte_read == b"d":
                    print("Reading carbon dioxide data...")
                    Sensor = CO2
                elif byte_read == b"x":
                    print("Reading proximity data...")
                    Sensor =  PROXIMITY
                else:
                    print(f'Sensor {byte_read.decode("utf-8")} not recognized. Stopping program.')
                    exit(1)
                continue
            
            if Sensor != NONE:
                    
                if byte_read == b">":
                    # End of message. Convert it to a string and split it.
                    message_str = "".join(message)
                    message_parts = message_str.split(",")
                    message_parts = float(message_parts[0])
                    
                    if Sensor == TEMPERATURE:
                        print(f"Received temperature data: {message_parts} F")
                    elif Sensor == PRESSURE:
                        print(f"Received pressure data: {message_parts}")
                    elif Sensor == HUMIDITY:
                        print(f"Received humidity data: {message_parts}")
                    elif Sensor == OXYGEN:
                        print(f"Received oxygen data: {message_parts}")
                    elif Sensor == CO:
                        print(f"Received carbon monoxide data: {message_parts}")
                    elif Sensor == CO2:
                        print(f"Received carbon dioxide data: {message_parts}")
                    elif Sensor == PROXIMITY:
                        print(f"Received proximity data: {message_parts}")
                    else:
                        print(f"Received unknown data: {message_parts}")
                            
#                     print("Received message:", message_parts)
                    message_started = False
                    Sensor = NONE
                    message = []
            
                else:
                    # Accumulate message byte.
                    message.append(byte_read.decode("utf-8"))

#    else:
#         time.sleep(3)  # Wait before checking again
         # ~ print(f"No Message Received...")

picam2.close()
uart.close()
       

