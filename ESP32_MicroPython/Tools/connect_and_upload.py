import serial
import serial.tools.list_ports
import subprocess
import os
from Common.Config import config

def detect_esp32_port():
    """Auto-detect ESP32 port"""
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'CP210' in port.description or 'CH340' in port.description or 'USB' in port.description:
            print(f"Found potential ESP32 port: {port.device}")
            return port.device

    print("Available ports:")
    for port in ports:
        print(f"  {port.device}: {port.description}")

    if ports:
        return ports[0].device
    return None

def execute_command(cmd:list):

    try:
        concatenated_command = " ".join(cmd)
        print(f'Try to execute command: {concatenated_command}')
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("File uploaded successfully!")

    except subprocess.CalledProcessError as e:
        print("Error uploading file:")
        print(e.stderr)

def get_boot_and_main_path(dir_path:str):

    def get_all_files(directory_path):
        """Get all files recursively from a directory"""
        all_files = []

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                full_path = os.path.join(root, file)
                all_files.append(full_path)

        return all_files

    file_list = get_all_files(dir_path)
    boot_path, main_path = None, None
    is_main = False
    is_boot = False
    for path in file_list:
        file_name = str(path).split('/')[-1]
        if not is_main and file_name == "main.py":
            main_path = path
            is_main = True
        elif not is_boot and file_name == "boot.py":
            boot_path = path
            is_boot = True
    assert is_boot and is_main, 'Invalid boot.py or main.py'
    return boot_path, main_path

def is_port_free(port):
    try:
        s = serial.Serial(port)
        s.close()
        return True
    except serial.SerialException:
        return False

def connect_to_esp_flow():
    working_directory = config.get_common_working_directory_path()
    print(f'Working directory path: {working_directory}')

    is_auto_detection_port = config.get_common_auto_detect_port()
    print(f'Port detection mode: {"Auto detection port" if is_auto_detection_port else "Manually detection port"}')

    interface = config.get_common_interface()
    print(f'Interface: {interface}')

    boot_path, main_path = get_boot_and_main_path(working_directory)
    print(f'Boot file path: {boot_path}')
    print(f'Main file path: {main_path}')

    if is_auto_detection_port:
        device_com_port = detect_esp32_port()
    else:
        device_com_port = config.get_common_com_port()

    if is_port_free(device_com_port):
        command = [interface, "connect", device_com_port, "fs", "put", boot_path, main_path]
        execute_command(command)
    else:
        print('The port is busy...')


connect_to_esp_flow()



