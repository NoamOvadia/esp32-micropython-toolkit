from machine import mem32, mem16, mem8
from Common.Const.register_map import (GPIO_OUT_REG,
                                       GPIO_OUT_W1TS_REG,
                                       GPIO_OUT_W1TC_REG,
                                       GPIO_ENABLE_REG,
                                       GPIO_ENABLE_W1TS_REG,
                                       GPIO_ENABLE_W1TC_REG,
                                       GPIO_IN_REG)

class MemoryUtils:
    """Class for reading and writing to ESP32-S3 registers"""

    @staticmethod
    def read_reg32(address):
        """
        Read a 32-bit value from a register

        Args:
            address: Register address (must be 4-byte aligned)

        Returns:
            32-bit integer value
        """
        if address % 4 != 0:
            raise ValueError("Address must be 4-byte aligned for 32-bit access")
        return mem32[address]

    @staticmethod
    def write_reg32(address, value):
        """
        Write a 32-bit value to a register

        Args:
            address: Register address (must be 4-byte aligned)
            value: 32-bit integer value to write
        """
        if address % 4 != 0:
            raise ValueError("Address must be 4-byte aligned for 32-bit access")
        mem32[address] = value & 0xFFFFFFFF

    @staticmethod
    def read_reg16(address):
        """
        Read a 16-bit value from a register

        Args:
            address: Register address (must be 2-byte aligned)

        Returns:
            16-bit integer value
        """
        if address % 2 != 0:
            raise ValueError("Address must be 2-byte aligned for 16-bit access")
        return mem16[address]

    @staticmethod
    def write_reg16(address, value):
        """
        Write a 16-bit value to a register

        Args:
            address: Register address (must be 2-byte aligned)
            value: 16-bit integer value to write
        """
        if address % 2 != 0:
            raise ValueError("Address must be 2-byte aligned for 16-bit access")
        mem16[address] = value & 0xFFFF

    @staticmethod
    def read_reg8(address):
        """
        Read an 8-bit value from a register

        Args:
            address: Register address

        Returns:
            8-bit integer value
        """
        return mem8[address]

    @staticmethod
    def write_reg8(address, value):
        """
        Write an 8-bit value to a register

        Args:
            address: Register address
            value: 8-bit integer value to write
        """
        mem8[address] = value & 0xFF

    @staticmethod
    def set_bits(address, mask):
        """
        Set specific bits in a register (OR operation)

        Args:
            address: Register address
            mask: Bit mask to set
        """
        current = mem32[address]
        mem32[address] = current | mask

    @staticmethod
    def clear_bits(address, mask):
        """
        Clear specific bits in a register (AND NOT operation)

        Args:
            address: Register address
            mask: Bit mask to clear
        """
        current = mem32[address]
        mem32[address] = current & ~mask

    @staticmethod
    def toggle_bits(address, mask):
        """
        Toggle specific bits in a register (XOR operation)

        Args:
            address: Register address
            mask: Bit mask to toggle
        """
        current = mem32[address]
        mem32[address] = current ^ mask

    @staticmethod
    def modify_bits(address, mask, value):
        """
        Modify specific bits in a register

        Args:
            address: Register address
            mask: Bit mask for the bits to modify
            value: New value for the masked bits
        """
        current = mem32[address]
        mem32[address] = (current & ~mask) | (value & mask)

    @staticmethod
    def read_bit(address, bit_position):
        """
        Read a specific bit from a register

        Args:
            address: Register address
            bit_position: Bit position (0-31)

        Returns:
            1 if bit is set, 0 if clear
        """
        if bit_position < 0 or bit_position > 31:
            raise ValueError("Bit position must be between 0 and 31")
        return (mem32[address] >> bit_position) & 1

    @staticmethod
    def write_bit(address, bit_position, value):
        """
        Write a specific bit in a register

        Args:
            address: Register address
            bit_position: Bit position (0-31)
            value: 1 to set, 0 to clear
        """
        if bit_position < 0 or bit_position > 31:
            raise ValueError("Bit position must be between 0 and 31")

        if value:
            MemoryUtils.set_bits(address, 1 << bit_position)
        else:
            MemoryUtils.clear_bits(address, 1 << bit_position)

    @staticmethod
    def read_bits(address, start_bit, num_bits):
        """
        Read multiple consecutive bits from a register

        Args:
            address: Register address
            start_bit: Starting bit position
            num_bits: Number of bits to read

        Returns:
            Integer value of the specified bits
        """
        if start_bit < 0 or start_bit > 31:
            raise ValueError("Start bit must be between 0 and 31")
        if num_bits < 1 or start_bit + num_bits > 32:
            raise ValueError("Invalid number of bits")

        mask = (1 << num_bits) - 1
        return (mem32[address] >> start_bit) & mask

    @staticmethod
    def write_bits(address, start_bit, num_bits, value):
        """
        Write multiple consecutive bits to a register

        Args:
            address: Register address
            start_bit: Starting bit position
            num_bits: Number of bits to write
            value: Value to write
        """
        if start_bit < 0 or start_bit > 31:
            raise ValueError("Start bit must be between 0 and 31")
        if num_bits < 1 or start_bit + num_bits > 32:
            raise ValueError("Invalid number of bits")

        mask = ((1 << num_bits) - 1) << start_bit
        value_shifted = (value << start_bit) & mask
        current = mem32[address]
        mem32[address] = (current & ~mask) | value_shifted

    @staticmethod
    def gpio_set_output(pin):
        """Enable GPIO pin as output"""
        MemoryUtils.set_bits(GPIO_ENABLE_REG, 1 << pin)

    @staticmethod
    def gpio_set_high(pin):
        """Set GPIO pin high"""
        MemoryUtils.write_reg32(GPIO_OUT_W1TS_REG, 1 << pin)

    @staticmethod
    def gpio_set_low(pin):
        """Set GPIO pin low"""
        MemoryUtils.write_reg32(GPIO_OUT_W1TC_REG, 1 << pin)

    @staticmethod
    def gpio_read(pin):
        """Read GPIO pin state"""
        return MemoryUtils.read_bit(GPIO_IN_REG, pin)

    @staticmethod
    def gpio_toggle(pin):
        """Toggle GPIO pin"""
        MemoryUtils.toggle_bits(GPIO_OUT_REG, 1 << pin)