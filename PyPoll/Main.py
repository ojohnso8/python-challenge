#import
import os
import csv

#csv path
election_csv = os.path.join(".", "election_data.csv")

#empty dictionary

poll_data = {}
poll_percentage = {}

#empty lists/declarations

votes = []
unique_candidate = []
winning_count = 0
winning_candidate = ""
winner_list = []

#open csv
with open(election_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        
        votes.append(row[0])
#Get list of unique candidate names
        candidate_name = row[2]
        if candidate_name not in unique_candidate:
            unique_candidate.append(candidate_name)

# calculate total number of votes each candidate won   
            poll_data[candidate_name] = 0 #reset count
        poll_data[candidate_name] += 1 #adding up votes; total votes
    print(unique_candidate) #checkwork
    print(poll_data) #checkwork

# calculate total number of votes cast  
    total_votes = len(votes)
    print("Total Votes: ", total_votes) #checkwork

# calculate percentage of votes each candidate won
    for (key, value) in poll_data.items():
        poll_percentage[key] = round(float(value/total_votes * 100), 2)
    print(poll_percentage)

# figure out the winner of the election based on popular vote.
    for candidate in poll_data:
        votes = poll_data[candidate]
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate  
    print(winning_candidate) #check work
    print(winning_count) #check work

#print to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: ", total_votes)
print("--------------------------")

#TAs: I've tried multiple ways to try and format the data below the way it should be in the 
#example without luck. I believe the formatting trouble has to do with the way I wrote the code
#above/logic flow. I have tried different combinations of the f-string to try and tease out individual 
#values to group by candidate. But when I have done that, I have gotten some odd combinations (ie. only
#one candidate name printing out and/or one vote count.)
print(unique_candidate)
print(poll_percentage)
print(poll_data)
print("---------------------------")
print(f"Winner: {winning_candidate}")
print("---------------------------")

#write output
output_path = os.path.join(".", "election_results.txt")

with open(output_path, 'w') as writefile:
    writefile.writelines('Election Results' + '\n')
    writefile.writelines('------------------------' + '\n')
    writefile.writelines('Total Votes: ' + str(total_votes) + '\n')
    writefile.writelines('------------------------' + '\n')
    writefile.writelines(str(unique_candidate) + '\n')
    writefile.writelines(str(poll_percentage) + '\n')
    writefile.writelines(str(poll_data) + '\n')
    writefile.writelines('------------------------' + '\n')
    writefile.writelines('Winner: ' + winning_candidate + '\n')