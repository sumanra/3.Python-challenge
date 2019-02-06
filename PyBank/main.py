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
    a = ["", 0]
    b = 0.0
    greatest = ["", 0]
    least = ["",0]
    average_change = 0.0
    lenght = 0
#    def average(row):
#        length = len(row)
 #       average_change = 0.0
#        for rows in row:
#            average_change += rows
#    return average_change / (length-2)
    for row in csvreader:
        #print(row)
        lenght = len(row)
        total = total + int(row[1])
        months= months+1
        a = row[1]
        b = [s.split(',') for s in a]
        average_change = float(average_change) - float(row[1])
        average = average_change/(lenght-2)
        try:
            print(average)
        except ZeroDivisionError:
            print ("You can't divide by zero!")
        #average_ = int(row[months+1]))-int(row[1])/(months-1)   
        #average = (total/months)
        
       

        if int(row[1]) > int(greatest [1]):
            greatest = row
        
        if int(row[1]) < int(least [1]):
            least = row
#average = average_change/(row- 2)    
# Printing everything
print("```text")
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average  Change: ${average}")
print(f"Greatest Increase in Profits:{greatest}")
print(f"Greatest Decrease in Profits:{least}")
print("```")

