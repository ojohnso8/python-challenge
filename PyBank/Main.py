#import
import os
import csv

#csv path
budget_csv = os.path.join(".", "budget_data.csv")

#Must create empty lists for months and revenue
months = []
revenue = []

#open csv
with open(budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

#append to put data from row[0] and row[1] into the lists created above
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

#total months
    total_months = len(months)
    print("Total Months: ", total_months)

# The net total amount of "Profit/Losses" over the entire period
    total_amount = sum(revenue)
    print("Total: $",total_amount)

# The average of the changes in "Profit/Losses" over the entire period
# you have to find calculate the % change for each row...
# then add the averages
# then divide average total by the number of months
# [(new value - old value) / old value] * 100 

    average_change = round(total_amount/total_months, 2)
    print("Average Change: $", average_change)

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period
