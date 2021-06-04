import csv
import os
# Path to csv input file and text output file
csvpath = os.path.join("Resources", "election_data.csv")
outpath = os.path.join("Analysis", "pybank_analysis.txt")
#Set variables
total_votes = 0
all_candidates = []
candidate_votes = {}

winning_candidate = ""
win_count = 0

#Open file
with open(csvpath) as pollfile:
  csvreader = csv.DictReader(pollfile)
 
for row in csvreader:
#Total number of votes cast
  total_votes = total_votes + 1

  candidate = row["Candidate"]

  #if candidate has other votes then add to vote tally
  if candidate not in all_candidates:
    all_candidates.append(candidate)
    candidate_votes[candidate] = 0
    candidate_votes[candidate] += 1
  
with open(outpath, "w") as txt_file:
  
  #print results
  election_results = ()
  print("Election Results")
  print("--------------------------")
  print(f"Total Votes: {total_votes}")
)
print(election_results)

txt_file.write(election_results)

# find winner
for candidate in candidate_votes:
  votes = candidate_votes.get(candidate)
  vote_percent = float(votes)/float(total_votes) * 100
  
  if (votes > win_count):
    win_count = votes
    winning_candidate = candidate

  voter_output = f"{candidate}: {vote_percent:.2f}% ({votes})\n"
  print(voter_output)

#winner
winner_sum = (
  f"--------------------------\n"
  f"Winner: {winning_candidate}\n"
  f"--------------------------\n"
)
print(winner_sum)

txt_file.write(winner_sum)