import os
import csv

csv_path = os.path.join("resources", "election_data.csv")
analysis = os.path.join("analysis", "analysis.txt")

votes = 0
candidates = []
votes_total = []
votes_percent = []
most_votes = 0


# Open and read file
with open(csv_path) as csv_file:
    data = csv.reader(csv_file, delimiter=",")
    
    # Skip header 
    header = next(data)


    # Start the for loop to get the total number of votes
    for row in data:
        votes += 1

        # List of name, total votes and % votes 
        if row[2] not in candidates:
            candidates.append(row[2])
            votes_total.append(0)
            votes_percent.append(0)

        # Count the name of the peson who was boted for and add to their total
        for i, candidate in enumerate(candidates):
            if candidate == row[2]:
                votes_total[i] += 1     
# Calculate % won
for i in range(len(candidates)):
    votes_percent[i] = "{:.3%}".format(votes_total[i]/votes)

    #check to see who has the highest total count and set the winner variable to that candidate
    if votes_total[i] > most_votes:
        most_votes = votes_total[i]
        winner = candidates[i]

# Variable that holds a list of all the names and their data
candidate_list = [f'{candidates[i]}: {votes_percent[i]} ({votes_total[i]})' for i in range(len(candidates))]

# Write to analysis.txt 
with open(analysis, "w") as output:
    output.write("Election Reults\n")
    output.write("--------------------------\n")
    output.write(f"Total Votes: {votes}\n")
    output.write("--------------------------\n")
    for name in candidate_list:
        output.write(f"{name}\n")
    output.write("--------------------------\n")
    output.write(f'Winner: {winner}\n')
    output.write("--------------------------")


with open(analysis) as txtfile:
    print(txtfile.read())