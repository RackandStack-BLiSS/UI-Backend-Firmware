import serial
import time

# Open serial port on GPIO14 (TX) and GPIO15 (RX) with 9600 baud rate
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=5)  # "/dev/serial0" is used for Raspberry Pi's UART

message_started = False
message = []

while True:
    if uart.in_waiting > 0:  # Check if data is available in the buffer
        byte_read = uart.read(1)  # Read one byte

        if byte_read == b"<":
            # Start of message. Start accumulating bytes, but don't record the "<".
            message = []
            message_started = True
            continue

        if message_started:
            if byte_read == b">":
                # End of message. Convert it to a string and split it.
                message_str = "".join(message)
                message_parts = message_str.split(",")
                print("Received message:", message_parts)
                message_started = False
                message = []
            else:
                # Accumulate message byte.
                message.append(byte_read.decode("utf-8"))

    else:
        time.sleep(3)  # Wait before checking again