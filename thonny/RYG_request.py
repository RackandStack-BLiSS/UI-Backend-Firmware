import serial
import time

uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=5)  # "/dev/serial0" is used for Raspberry Pi's UART (14TX/15RX)

UPDATE_INTERVAL = 5.0
last_time_sent = 0

status = input("What is the status of the rack: [good/okay/bad]")

while True:
	now = time.monotonic()
	if now - last_time_sent >= UPDATE_INTERVAL:
		if status == "bad":
			uart.write(bytes(f"<r>"), "ascii") # turning on red light
		else if status == "okay":
			uart.write(bytes(f"<y>"), "ascii") # turning on yellow light
		else if status == "good":
			uart.write(bytes(f"<g>"), "ascii") # turnning on green light
		else:
			status = input("Unknown input, try again: [good/okay/bad]")
	
	if status == "good" or status == "okay" or status == "bad":
		print("Sending the status of the rack")
	last_time_sent = now
