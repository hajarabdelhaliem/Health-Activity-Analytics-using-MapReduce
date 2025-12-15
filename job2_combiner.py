#!/usr/bin/env python3
import sys
from collections import defaultdict

agg = defaultdict(lambda: [0.0, 0.0, 0.0, 0])  # weight, calories, steps, count

for line in sys.stdin:
    line = line.strip()
    if "\t" not in line:  # skip invalid lines
        continue
    day, values = line.split("\t")
    weight, calories, steps, count = map(float, values.split(","))
    agg[day][0] += weight
    agg[day][1] += calories
    agg[day][2] += steps
    agg[day][3] += count

for day, v in agg.items():
    print(f"{day}\t{v[0]},{v[1]},{v[2]},{v[3]}")
