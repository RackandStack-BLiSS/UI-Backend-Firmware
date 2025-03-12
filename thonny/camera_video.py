#This code is for taking video with Pi Camera 3 Wide
#Code is from https://forums.raspberrypi.com/viewtopic.php?t=368757

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import time

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)
picam2.start_preview(Preview.QTGL)
encoder = H264Encoder(10000000) #10 mega pixel
picam2.start()

video_output = FfmpegOutput("test.mp4")
print("Start...")
picam2.start_recording(encoder,output=video_output)
time.sleep(10) # Recording duration in seconds
picam2.stop_recording()
print("...End")
picam2.stop()