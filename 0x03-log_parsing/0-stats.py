#!/usr/bin/python3
"""Parse Log File"""

import sys

if __name__ == "__main__":
    file_Size = 0
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
        print("File size: {:d}".format(file_Size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass

            try:
                file_Size += int(data[-1])
            except BaseException:
                pass

            if count % 10 == 0:
                print_stats(stats, file_Size)

        print_stats(stats, file_Size)
    except KeyboardInterrupt:
        print_stats(stats, file_Size)
        raise
