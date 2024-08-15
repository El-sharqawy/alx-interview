#!/usr/bin/python3
"""Parse A Log File"""

import sys

if __name__ == "__main__":
    fileSize = 0
    count = 0

    stats = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size : {:d}".format(file_size))
        for key, val in sorted(stats.items()):
            if val:
                print("{}: {}".format(key, val))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                statusCode = data[-2]
                if statusCode in stats:
                    stats[statusCode] += 1
            except BaseException:
                pass

            try:
                fileSize += int(data[-1])
            except BaseException:
                pass

                if count % 10 == 0:
                    print_stats(stats, fileSize)
        print_stats(stats, fileSize)
    except KeyboardInterrupt:
        print_stats(stats, fileSize)
        raise
