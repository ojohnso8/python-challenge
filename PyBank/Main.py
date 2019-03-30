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
    # print("Total Months: ", total_months)

#calculate the net total amount of "Profit/Losses" over the entire period
    total_amount = sum(revenue)
    # print("Total: $",total_amount)

 #calculate the average of the changes in "Profit/Losses" over the entire period 
    average = sum(revenue)/total_months
    # print("Average Change: $", round(average, 2))

# The greatest increase/decrease in profits (date and amount) over the entire period
    greatest_increase= 0
    greatest_decrease= 0
    inc = 0
    dec = 0
  
    for inc in range(len(revenue)):
        if (revenue[inc]) - (revenue[inc -1 ]) > greatest_increase:
            greatest_increase = (revenue[inc]) - (revenue[inc - 1])
            greatest_inc_month = months[inc]

    # print('Greatest Increase Month ', greatest_inc_month) 
    # print('Greatest Increase Amt ', '$',greatest_increase)
   

    for dec in range(len(revenue)):
        if  (revenue[dec]) - (revenue[dec- 1]) < greatest_decrease:
            greatest_decrease = (revenue[dec]) - (revenue[dec - 1])
            greatest_dec_month = months[dec]
    # print('Greatest Decrease Month ', greatest_dec_month)
    # print('Greatest Decrease Amt ', '$',greatest_decrease)

#print to terminal

    print("Financial Analysis")
    print('------------------------')
    print("Total Months: ", total_months)
    print("Total: $",total_amount)
    print("Average Change: $", round(average, 2))
    print('Greatest Increase Month ', greatest_inc_month) 
    print('Greatest Increase Amt ', '$',greatest_increase)
    print('Greatest Decrease Month ', greatest_dec_month)
    print('Greatest Decrease Amt ', '$',greatest_decrease)

#write output
output_path = os.path.join(".", "budget_output.txt")

with open(output_path, 'w') as writefile:
    writefile.writelines('Financial Analysis' + '\n')
    writefile.writelines('------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total $' + str(total_amount) + '\n')
    writefile.writelines('Average Change: $' + str(round(average, 2)) + '\n')
    writefile.writelines('Greatest Increase: ' + str(greatest_inc_month) + ' $' + str(greatest_increase) + '\n')
    writefile.writelines('Greatest Decrease: ' + str(greatest_dec_month) + ' $' + str(greatest_decrease) + '\n')
