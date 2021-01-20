#Import Python module needed
import csv
import os
#Path to csv input file and text output file
csvpath = os.path.join("Resources","budget_data.csv")
#Set variables and counters 
months = []
revenue = 0
revenue_change = []
month_change = []
#Read the budget_data.csv file
with open(csvpath, 'r', newline='') as budgetfile:
   csvreader = csv.reader(budgetfile , delimiter = ',')
   print(csvreader)
#Loop through rows of data and find number of months
   for row in csvreader:
    months.append(row[0])
   print(len(months))
#Print total Revenue
   total_rev = revenue + int(row[1])
   print(total_rev)