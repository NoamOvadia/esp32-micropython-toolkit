
from time import sleep
from Common.Const import colors_map as colors
from machine import Pin
from neopixel import NeoPixel
from Common.Const.gpio_map import GPIO48_INTERNAL_WS2812_RGB_LED

num_of_leds = 1
pin = Pin(GPIO48_INTERNAL_WS2812_RGB_LED, Pin.OUT)
led = NeoPixel(pin, num_of_leds)


class BuiltInLED:

    @staticmethod
    def set_color(color: tuple[int, int, int]) -> None:
        """
        Prepare a color before set to the internal LED
        :param color: RGB tuple (uint8, uint8, uint8)
        :return: None
        """
        led[0] = color

    @staticmethod
    def off() -> None:
        """
        Set the internal led to OFF
        :return: None
        """
        led[0] = colors.NONE
        led.write()

    @staticmethod
    def on() -> None:
        """
        Set the internal led to ON
        :return: None
        """
        led.write()

    @staticmethod
    def blink(intervals: int = 1, duration: float = 0.5, color: tuple[int, int, int] = colors.GREEN) -> None:
        """
        Blink an LED or display element with a specified color and timing.
        :param intervals: The number of times to blink the indicator.
                          Must be a non-negative integer, optional.

        :param duration: The duration in seconds for each on/off state within
                         a blink cycle, optional.

        :param color: RGB - tuple[int, int, int], optional.

        :return: None
        """

        for _ in range(intervals):
            BuiltInLED.set_color(color)
            BuiltInLED.on()
            sleep(duration)
            BuiltInLED.set_color(color)
            BuiltInLED.off()
            sleep(duration)
