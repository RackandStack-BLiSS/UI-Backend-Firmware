# UI-Backend-Firmware
Contains developed firmware, backend, and frontend code for BLiSS's Rack-and-Stack project
# Getting Started with Thonny
We will be working with CircuitPython IDE from adafruit (NOT the same as Micropython) and using the text editor Thonny to upload code to the Raspberry Pi Pico. 
1) First, download Thonny using their website
2) Connect the pi pico to your computer and hold down bootsel while doing so to open up the drive titled 'RPI-...'. Do not close this as we need to put more files unto this drive
3) Make sure not to press the bootsel button every time you go to plug in the pico (only do it the first time), otherwise it will erase and overwrite previous code already on the device.
4) Download the following .uf2 file. This will install firmware unto the pico. https://circuitpython.org/board/raspberry_pi_pico/
5) Drag and drop unto the drive. This will change the drive name to CIRCUITPY.
6) Download adafruit blinka AND platform detect from the following zip files. [Adafruit_Blinka-8.51.0.zip](https://github.com/user-attachments/files/18597279/Adafruit_Blinka-8.51.0.zip)
[Adafruit_Python_PlatformDetect-3.77.0.zip](https://github.com/user-attachments/files/18597283/Adafruit_Python_PlatformDetect-3.77.0.zip)
7) Configure blinka by going into src/adafruit-blinka/microcontroller/ and deleting EVERYTHING except the rp2040 and rp2040.u2if folders
8) Configure platform-detect by just going to Adafruit_Python_PlatformDetect-3.77.0/adafruit_platform detect and selecting just that folder
9) IMPORTANT!!! Now drag both adafruitblinka/src AND adafruit_platform detect folders into the 'lib' folder on the CIRCUITPY drive
10) This will now have installed all the important circuitpython libraries. Remember to put all python code on the 'code.py' within the drive. Enjoy Thonny!
11) Later on, we will be separating each sensor into its own .py file and adding that to the lib folder. Then, in 'code.py' we will be importing those. This will make the code more organized and less confusing.
