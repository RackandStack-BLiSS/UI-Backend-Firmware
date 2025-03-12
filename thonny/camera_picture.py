#This code is for taking picture with Pi Camera 3 Wide
#Code taken from https://github.com/raspberrypi/picamera2/blob/main/examples/capture_png.py
#Credit to Joban for finding this

# cd Desktop

# Capture a PNG while still running in the preview mode.

import time

from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)

preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

picam2.capture_file("test.png")