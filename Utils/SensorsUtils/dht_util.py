import dht
from Utils.DeviceUtil.built_in_led_util import BuiltInLED
from time import sleep
from Common.Const import colors_map as color


class DhtUtils:

    def __init__(self, dht_sensor_obj: dht.DHT11):
        self.sensor = dht_sensor_obj

    def measure(self) -> None:
        self.sensor.measure()

    def read_dht_11(self, log: bool = True) -> tuple[float, float]:
        """Read the temperature in Celsius and humidity in precent"""
        temperature_c = self.sensor.temperature()
        humidity_prc = self.sensor.humidity()
        if log:
            print(f"Temperature: {temperature_c}°C Humidity: {humidity_prc}%")
        return temperature_c, humidity_prc

    def read_sensor_flow(self, sleep_interval_sec: float = 2, log: bool = True):
        """Read DHT11"""
        BuiltInLED.set_color(color.ORANGE)
        BuiltInLED.on()
        self.measure()
        temperature_c, humidity = self.read_dht_11(log)
        BuiltInLED.off()
        sleep(sleep_interval_sec)
        return temperature_c, humidity


def celsius_2_fahrenheit(temp_c):
        return temp_c * 1.8 + 32

def fahrenheit_2_celsius(temp_f):
        return temp_f - 32 * 5 / 9
