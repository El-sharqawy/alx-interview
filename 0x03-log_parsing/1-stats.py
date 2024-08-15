#!/usr/bin/python3
"""A Script that Parses Log File"""

import re


def extInput(line):
    """Extracts line of HTTP Request"""
    fp = (
        r"\s*(?P<ip>\S+)\s*",
        r"\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]",
        r'\s*"(?P<request>[^"]*)"\s*',
        r"\s*(?P<status_code>\S+)",
        r"\s*(?P<file_size>\d+)",
    )
    info = {
        "status_code": 0,
        "file_size": 0,
    }
    log_fmt = "{}\\-{}{}{}{}\\s*".format(fp[0], fp[1], fp[2], fp[3], fp[4])
    result_match = re.fullmatch(log_fmt, line)
    if result_match is not None:
        status_code = result_match.group("status_code")
        file_size = int(result_match.group("file_size"))
        info["status_code"] = int(status_code)
        info["file_size"] = file_size
    return info


def print_stats(file_size, stats_codes):
    """Print HTTP Request Log Statistics"""
    print("File size: {:d}".format(file_size), flush=True)
    for code in sorted(stats_codes):
        num = stats_codes.get(code, 0)
        if num > 0:
            print("{:s}: {:d}".format(code, num), flush=True)


def update(line, file_size, stats_codes):
    """Updates the metrics from HTTP Requst Log"""
    lineInfo = extInput(line)
    code = lineInfo.get("status_code", 0)
    if code in stats_codes.keys():
        stats_codes[code] += 1
    return file_size + lineInfo["file_size"]


def main():
    """Main Def"""
    line_num = 0
    file_size = 0
    stats_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        while True:
            line = input()
            file_size = update(line, file_size, stats_codes)
            line_num += 1
            if line_num % 10 == 0:
                print_stats(file_size, stats_codes)
    except (KeyboardInterrupt, EOFError):
        print_stats(file_size, stats_codes)


if __name__ == "__main__":
    main()
