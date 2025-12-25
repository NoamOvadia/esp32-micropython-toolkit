from machine import ADC, Pin
from Utils.Logger.logger import Logger
import time

adc = None
_offset = None

_logger = Logger('Microphone Module')


def read_microphone():
    global _offset

    raw = adc.read_u16()
    centred = adc.read_u16() - _offset
    _logger.info(f'raw: {raw} centred: {centred}')
    return centred


def init_adc_gpio(gpio_num: int) -> None:
    _logger.info(f'Begin initialize ADC with GPIO {gpio_num}')
    global adc
    adc = ADC(Pin(gpio_num))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)


def calibrate_dc(num_samples: int) -> float:
    _logger.info(f'Calibrate DC with {num_samples} samples')
    global _offset
    s = 0
    for _ in range(num_samples):
        raw_data = adc.read_u16()
        #_logger.info(f'Raw data = {raw_data}')

        s += raw_data
    offset = s / num_samples if num_samples else 0

    msg = f'Microphone DC calibrated with offset: {offset}'
    _logger.info(msg) if offset else _logger.warning(msg)
    _offset = offset
    return offset


def get_offset():
    return _offset
