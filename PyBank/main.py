# Import the libraries

import os
import csv

# Read data
data = os.path.join("resources", "budget_data.csv")

# Output file
analysis = os.path.join("analysis", "analysis.txt")

with open(data) as data_file:
    raw_data = csv.reader(data_file, delimiter = ",")
    header = next(raw_data)
    print(f"header: {header}")

    for row in raw_data:
        print(row)
