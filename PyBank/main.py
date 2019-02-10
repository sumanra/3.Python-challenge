## Bank Budget Analysis ##
import os
import csv

def print_and_write(file, data):
    print(data, end="")
    file.write(data)

budgetdata_csv = os.path.join("budget_data.csv")

#Open and read the CSV
with open(budgetdata_csv, newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

 # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
  
    # assigning the value
    total = 0
    months = 0
    average = 0.0
    date = []
    greatest = ["",0]
    least = ["",0]
    change_in_profit = [0]
    Profit_Loss_in_previous_row = 0
    change_in_profit_Sum = 0
# Calculation
    for row in csvreader:
        #Total profits/losses for the period       
        total+= int(row[1])
        #The number of months
        months= months+1
        #List of dates
        date.append(row[0])
       
        if (months > 1) :
            #change_in_profit.append((int(row[1]))
            change_in_profit.append( (int(row[1]) - Profit_Loss_in_previous_row))
            
        Profit_Loss_in_previous_row = int(row[1])
   
# Sum of total change in profit/loss
change_in_profit_Sum = sum(change_in_profit)

#Average  Change: and round it to two decimal
average = round((change_in_profit_Sum/(months-1)),2)
#Greatest Increase in Profits:
greatest[1] = max(change_in_profit)
#finding the max index
max_index = change_in_profit.index(greatest[1])
#Greatest Increase in Profits Dates:
max_change_date = date[max_index]
#Greatest Decrease in Profits:
least[1] = min(change_in_profit)
#finding the min index
min_index = change_in_profit.index(least[1])
#Greatest Decrease in Profits dates:
min_change_date = date[min_index]

#Create the path for the filename
budgetdata_output=os.path.join("budgetdata.txt")
# Printing everything
with open(budgetdata_output, "w", newline="") as textfile:
    print_and_write(textfile, "```text \n")
    print_and_write(textfile, "Financial Analysis \n")
    print_and_write(textfile, "-------------------------------- \n")
    print_and_write(textfile, f"Total Months: {months} \n")
    print_and_write(textfile, f"Total: ${total} \n")
    print_and_write(textfile, f"Average  Change: ${average} \n")
    print_and_write(textfile, f"Greatest Increase in Profits:  {max_change_date}  (${greatest[1]}) \n")
    print_and_write(textfile, f"Greatest Decrease in Profits:  {min_change_date}  (${least[1]}) \n")
    print_and_write(textfile, "``` \n")
