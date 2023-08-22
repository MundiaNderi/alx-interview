#!/usr/bin/python3
"""Medthod that determines if a given data set represents
a valid UTF-8 encoding
"""


def validUTF8(data):
    """This function will check if data is a valid
    UTF-8 encoding and return True
    else it will return False"""

    # Variable to keep track of the number of leading ones in the current byte
    num_leading_ones = 0

    # Iterate through each integer in the data list
    for byte in data:
        # Check if the current byte is a continuation byte (starts with '10')
        if num_leading_ones > 0:
            if (byte >> 6) != 0b10:
                return False
            num_leading_ones -= 1
        else:
            # Count the number of leading ones in the current byte
            mask = 0b10000000
            while mask & byte:
                num_leading_ones += 1
                mask >>= 1

            # Validate the number of leading ones and their positions
            if num_leading_ones == 1 or num_leading_ones > 4:
                return False

    # Check if all bytes have been used to complete multi-byte characters
    return num_leading_ones == 0
