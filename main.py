import time
from machine import Pin
from time import sleep
from Utils.SensorsUtils.microphone_module import *


# Implement your code here
while True:
    mic_raw_value = read_microphone()
    #print(f'Raw data: {mic_raw_value}')
    sleep(0.2)









