# Pybank.py
# Create a Python script to analyze the financial records of your company.
# You'll be using budget_data.csv.
# The dataset is composed of two columns: "Date" and "Profit/Losses".

# Analyze the records to calculate each of the following values:
#   The total number of months included in the dataset
#   The net total amount of "Profit/Losses" over the entire period
#   The changes in "Profit/Losses" over the entire period, and then the average of those changes
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in profits (date and amount) over the entire period

# Import necessary modules
import os
import csv

months = [] # Month-year dates go here
results = [] # Profit/loss data goes here
changes = [] # Monthly differences in profit/loss goes here

filepath = os.path.join("Resources", "budget_data.csv")

# Copy data from .csv into variables
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvfile)
    for clmn in csvreader:
        months.append(clmn[0])
        results.append(int(clmn[1]))

# Calculate data for monthly differences in profit/loss,...
# https://www.geeksforgeeks.org/python-calculate-difference-between-adjacent-elements-in-given-list/
changes = [results[x+1] - results[x] for x in range(len(results)-1)]
# ... and the average of those monthly differences.
avg_change = round(sum(changes) / int(len(changes)), 2)

# Find the data for greatest profit, greatest loss, and their...
# ... respective dates.
for x in range(len(months)):
    if results[x] == min(results):
        maxloss = results[x]
        dateloss = months[x]
    elif results[x] == max(results):
        maxgain = results[x]
        dategain = months[x]
        
print("Financial Analysis")
print("----------------------------------------------------------")
# Find the total months included in the dataset
print(f"The dataset covers a total of {len(months)} months.")

# What's the net total revenue/loss for the whole period?
print(f"The net profit/loss for the covered period is ${sum(results)}.")

# Did the difference calculator work?
print(f"The average monthly change in profits/losses was ${avg_change}.")

# Did we get the greatest profit and loss, and their dates?
print(f"Our greatest profit was of ${maxgain} on {dategain}.")
print(f"Our greatest loss was of ${maxloss} on {dateloss}.")

