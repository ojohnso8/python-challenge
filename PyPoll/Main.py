#import
import os
import csv

#csv path
election_csv = os.path.join(".", "election_data.csv")

#empty lists

votes = []
candidateList= []

#open csv
with open(election_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
    
        votes.append(row[0])
        candidateList.append(row[2])

  # The total number of votes cast  
    total_votes = len(votes)
    print("Total Votes: ", total_votes)

# A complete list of candidates who received votes
    x = candidateList
    unique_candidate_list = list(set(x))
    print("Candidates who received votes: ", unique_candidate_list)

# The percentage of votes each candidate won



# The total number of votes each candidate won

# The winner of the election based on popular vote.