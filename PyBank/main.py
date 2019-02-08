# Modules
import os
import csv

budgetdata_csv = os.path.join("budget_data.csv")

with open(budgetdata_csv, newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

 # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
  
    #print(f"CSV Header: {csv_header}")

    # assigning the value
    total = 0
    months = 0
    average = 0.0

    greatest = ["", 0]
    least = ["",0]
   # max_index = 0
    #least_index = 0
    change_in_profit = [0.0]
    lenght = 0
    average1 = 0
    Profit_Loss_in_previous_row = 0
    change_in_profit_Sum = 0

    for row in csvreader:
               
        total+= int(row[1])
        months= months+1
        
       # print(Profit_Loss_in_previous_row)
        if (months > 1) :
            #change_in_profit.append((int(row[1]))
            change_in_profit.append( (int(row[1]) - Profit_Loss_in_previous_row))

        Profit_Loss_in_previous_row = int(row[1])
   
       #finding greatest and least increase i  profit and loss
        #if int(row[1]) == int(greatest[1]):
        #    greatest[0] = row[0]
        
        #if int(row[1]) < int(least [1]):
        #    least[0] = row[0]

change_in_profit_Sum = sum(change_in_profit)
#print(change_in_profit_Sum)
average = round((change_in_profit_Sum/(months-1)),2)
greatest[1] = max(change_in_profit)
#finding the max index
#max_index = change_in_profit.index(greatest[1])
#finding the min index
least[1] = min(change_in_profit)

# Printing everything
print("```text")
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average  Change: ${average}")
print(f"Greatest Increase in Profits:  {greatest[0]}  (${greatest[1]})")
print(f"Greatest Decrease in Profits:  {least[0]}  (${least[1]})")
print("```")

