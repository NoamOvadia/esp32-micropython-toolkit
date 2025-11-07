import machine
import sys
import esp32
import gc

class DeviceUtil:
    """ESP32-S3 Chip using built-in functions"""

    @staticmethod
    def get_chip_id():
        """
        Get unique chip ID

        Returns:
            Integer chip ID
        """
        return machine.unique_id()

    @staticmethod
    def get_chip_id_hex():
        """
        Get chip ID as hex string

        Returns:
            String like "AABBCCDD"
        """
        chip_id = machine.unique_id()
        return ''.join(['{:02X}'.format(b) for b in chip_id])

    @staticmethod
    def get_frequency():
        """
        Get CPU frequency in Hz

        Returns:
            Integer frequency in Hz
        """
        return machine.freq()

    @staticmethod
    def get_reset_cause():
        """
        Get the cause of the last reset

        Returns:
            Tuple of (reset_code, reset_name)
        """
        reset_causes = {
            machine.PWRON_RESET: "Power-on reset",
            machine.HARD_RESET: "Hard reset",
            machine.WDT_RESET: "Watchdog reset",
            machine.DEEPSLEEP_RESET: "Deep sleep reset",
            machine.SOFT_RESET: "Soft reset"
        }

        cause = machine.reset_cause()
        name = reset_causes.get(cause, "Unknown reset")

        return cause, name

    @staticmethod
    def get_flash_size():
        """
        Get flash memory size

        Returns:
            Flash size in bytes
        """
        try:
            # Try to get flash size from esp32 module
            return esp32.flash_size()
        except:
            return "Unknown"

    @staticmethod
    def get_heap_info():
        """
        Get heap memory information

        Returns:
            Dictionary with free and total heap
        """
        import gc
        gc.collect()

        return {
            'free': gc.mem_free(),
            'allocated': gc.mem_alloc(),
            'total': gc.mem_free() + gc.mem_alloc()
        }

    @staticmethod
    def get_platform():
        """
        Get platform information

        Returns:
            String with platform name
        """
        return sys.platform

    @staticmethod
    def get_implementation():
        """
        Get Python implementation info

        Returns:
            String with implementation details
        """
        impl = sys.implementation
        return f"{impl.name} {impl.version[0]}.{impl.version[1]}.{impl.version[2]}"

    @staticmethod
    def get_all_info():
        """
        Get all system information

        Returns:
            Dictionary with all available information
        """
        heap = DeviceUtil.get_heap_info()
        reset_code, reset_name = DeviceUtil.get_reset_cause()

        return {
            'chip': 'ESP32-S3',
            'chip_id': DeviceUtil.get_chip_id_hex(),
            'platform': DeviceUtil.get_platform(),
            'implementation': DeviceUtil.get_implementation(),
            'cpu_freq_mhz': DeviceUtil.get_frequency() // 1_000_000,
            'flash_size': DeviceUtil.get_flash_size(),
            'heap_free': heap['free'],
            'heap_allocated': heap['allocated'],
            'heap_total': heap['total'],
            'reset_cause_code': reset_code,
            'reset_cause': reset_name
        }

    @staticmethod
    def print_info():
        """Print system information in a readable format"""
        info = DeviceUtil.get_all_info()

        print("=" * 50)
        print("ESP32-S3 System Information")
        print("=" * 50)
        print(f"Chip:           {info['chip']}")
        print(f"Chip ID:        {info['chip_id']}")
        print(f"Platform:       {info['platform']}")
        print(f"Implementation: {info['implementation']}")
        print(f"CPU Frequency:  {info['cpu_freq_mhz']} MHz")

        if isinstance(info['flash_size'], int):
            flash_mb = info['flash_size'] // (1024 * 1024)
            print(f"Flash Size:     {flash_mb} MB ({info['flash_size']} bytes)")
        else:
            print(f"Flash Size:     {info['flash_size']}")

        print(f"Heap Free:      {info['heap_free']:,} bytes")
        print(f"Heap Allocated: {info['heap_allocated']:,} bytes")
        print(f"Heap Total:     {info['heap_total']:,} bytes")
        print(f"Reset Cause:    {info['reset_cause']} ({info['reset_cause_code']})")
        print("=" * 50)


def print_chip_info():
    DeviceUtil.print_info()

def get_chip_id():
    return DeviceUtil.get_chip_id_hex()

def get_free_memory():
    """Get free memory in KB"""
    gc.collect()
    return gc.mem_free() // 1024

def get_reset_reason():
    _, name = DeviceUtil.get_reset_cause()
    return name

