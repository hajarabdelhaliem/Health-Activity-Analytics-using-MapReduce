#!/usr/bin/env python3
import sys

print("Day,Protein_per_kg,Calories_per_min,Steps_per_100cal")
for line in sys.stdin:
    line = line.strip()
    print(line.replace('\t', ','))