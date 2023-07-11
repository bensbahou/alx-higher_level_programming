#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys

file_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
i = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            a = i
            if tokens[-2] in status_counts:
                status_counts[tokens[-2]] += 1
                i += 1
            try:
                file_size += int(tokens[-1])
                if a == i:
                    i += 1
            except FileNotFoundError:
                if a == i:
                    continue
        if i % 10 == 0:
            print(f"File size: {file_size:d}")
            for key, value in sorted(status_counts.items()):
                if value:
                    print(f"{key:s}: {value:d}")
    print(f"File size: {file_size:d}")
    for key, value in sorted(status_counts.items()):
        if value:
            print(f"{key:s}: {value:d}")

except KeyboardInterrupt:
    print(f"File size: {file_size:d}")
    for key, value in sorted(status_counts.items()):
        if value:
            print(f"{key:s}: {value:d}")
