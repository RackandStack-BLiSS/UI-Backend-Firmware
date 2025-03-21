import board
import neopixel
import array, time
  
'Update this to match the number of NeoPixel LEDs connected to your board.'
num_pixels = 60
  
pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 1
red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
white = (255,255,255)
off = (0,0,0)

'''while True:
    pixels.fill((200, 0, 150))
    pixels[::3] = [green] * (len(pixels) // 3)
    time.sleep(0.1)
    pixels.fill(green)
    pixels[::3] = (200,0,150) * (len(pixels) // 3)
    time.sleep(0.1)
    pixels.fill((100, 50, 50))
    pixels[::3] = (0,0,255) * (len(pixels) // 3)
    time.sleep(0.1)'''
      
bpink = (214,2,112)
bpurple = (155,79,150)
bblue = (0,56,168)
"bpattern = [bpink,bpink,bpurple,bblue,bblue]"
pattern = [white]
  
pixels.set_light_pattern(pattern)
pixels.roll_pattern(pattern, 0.1)