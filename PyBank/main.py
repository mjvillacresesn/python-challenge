import os
import csv

#path to collect data saved in my repo
banking_upload = os.path.join(".", "budget_datar.csv")
banking_output = os.path.join(".", "budget_results.txt")

#List to store data
tot_months = 0
tol_net = 0
average_change = []
profit_list = []
loss_list = ["", 0]
profitDic = {}

with open(banking_upload, "r") as csvfile:
    bankdata = csv.reader(csvfile, delimiter=",")
    #print("i can read it!")

    #!reads the header row
    header = next(bankdata)
    firstRow = next(bankdata)
    tot_months = tot_months + 1
    firstnumber = int(firstRow[1])
    tol_net = tol_net + int(firstRow[1])

    for row in bankdata:
        profit_list.append(tol_net)
        profit_list = [line.rstrip('\n') for line in csvfile]
        profitDic = profit_list
           # if profit_list


    for row in bankdata:
        tot_months = tot_months + 1
        #!explain logic
        tol_net = tol_net + int(row[1])
        #max

    average_change = int(tol_net / tot_months)


print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {tot_months}")
print(f"Total: ${tol_net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {profit_list}")
print(f"Greatest Decrease in Profits: {loss_list}")
print(max(profit_list))