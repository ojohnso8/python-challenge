#import
import os
import csv

#create csv path
budget_csv = os.path.join(".", "budget_data.csv")

#Create empty lists for months and revenue
months = []
revenue = []

#open csv
with open(budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)


#append month and revenue data from csv into empty lists created in lines 9 and 10
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

#calculate total months
    total_months = len(months)
    print("Total Months: ", total_months)

#calculate the net total amount of "Profit/Losses" over the entire period
    total_amount = sum(revenue)
    print("Total: $",total_amount)

 #calculate the average of the changes in "Profit/Losses" over the entire period 
 #average change = new value - old value/old value * 100 ; x = rows
    # for x in revenue:
    average = sum(revenue)/total_months
        # average_change = (revenue[x + 1] - revenue[x])/revenue[x] * 100
        # print(average_change)
    print("Average Change: $", round(average, 2))

# The greatest increase in profits (date and amount) over the entire period
    greatest_inc = 0
    greatest_dec = 0
    
    # for x in range(len(revenue)):
    #     if revenue[x] >= greatest_inc:
    #         greatest_inc = revenue[x]
    #         print(x)

 
# The greatest decrease in losses (date and amount) over the entire period