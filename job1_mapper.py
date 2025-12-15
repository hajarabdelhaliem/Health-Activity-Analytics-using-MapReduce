#!/usr/bin/env python3
import csv

csv_file_path = "Gym_Progress_Dataset.csv"

with open(csv_file_path, "r") as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header
    next(reader, None)
    for row in reader:
        if len(row) != 6:
            continue
        day, protein, weight, calories, workout, steps = row
        print(f"{day}\t{protein},{weight},{calories},{workout},{steps}")
