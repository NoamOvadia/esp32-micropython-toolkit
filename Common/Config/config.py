import json
import os

DEVICE_TYPE = "device_type"
WIFI_NETWORK_NAME = "wifi_network_name"
COM_PORT = "com_port"
WIFI_SSID = "wifi_ssid"
WORKING_DIRECTORY_PATH = "working_directory_path"
AUTO_DETECT_PORT = "auto_detect_port"
COMMON_INTERFACE = "interface"
AUTO_DETECT_DIRECTORY_PATH = "auto_detect_directory_path"

def get_common_device_config():
    # Get the directory of the current script and build the path to the JSON file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'device_config.json')
    with open(json_path, 'r') as file:
        device_config = json.load(file)
        return device_config


def get_common_wifi_name() -> str:
    return device_config.get(WIFI_NETWORK_NAME)


def get_common_com_port() -> str:
    return device_config.get(COM_PORT)


def get_common_wifi_ssid() -> str:
    return device_config.get(WIFI_SSID)


def get_common_device_type() -> str:
    return device_config.get(DEVICE_TYPE)


def get_common_working_directory_path() -> str:
    return device_config.get(WORKING_DIRECTORY_PATH)


def get_common_auto_detect_port() -> bool:
    return device_config.get(AUTO_DETECT_PORT)


def get_common_interface() -> str:
    return device_config.get(COMMON_INTERFACE)


def get_common_auto_detect_directory_path() -> bool:
    return device_config.get(AUTO_DETECT_DIRECTORY_PATH)


device_config = get_common_device_config()
