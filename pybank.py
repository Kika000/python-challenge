# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

csvpath = os.path.join('..','python-challenge','Resources','budget_data.csv')
# print(csvpath)

totalNumMonth = 0
totalProfit_Loss = 0
month_change = 0
total_AverageChange = 0
prior_rev = 0
total_month_Change = 0
GrIncrProf = 0
GrDecrLoss = 0


with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # print(csv_header)
    for row in csvreader:
        totalNumMonth = totalNumMonth + 1
        this_rev = int(row[1])
        totalProfit_Loss = totalProfit_Loss + this_rev
        

        if totalNumMonth >= 2:
            month_change = this_rev - prior_rev
            total_month_Change= total_month_Change + month_change
        prior_rev = this_rev 
        

        if month_change> GrIncrProf:
            GrIncrMonth=row[0]
            GrIncrProf= month_change
            # print("Month" + str(GrIncrMonth) + "  " + "Change = " + str(GrIncrProf))
        if month_change<  GrDecrLoss:
            GrDecrMonth=row[0]
            GrDecrLoss= month_change

total_AverageChange = total_month_Change/(totalNumMonth-1)



print("Total number of months are:" + str(totalNumMonth))
print("Total Profit and Loss:" + str(totalProfit_Loss))
print("Total month Change = " + str(total_month_Change))
print ("Total Average Change " + str(total_AverageChange))
print ("Greatest Increase in Profits = " + str(GrIncrMonth)+ "  " + str(GrIncrProf) )
print ("Greatest Increase in Profits = " + str(GrDecrMonth)+ "  " + str(GrDecrLoss) )



       