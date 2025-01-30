# UI-Backend-Firmware
Contains developed firmware, backend, and frontend code for BLiSS's Rack-and-Stack project
# Getting Started with Thonny
1) First, download Thonny using their website
2) Connect the pi pico to your computer and hold down bootsel while doing so to open up the drive titled 'RPI-...'. Do not close this as we need to put more files unto this drive
3) Download the following .uf2 file. This will install firmware unto the pico. https://circuitpython.org/board/raspberry_pi_pico/
4) Drag and drop unto the drive. This will change the drive name to CIRCUITPY.
5) Download adafruit blinka AND platform detect from the following zip files. [Adafruit_Blinka-8.51.0.zip](https://github.com/user-attachments/files/18597279/Adafruit_Blinka-8.51.0.zip)
[Adafruit_Python_PlatformDetect-3.77.0.zip](https://github.com/user-attachments/files/18597283/Adafruit_Python_PlatformDetect-3.77.0.zip)
6) Configure blinka by going into src/adafruit-blinka/microcontroller/ and deleting EVERYTHING except the rp2040 and rp2040.u2if folders
7) Configure platform-detect by just going to adafruit_platform detect
8) IMPORTANT!!! Now drag both adafruitblinka/src AND adafruit_platform detect folders into the 'lib' folder on the CIRCUITPY drive
9) This will now have installed all the important circuitpython libraries. Remeber to put all python code on the 'code.py' within the drive. Enjoy Thonny!
