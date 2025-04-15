import serial
import time

def Sensor_Reading():
    # Open serial port on GPIO14 (TX) and GPIO15 (RX) with 9600 baud rate (GPIO0 (TX)/GPIO1 (RX) for Pico)
    uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=5)  # "/dev/serial0" is used for Raspberry Pi's UART (14TX/15RX)

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

    Still_Messages = 1 # check messages in the buffer
    First_Time = True # if the first time running

    while Still_Messages > 0:
        if First_Time:
            Still_Messages = 1
        else:
            Still_Messages = uart.in_waiting
                
        
        if uart.in_waiting > 0:  # Check if data is available in the buffer
            First_Time = False
            byte_read = uart.read(1)  # Read one byte
                
            if byte_read == b"<":
                    # Start of message. Start accumulating bytes, but don't record the "<".
                message = []
                message_started = True
                continue

            if message_started:
                    
                if Sensor == NONE:
                    if byte_read == b"p":
                        # ~ print("Reading pressure data...")
                        Sensor = PRESSURE
                    elif byte_read == b"t":
                        # ~ print("Reading temperature data...")
                        Sensor = TEMPERATURE
                    elif byte_read == b"h":
                        # ~ print("Reading humidity data...")
                        Sensor = HUMIDITY
                    elif byte_read == b"o":
                        # ~ print("Reading oxygen data...")
                        Sensor = OXYGEN
                    elif byte_read == b"m":
                        # ~ print("Reading carbon monoxide data...")
                        Sensor = CO
                    elif byte_read == b"d":
                        # ~ print("Reading carbon dioxide data...")
                        Sensor = CO2
                    elif byte_read == b"x":
                        # ~ print("Reading proximity data...")
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
                            temperature = message_parts
                            print(f"Received temperature data: {message_parts} F")
                        elif Sensor == PRESSURE:
                            pressure = message_parts
                            print(f"Received pressure data: {message_parts}")
                        elif Sensor == HUMIDITY:
                            humidity = message_parts
                            print(f"Received humidity data: {message_parts}")
                        elif Sensor == OXYGEN:
                            oxygen = message_parts
                            print(f"Received oxygen data: {message_parts}")
                        elif Sensor == CO:
                            co = message_parts
                            print(f"Received carbon monoxide data: {message_parts}")
                        elif Sensor == CO2:
                            co2 = message_parts
                            print(f"Received carbon dioxide data: {message_parts}")
                        elif Sensor == PROXIMITY:
                            proximity = message_parts
                            print(f"Received proximity data: {message_parts}")
                        else:
                            print(f"Received unknown data: {message_parts}")
                                
                        #print("Received message:", message_parts)
                        message_started = False
                        Sensor = NONE
                        message = []
                
                    else:
                        # Accumulate message byte.
                        message.append(byte_read.decode("utf-8"))
                        
    uart.close()
    return temperature, pressure, humidity, oxygen, co, co2, proximity

# ~ temperature, pressure, humidity, oxygen, co, co2, proximity = Sensor_Reading()
# ~ print(temperature, pressure, humidity, oxygen, co, co2, proximity)
