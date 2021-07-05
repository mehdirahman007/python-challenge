# Import the libraries

import os
import csv

# Read data
data = os.path.join("resources", "budget_data.csv")

# Output file
analysis = os.path.join("analysis", "analysis.txt")

# Variables
month = 0
pltotal = 0
change = []
current = 0
past = 0
mostinc = 0
mostdec = 0



with open(data) as data_file:
    raw_data = csv.reader(data_file, delimiter = ",")
    header = next(raw_data)

    for i, row in enumerate(raw_data):
        month += 1
        pltotal += int(row[1])

        if i > 0:
            current = int(row[1])
            change.append(current - past)
            mchange = current - past

            if mchange > mostinc:
                month_inc = row[0]
                mostinc = mchange
        
            elif mchange < mostdec:
                month_dec = row[0]
                mostdec = mchange
            past = int(row[1])
        else:
            past = int(row[1])

change = round(sum(change)/len(change),2)

print(change)


with open(analysis, "w") as output:
    output.write("Financial Analysis\n")
    output.write("--------------------------\n")
    output.write(f"Total Months: {month}\n")
    output.write(f"Total: ${pltotal}\n")
    output.write(f"Average Change: ${change}\n")
    output.write(f"Greatest Increase in Profits: {month_inc} (${mostinc})\n")
    output.write(f"Greates Decrease in Profits: {month_dec} (${mostdec})\n")

with open(analysis) as print_file:
    print(print_file.read())




    