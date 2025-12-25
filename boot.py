import time

from Utils.DeviceUtil.device_util import DeviceUtil
from Utils.DeviceUtil.built_in_led_util import BuiltInLED
from Common.Const.colors_map import GREEN, BLUE, GOLD
from Utils.Logger.logger import Logger

from Utils.SensorsUtils.microphone_module import calibrate_dc, init_adc_gpio
from Common.Const.gpio_map import GPIO1

_logger = Logger('Boot')



BuiltInLED.blink(7, 0.04, GREEN)
DeviceUtil.print_info()


init_adc_gpio(GPIO1)
_logger.info('Wait 2 seconds...')
time.sleep(5)
BuiltInLED.set_color(GOLD)
BuiltInLED.on()
calibrate_dc(9000)
time.sleep(2)
BuiltInLED.blink(7, 0.02, GOLD)