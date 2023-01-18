# Financial Statement Analysis

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

# Find the total amount of months represented in data set
totalmon = len(months)

# Find the net total revenues/losses for this dataset
netresult = sum(results)

# Calculate data for monthly differences in profit/loss,...
# https://www.geeksforgeeks.org/python-calculate-difference-between-adjacent-elements-in-given-list/
changes = [results[x+1] - results[x] for x in range(len(results)-1)]
# ... and the average of those monthly differences.
avg_change = round(sum(changes) / int(len(changes)), 2)

# Find the data for greatest profit, greatest loss, and their...
# ... respective dates.
for x in range(len(changes)):
    if changes[x] == min(changes):
        maxloss = changes[x]
        dateloss = months[x+1]
    elif changes[x] == max(changes):
        maxgain = changes[x]
        dategain = months[x+1]

# Output results into terminal
print("Financial Analysis")
print("----------------------------------------------------")
print(f"The dataset covers a total of {totalmon} months.")
print(f"The net profit/loss for the covered period is ${netresult}.")
print(f"The average monthly change in profits/losses was ${avg_change}.")
print(f"Our greatest profit was of ${maxgain} on {dategain}.")
print(f"Our greatest loss was of ${maxloss} on {dateloss}.")

# Export results in a .txt file
export = 'Analysis/Financial_Analysis.txt'
with open(export, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------------------------------\n")
    f.write(f"The dataset covers a total of {totalmon} months.\n")
    f.write(f"The net profit/loss for the covered period is ${sum(results)}.\n")
    f.write(f"The average monthly change in profits/losses was ${avg_change}.\n")
    f.write(f"Our greatest profit was of ${maxgain} on {dategain}.\n")
    f.write(f"Our greatest loss was of ${maxloss} on {dateloss}.\n")
    f.close()
    
print("----------------------------------------------------")
print("Analysis results exported as .txt file in Analysis folder.")
