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
tolMonV = ("Total Months: {:,}".format(tot_months))
tolnetV = ("Total Profit: ${:,}".format(tol_net))

#find max and min, for loop, create a list stored as profit
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
result_header = "Financial Analysis:"
skipper = "----------------------------------------"

print(f"{result_header}\n"
      f"{skipper}\n"
      f"{tolMonV}\n"
      f"{tolnetV}\n"
      f"{AvgChange}\n"
      f"{max_calc}\n"
      f"{min_calc}\n")

output = [result_header, skipper, tolMonV, tolnetV, AvgChange,
          max_calc, min_calc]

with open(banking_output, "w") as resultsf:
    writer = csv.writer(resultsf)
    
    for row in output:
        resultsf.write(row + '\n')



