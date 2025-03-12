import board
import busio
import digitalio
import adafruit_bmp3xx
import time

# For most CircuitPython boards:
#led = digitalio.DigitalInOut(board.LED)

uart = busio.UART(board.GP16,board.GP17, baudrate=9600, timeout=5)

message_started = False

while True:
    byte_read = uart.read(32)  # Read one byte over UART lines
    
    if byte_read is None:
        time.sleep(3)
        continue
    else: print(byte_read)
    if chr(byte_read[0]) == "<":
    # Start of message. Start accumulating bytes, but don't record the "<".
        message = []
        message_started = True
        continue

    if message_started:
        print("hello im here")
        if chr(byte_read[0]) == ">":
            print("ending message")
            # End of message. Don't record the ">".
            # Now we have a complete message. Convert it to a string, and split it up.
            # print(message)
            message_parts = "".join(message).split(",")
            print(message_parts)
            message_type = message_parts[0]
            message_started = False
            message = []
        else:
            # Accumulate message byte.
            message.append(chr(byte_read[0]))
            # print(message)
        