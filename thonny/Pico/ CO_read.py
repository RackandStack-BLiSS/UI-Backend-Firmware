import board
import time
import analogio
import digitalio

#co = digitalio.DigitalInOut(board.GP26)  # GP25
#co.direction = digitalio.Direction.INPUT

sensor = analogio.AnalogIn(board.A0)
# returns 16 bit value from 0 - 65535
sensor_level = sensor.value

# converts bit values to voltage with Vref = 3.3 V
volts = (sensor_level*3.3)/(65535)
# first initialization calculation for Ro; Ro = [(5*20kohm)/(volts)] - 20kohm
# MUST be performed in clean air then replace !!
Ro = (5*20000)/(volts) - 20000

while True:
    Rs = (5*20000)/(volts) - 20000
    ratio = Rs/Ro
    print(ratio)
    if ratio <= 3 and ratio >= 1.5:
        print("~200 ppm")
    if ratio < 1.5 and ratio >= 1.1:
        print("~500 ppm")
    if ratio < 1.1 and ratio >= 0.8:
        print("~800 ppm")
    if ratio < 0.8 and ratio >= 0.75:
        print("~1000 ppm")
    if ratio < 0.75:
        print("Exceeding 1000 ppm")
        
    time.sleep(3)
    
