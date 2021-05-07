import csv
import os
# Path to csv input file and text output file
csvpath = os.path.join("Resources", "election_data.csv")
outpath = os.path.join("Analysis", "pybank_analysis.txt")
#Set variables
total_votes = 0
all_candidates = []
vote_count  = []
#Open file
with open(csvpath) as pollfile:
 csvreader = csv.reader(pollfile)
 for row in csvreader:
  line = next(csvreader,None)
#Total number of votes cast
  total_votes += 1
  candidate = row[2]
        #if candidate has other votes then add to vote tally
  if candidate in all_candidates:
    candidate = all_candidates.index(candidate)
    vote_count[all_candidates] += 1
        #else create new spot in list for candidate
  else:
    all_candidates.append(candidate)
    vote_count.append(1)
#Variables calculated outside the loop
percentages = []
max_votes = vote_count[0]
max_index = 0
#Percentage of votes per candidate and Winner
for count in range(len(all_candidates)):
    vote_percentage = vote_count[count]/total_votes*100
    percentages.append(vote_percentage)
    if vote_count[count] > max_votes:
        max_votes = vote_count[count]
        print(max_votes)
        max_index = count
winner = all_candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
for count in range(len(all_candidates)):
    print(f"{all_candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"pypoll_results_summary.txt"

#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {total_votes}\n")
for count in range(len(all_candidates)):
    filewriter.write(f"{all_candidates[count]}: {percentages[count]}% ({vote_count[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()