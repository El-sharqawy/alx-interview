#!/usr/bin/python3
"""UTF-8 Validation check"""


def validUTF8(data):
    """checks if a given data set represents a valid UTF-8 encoding"""
    bytesNum = 0
    for char in data:
        bin = format(char, "#010b")[-8:]
        if bytesNum == 0:
            if bin.startswith("0"):
                continue
            elif bin.startswith("110"):
                bytesNum = 1
            elif bin.startswith("1110"):
                bytesNum = 2
            elif bin.startswith("11110"):
                bytesNum = 3
            else:
                return False
        else:
            if not bin.startswith("10"):
                return False
            bytesNum -= 1
    return bytesNum == 0
