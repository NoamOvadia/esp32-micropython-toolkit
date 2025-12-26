from machine import Pin
import dht
import time
from Common.Const.gpio_map import GPIO4

sensor = dht.DHT11(Pin(GPIO4))

while True:
    try:
        sensor.measure()  # קריאת מדידה מהחיישן
        temp = sensor.temperature()  # טמפרטורה במעלות צלזיוס
        hum = sensor.humidity()  # לחות באחוזים
        print(f"Temperature: {temp}°C  |  Humidity: {hum}%")
    except OSError as e:
        print("Failed to read sensor:", e)

    time.sleep(2)  
