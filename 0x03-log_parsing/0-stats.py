#!/usr/bin/python3

import sys
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) != 7:
                continue

            ip_address, date, request, status_code, file_size = parts
            if status_code.isdigit():
                status_counts[status_code] += 1
            total_size += int(file_size)

            line_count += 1
            if line_count == 10:
                print_statistics(total_size, status_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
