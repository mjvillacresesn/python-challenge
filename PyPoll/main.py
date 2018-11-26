import os
import csv

poll_infile = os.path.join(".", "election_data.csv")
#poll_outfile = os.path.join(".", "election_results.txt")

#List to store data
#Khan = []
#Correy = []
#Li = []
#OTooley = []
CandidatesList = []
KhanV = []
Correy = []
Li = []
otherc = []


#find total # months and total net value, loop
with open(poll_infile, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    next(csvreader)
    #count number of votes
    vote_count = sum(1 for line in csvreader)
    tol_count = ("Total Votes:{:,}".format(vote_count))

with open(poll_infile, 'r') as another:
    next(another)
    for row in csv.reader(another):
        CandidatesList = [str(row[2]) for row in csv.reader(another)]
        #print(CandidatesList)
    for eachword in CandidatesList:
        if eachword == "Khan":
            KhanV.append("1")
        elif eachword == "Correy":
            Correy.append("1")
        elif eachword == "Li":
            Li.append("1")
        else:
            otherc.append("1")


header = "Election Results\n"
skipper = "----------------------------------\n"
print(f"{header}\n"
      f"{skipper}\n"
      f"{tol_count}\n"
      f"{skipper}\n")
skipper = "----------------------------------\n"
counterKha = sum(1 for numb in KhanV)
print(f"Khan: {counterKha}")

counterCor = sum(1 for numb in Correy)
print(f"Correy: {counterCor}")

counterLi = sum(1 for numb in Li)
print(f"Li: {counterLi}")

counterOte = sum(1 for numb in otherc)
print(f"O'Tooley: {counterOte}")
#counterKha = sum(1 for num in Khan)
#print(counterKha)
