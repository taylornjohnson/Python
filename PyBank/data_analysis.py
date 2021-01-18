#Import Python module needed
import csv
import os

#Path to csv input file and text output file
csvpath = os.path.join("Desktop","Python","PyBank","Resources","budget_data.csv")
pathout = os.path.join("Desktop","Python","PyBank","Analysis", "budget_analysis.txt")

#Set variables and counters 
totalMonth = 0
totalRevenue = 0
previousRevenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999999999]

#Read the budget_data.csv file
with open(csvpath, 'w', newline='') as revdata:
   csvreader = csv.reader(csvpath , delimiter = ',')

#Loop through rows of data
   for row in csvreader:

       #Totaling
           totalMonth = totalMonth + 1
           totalRevenue = totalRevenue + int(row["Revenue"])

#Change of revenue calculations
           revenue_change = int(row["Revenue"]) - previousRevenue
           previousRevenue = int(row["Revenue"])
           month_of_change = month_of_change + [row["Date"]]

           #Greatest Increase value
           if (revenue_change > greatestIncrease[1]):
               greatestIncrease[1] = revenue_change
               greatestIncrease[0] = row["Date"]

           if (revenue_change < greatestDecrease[1]):
               greatestDecrease[0] = row["Date"]
               greatestDecrease[1] = revenue_change
        
#Average revenue calculations (outside of loop)
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


#Print the outcomes
output = (
    f"Total Months: {totalMonth}\n"
    f"Total Revenue: {totalRevenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest increase in Revenue: {greatestIncrease[0]} ${greatestIncrease[1]}\n"
    f"Greatest decrease in Revenue: {greatestDecrease[0]} ${greatestDecrease[1]}\n"
)

print(output)

#Write to the text path
with open(pathout, "w") as txt_file:
    txt_file.write(output)
