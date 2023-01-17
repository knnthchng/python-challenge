# PyPoll.py

import os
import csv

filepath = os.path.join("Resources","election_data.csv")

cand_total = []
cand_names = []

with open (filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvfile)
    for row in csvreader:
        cand_total.append(row[2])
        
# Get total number of votes
votetotal = len(cand_total)
print(f"Total Ballots Cast: {votetotal}")

# Get the unique list of candidates
cand_set = set(cand_total)
cand_names = list(cand_set)

# Calculate total votes (and percentages) for each candidate
cand0_total = cand_total.count(cand_names[0])
cand0_percent = round(cand0_total / votetotal * 100, 3)
print(f"{cand_names[0]}: {cand0_percent}% ({cand0_total})")

cand1_total = cand_total.count(cand_names[1])
cand1_percent = round(cand1_total / votetotal * 100, 3)
print(f"{cand_names[1]}: {cand1_percent}% ({cand1_total})")

cand2_total = cand_total.count(cand_names[2])
cand2_percent = round(cand2_total / votetotal * 100, 3)
print(f"{cand_names[2]}: {cand2_percent}% ({cand2_total})")

# Find winner
# The mode of the total candidates' votes list will bring up the winner
import statistics
winner = statistics.mode(cand_total)
print(f"Winner: {winner}")

# Create .txt file that reads out the analysis
output = 'Analysis/Python_Election_Results.txt'
with open(output, 'w') as f:
        f.write("Election Results\n")
        f.write("----------------------------------------------------\n")
        f.write(f"Total Ballots Cast: {votetotal}\n")
        f.write("----------------------------------------------------\n")
        f.write(f"{cand_names[0]}: {cand0_percent}% ({cand0_total})\n")
        f.write(f"{cand_names[1]}: {cand1_percent}% ({cand1_total})\n")
        f.write(f"{cand_names[2]}: {cand2_percent}% ({cand2_total})\n")
        f.write("----------------------------------------------------\n")
        f.write(f"Winner: {winner}\n")
        f.write("----------------------------------------------------\n")
        f.close()

print("Results saved as .txt in Analysis folder.")
