# PyPoll.py

import os
import csv
import statistics

filepath = os.path.join("Resources","election_data.csv")

ballotID = []
county = []
candidate = []

with open (filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvfile)
    for row in csvreader:
        ballotID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
# Get total number of votes
votetotal = len(ballotID)
print(votetotal)

# Get total list of candidates
CCS_votes = candidate.count("Charles Casper Stockham")
CCS_percent = round(CCS_votes / votetotal * 100, 3)
DD_votes = candidate.count("Diana DeGette")
DD_percent = round(DD_votes / votetotal * 100, 3)
RAD_votes = candidate.count("Raymon Anthony Doane")
RAD_percent = round(RAD_votes / votetotal * 100, 3)

print(f"Charles Casper Stockham: {CCS_percent}% ({CCS_votes})")
print(f"Diana Degette: {DD_percent}% ({DD_votes})")
print(f"Raymon Anthony Doane: {RAD_percent}% ({RAD_votes})")

# Find winner
winner = statistics.mode(candidate)
print(f"Winner: {winner}")

