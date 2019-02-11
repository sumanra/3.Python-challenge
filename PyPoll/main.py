# Modules
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
    Khan_Counter = 0
    Correy_Counter = 0
    Li_Counter = 0
    Tooley_Counter = 0
    percent_Khan = 0.000
    percent_Correy = 0.000
    percent_Li = 0.000
    percent_Tooley = 0.000

    for row in csvreader:
        #Total number of votes
        total_votes = total_votes +1
        #  The percentage of votes each candidate won
        #  The total number of votes each candidate won

  
        if str(row[2]) == "Khan" :
            Khan_Counter = Khan_Counter + 1
            percent_Khan = round((int(Khan_Counter) / int(total_votes)*100), 3)
        
        elif str(row[2]) == "Correy" :
            Correy_Counter = Correy_Counter + 1
            percent_Correy = round((int(Correy_Counter) / int(total_votes)*100), 3)

        elif str(row[2]) == "Li" :
            Li_Counter = Li_Counter + 1
            percent_Li = round((int(Li_Counter) / int(total_votes)*100), 3)
            

        elif str(row[2]) == "O'Tooley" :
            Tooley_Counter = Tooley_Counter + 1
            percent_Tooley = round((int(Tooley_Counter) / int(total_votes)*100), 3)
        else :
            print("No one from the list")

# Checking the Winner of the Election
    if Khan_Counter > Correy_Counter and Khan_Counter > Li_Counter and Khan_Counter > Tooley_Counter :
        Winner = str("Khan")
    elif Correy_Counter > Li_Counter and Correy_Counter > Tooley_Counter :
        Winner = str("Correy")
    elif Li_Counter > Tooley_Counter:
        Winner = str("Li")
    else:
        Winner = str("O'Tooley")
        
#The path for the filename

electiondata_output = os.path.join("electiondata.txt")
with open(electiondata_output, "w", newline="") as textfile:

# Printing everything
    print_and_write(textfile, "```text \n")
    print_and_write(textfile, "Election Results \n")
    print_and_write(textfile, "-------------------------------- \n")
    print_and_write(textfile, f"Total Votes: {total_votes} \n")
    print_and_write(textfile, "-------------------------------- \n")
    print_and_write(textfile, f"Khan: {percent_Khan}% ({Khan_Counter})  \n")
    print_and_write(textfile, f"Correy: {percent_Correy}% ({Correy_Counter}) \n")
    print_and_write(textfile, f"Li: {percent_Li}% ({Li_Counter}) \n")
    print_and_write(textfile, f"O'Tooley: {percent_Tooley}% ({Tooley_Counter}) \n")
    print_and_write(textfile, "-------------------------------- \n")
    print_and_write(textfile, f"Winner:{Winner} \n")
    print_and_write(textfile, "-------------------------------- \n")
    print_and_write(textfile, "``` \n")