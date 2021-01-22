import csv
import os
# Path to csv input file and text output file
csvpath = os.path.join("Resources", "budget_data.csv")
outpath = os.path.join("Analysis", "data_analysis.txt")
# Set variables and counters
total_months = 0
month_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_rev = 0
# Read the budget_data.csv file
with open(csvpath) as budgetfile:
   csvreader = csv.reader(budgetfile)
   header = next(csvreader)
   first_row = next(csvreader)
   total_months += 1
   total_rev += int(first_row[1])
   prev_rev = int(first_row[1])
# Loop through rows of data and find number of months
   for row in csvreader:
     total_months += 1
# Print total Revenue
     total_rev += int(row[1])
# Calculate revenue change
     revenue_change = int(row[1]) - prev_rev
     prev_rev = int(row[1])
     net_change_list += [revenue_change]
     month_change += [row[0]]
# Greatest increase
     if revenue_change > greatest_increase[1]:
       greatest_increase[0] = row[0]
       greatest_increase[1] = revenue_change
# Greatest decrease
     if revenue_change < greatest_decrease[1]:
       greatest_decrease[0] = row[0]
       greatest_decrease[1] = revenue_change
# Average Revenue (outside of loop)
revenue_avg = sum(net_change_list) / len(net_change_list)
# Print everthing with titles
output = (
    f"Total Months: {total_months}\n"
    f"Total Revenue: {total_rev}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest increase in Revenue: {greatest_increase[0]} ${greatest_increase[1]}\n"
    f"Greatest decrease in Revenue: {greatest_decrease[0]} ${greatest_decrease[1]}\n"
)
print(output)
# Write to the text path
with open(outpath, "w") as txt_file:
    txt_file.write(output)
