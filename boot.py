from Utils.DeviceUtil.device_util import DeviceUtil
from Utils.DeviceUtil.built_in_led_util import BuiltInLED
from Common.Const.colors_map import GREEN

BuiltInLED.blink(7, 0.04, GREEN)
DeviceUtil.print_info()

# Implement your code here