# #Election Result Analysis
import os
import csv

def print_and_write(file, data):
    print(data, end="")
    file.write(data)


electiondata_csv = os.path.join("election_data.csv")

with open(electiondata_csv, newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

 # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
  
    #print(f"CSV Header: {csv_header}")
#  Assigning the value
    total_votes = 0

    candidate_vote_counts = {} 
    #Creating dictionary to read all the votes, count the total and find unique candidates
    for row in csvreader:
        candidate_name = row[2]
        if candidate_name in candidate_vote_counts:
            candidate_vote_counts[candidate_name] += 1
        else:
            candidate_vote_counts[candidate_name] = 1
    total_votes = sum(candidate_vote_counts.values())

    #The path for the filename
    output_file = os.path.join("electiondata.txt")

    #Write data to a .txt file
    with open(output_file, "w", newline="") as textfile:
        print_and_write(textfile, "```text \n")
        print_and_write(textfile, "Election Results \n")
        print_and_write(textfile, "-------------------------------- \n")
        print_and_write(textfile, f"Total Votes: {total_votes} \n")
        print_and_write(textfile, "-------------------------------- \n")

        for candidate_name in candidate_vote_counts.keys():     

            #Calculate the percentage of votes for each candidate
            percent_votes = candidate_vote_counts[candidate_name] / total_votes * 100
            #Printing and writing
            print_and_write(textfile, "%s: %.3f %% (%i)\n" % (candidate_name, percent_votes, candidate_vote_counts[candidate_name]))
        
        #Winner equals the key with the largest value
        winner= max(candidate_vote_counts, key=candidate_vote_counts.get)


        print_and_write(textfile, "-------------------------------- \n")
        print_and_write(textfile, f"Winner: {winner} \n")
        print_and_write(textfile, "-------------------------------- \n")
        print_and_write(textfile, "``` \n")