import os
import csv

#path to collect data saved in my repo
banking_upload = os.path.join(".", "budget_datar.csv")
banking_output = os.path.join(".", "budget_results.txt")

#List to store data
tot_months = 0
tol_net = 0
average_change = 0
loss_list = ["", 0]

#find total # months and total net value, loop
with open(banking_upload, "r") as csvfile:
    bankdata = csv.reader(csvfile, delimiter=",")
    #print("i can read it!")

    #!reads the header row
    header = next(bankdata)
    firstRow = next(bankdata)
    tot_months = tot_months + 1
    firstnumber = int(firstRow[1])
    tol_net = tol_net + int(firstRow[1])

    for line in bankdata:
        tot_months = tot_months + 1
        #!explain logic
        tol_net = tol_net + int(line[1])

tolnetV = ("Total Profit: ${:,}".format(tol_net))

#find max and min, loop, list
with open(banking_upload, 'r') as secnd:
    next(secnd)
    for row in csv.reader(secnd):
        profit = [int(row[1]) for row in csv.reader(secnd)]

maxProfit = max(profit)
minProfit = min(profit)
#gives $ value to interger
#max_calc = ("${:,}".format(maxProfit)) or see below
max_calc = ("Greatest Increase in Profits ${:,}".format(maxProfit))
min_calc = ("Greatest Decrease in Profits: ${:,}".format(minProfit))

#simple avg: divide total net by total months
average_change = int(tol_net / tot_months)
AvgChange = ("Average Change: ${:,}".format(average_change))

print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {tot_months}")
print(tolnetV)
print(AvgChange)
print(max_calc)
print(min_calc)