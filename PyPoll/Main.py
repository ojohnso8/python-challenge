#import
import os
import csv

#csv path
election_csv = os.path.join(".", "election_data.csv")

#empty dictionary

poll_data = {}
poll_percentage = {}

#empty lists

votes = []
candidateList= []
unique_candidate_list = []
winning_count = 0
winning_candidate = ""
winner_list = []

#open csv
with open(election_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:

        votes.append(row[0])
        # candidateList.append(row[2])
        candidate_name = row[2]
        if candidate_name not in unique_candidate_list:
            unique_candidate_list.append(candidate_name)
# The total number of votes each candidate won   
            poll_data[candidate_name] = 0 #reset count
        poll_data[candidate_name] += 1 #adding up votes; total votes
    print(unique_candidate_list) #checkwork
    print(poll_data) #checkwork

# The total number of votes cast  
    total_votes = len(votes)
    print("Total Votes: ", total_votes) #checkwork

# The percentage of votes each candidate won
    for (key, value) in poll_data.items():
        poll_percentage[key] = round(float(value/total_votes * 100), 2)
    print(poll_percentage)

# The winner of the election based on popular vote.
    for candidate in poll_data:
        votes = poll_data[candidate]
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate  
    print(winning_candidate) #check work
    print(winning_count) #check work


#write output
output_path = os.path.join(".", "election_results.txt")

with open(output_path, 'w') as writefile:
    writefile.writelines('Election Results' + '\n')
    writefile.writelines('------------------------' + '\n')
    writefile.writelines('Total Votes: ' + str(total_votes) + '\n')
    writefile.writelines('------------------------' + '\n')
    # writefile.writelines('Total $' + str(total_amount) + '\n')
    writefile.writelines('------------------------' + '\n')
    writefile.writelines('Winner: ' + winning_candidate + '\n')