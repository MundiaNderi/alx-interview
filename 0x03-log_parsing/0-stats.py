#!/usr/bin/python3
import sys
from collections import defaultdict


def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print(f"{status_code}: {count}")


def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.strip().split()
            if len(parts) != 9:
                continue

            _, _, _, _, _, _, _, status_code, file_size = parts
            try:
                status_code = int(status_code)
                file_size = int(file_size)
            except ValueError:
                continue

            total_size += file_size
            status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
