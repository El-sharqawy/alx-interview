#!/usr/bin/python3
"""LockBoxes Algorithm Solution"""


def canUnlockAll(boxes):
    """Algo Solution"""
    for key in range(1, len(boxes)):
        bCanOpen = False
        for box in range(len(boxes)):
            if key in boxes[box] and key != box:
                bCanOpen = True
                break
        if bCanOpen is False:
            return False
    return True
