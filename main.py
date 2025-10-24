from machine import Pin
from neopixel import NeoPixel
from time import sleep
from Common.Const.gpio_map import GPIO48_INTERNAL_WS2812_RGB_LED


pin = Pin(GPIO48_INTERNAL_WS2812_RGB_LED, Pin.OUT)
internal_rgb_led = NeoPixel(pin, 1) # Create a NeoPixel object for one LED

for i in range(100):

    internal_rgb_led[0] =  (0, 0, 255)
    internal_rgb_led.write()
    sleep(0.05)
    internal_rgb_led[0] = (0, 0, 5)
    internal_rgb_led.write()
    sleep(0.9)
