"""
Blink internal ESP32 S3 Internal NeoPixel led
num of leds: 1pcs internal NeoPixel led in ESP32 connected to GPIO 48
"""
from Common.Const import colors_map as colors
from machine import Pin
from neopixel import NeoPixel
from time import sleep
from Common.Const.gpio_map import GPIO48_INTERNAL_WS2812_RGB_LED


num_of_leds = 1
pin = Pin(GPIO48_INTERNAL_WS2812_RGB_LED, Pin.OUT)
led = NeoPixel(pin, num_of_leds)

for color in colors.ALL_COLORS:
    led[0] = color
    led.write()
    sleep(0.5)

led[0] = colors.NONE