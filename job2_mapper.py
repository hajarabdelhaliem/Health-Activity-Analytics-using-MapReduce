#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) < 6: continue
    # Key: dummy, Value: Day,Weight,Calories,Steps
    print(f"dummy\t{parts[0]},{parts[2]},{parts[3]},{parts[5]}")