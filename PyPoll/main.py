import csv
import os

# Loading data and outputting analysis
loadedStats = os.path.join("Resources", "election_data.csv")
outputFile = os.path.join("analysis","output.txt")

# Initializing variables
number_votes_cast = 0
cand_list = []
total_votes_can = {}
percentageVotes = []
winner = []
winner_count = 0
cand_name = []

with open(loadedStats) as election_data:
    csvreader = csv.reader(election_data)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Beginning For Loop
    for row in csvreader:
        number_votes_cast += 1
        cand_name = row[2]
        if cand_name in cand_list:
            total_votes_can[cand_name] = total_votes_can[cand_name] + 1
        else:
            cand_list.append(cand_name)
            total_votes_can[cand_name] = 1

# Printing total votes cast and list of candidates receiving votes
print(total_votes_can)
print(cand_list)

with open(outputFile, 'w') as results_file:
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {number_votes_cast}\n"
        f"-------------------------\n")
    
    print(election_results)    
    results_file.write(election_results)

    for candidate in total_votes_can:
        votes = total_votes_can.get(candidate)

        # Calculating percentage of votes per candidate
        vote_percent = float(votes)/float(number_votes_cast) * 100
        vote_output = (f"{candidate}: {vote_percent:.3f}% ({votes})\n")

        # Printing list of candidates, percentage of votes, and total number of votes won per candidate
        print(vote_output)
        results_file.write(vote_output)
    
        # Determining winning candidate
        if (votes > winner_count):
            winner_count = votes
            winning_candidate = candidate

    winner_candidate = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")

    # Printing winning candidate  
    print(winner_candidate)
    results_file.write(winner_candidate)