#!/usr/bin/env python3
import sys

data = []
for line in sys.stdin:
    try:
        _, val = line.strip().split('\t')
        d, w, c, s = val.split(',')
        data.append({"day": d, "w": float(w), "c": float(c), "s": float(s)})
    except: continue

data.sort(key=lambda x: x['day'])
print("Day,Roll7_Avg_Weight,Roll7_Avg_Calories,Roll7_Avg_Steps")

for i in range(len(data)):
    window = data[max(0, i-6) : i+1]
    avg_w = sum(x['w'] for x in window) / len(window)
    avg_c = sum(x['c'] for x in window) / len(window)
    avg_s = sum(x['s'] for x in window) / len(window)
    print(f"{data[i]['day']},{avg_w:.2f},{avg_c:.1f},{avg_s:.1f}")