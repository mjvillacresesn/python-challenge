import os
import csv

#Find path
pybank_file = os.path.join(".", "budget_data.csv")
pybank_outfile = os.path.join(".", "budget_data_output.txt")

#Store Varibles
totalm = 0
PLlist = 0
averagec = 0.0
monthpl = []
date = []
newV = []
moschangel = []
i = 0
totalchange = 0
meanaverage = 0.0
lists ={"" , 0}

#open file and check you can read it
with open(pybank_file, newline="") as bankfile:
    csvreader = csv.reader(bankfile, delimiter=",")
    #print(csvreader)
    #read header
    header = next(bankfile)
    #print(f"{header}")

#1.The total number of months included in the dataset
#For loop and len count each value
    for each in csvreader:
        #1. print(each)
        totalm = totalm + 1

        # 2. add all P/L list
        PLlist = ((PLlist) + int(each[1]))


        #append all values into a new list to later draw out monthly change
        monthpl.append(each[1])
        date.append(each[0])
    print(date)
    #print(monthpl)
    #print


    #create function for all values in list "monthpl", where rowb is subtracted from rowa
    def monthlyAverage(RowB, RowA):
        return (float(int(RowA) - int(RowB)))
#3. then, run the for loop for each item in list where P/L are contained
for row in monthpl:
    #first parameter is saying pick row 1, - 1 = row 0 == RowB, then row == row 1 == rowA
    newV = float(monthlyAverage(monthpl[i - 1], row))
    #add each function result to this list
    moschangel.append(newV)
    #print(moschangel)
    i = i + 1

moschangel[0] = 0
#Total sum of montlhy average change
#print(moschangel)
for sum in range(len(moschangel)):
    totalchange = totalchange + moschangel[sum]

meanaverage = round(totalchange / (len(moschangel) - 1), 2)
#print(totalchange)
#print(meanaverage)
#print(totalm)
#print(PLlist)

#4.  &  5. Finding greatest increase and Decrease using max and min functions
maximum = int(max(moschangel))
maxk = moschangel.index(maximum)
indK = date[maxk]
#print(indK)
minimun =int(min(moschangel))
minL = moschangel.index(minimun)
indL = date[minL]
#print(maximum)
#print(minimun)

tolMonV = ("Total Months: " + str(totalm))
tolnetV = ("Total: $" + str(PLlist))
AvgChange = ("Average Change: $" + str(meanaverage))
max_calc = ("Greatest Increase in Profits: " + indK + " ($" + str(maximum) + ")")
min_calc = ("Greatest Decrease in Profits: " + indL + " ($" + str(minimun) + ")")
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

with open(pybank_outfile, "w") as resultsbank:
    writer = csv.writer(resultsbank)

    for row in output:
        resultsbank.write(row + '\n')