import os
import csv

poll_infile = os.path.join(".", "election_data.csv")
poll_outfile = os.path.join(".", "election_results.txt")

#List to store data
CandidatesList = []
KhanV = []
Correy = []
Li = []
otherc = []
KhanV2 = 0
Correy2 = 0
Li2 = 0
Other2 = 0
KhanPercent = 0
CorreyPercent = 0
LiPercent = 0
OTooleyPercent = 0
WinnerCounter = []

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
            KhanV2 += 1
        elif eachword == "Correy":
            Correy.append("1")
            Correy2 += 1
        elif eachword == "Li":
            Li.append("1")
            Li2 += 1
        else:
            otherc.append("1")
            Other2 += 1

counterKha = sum(1 for numb in KhanV)
WinnerCounter.append(counterKha)
counterCor = sum(1 for numb in Correy)
WinnerCounter.append(counterCor)
counterLi = sum(1 for numb in Li)
WinnerCounter.append(counterLi)
counterOte = sum(1 for numb in otherc)
WinnerCounter.append(counterOte)

Consolidated_count = {"Khan": KhanV2,
                     "Correy": Correy2,
                    "Li": Li2,
                    "Other": Other2}

for winner in Consolidated_count:
    if KhanV2 > Correy2:
        winnerCand = "Khan"
        break
        if Correy2 > Li2:
            winnerCand = "Correy"
            break
            if Li2 > Other2:
                winnerCand = "Li"
                break
                if Other2 > KhanV2:
                    winnerCand = "O'Tooley"

W = ("Winner: " + str(winnerCand))

KhanPercent =("Khan: {0:.0%}".format(counterKha/vote_count))
CorreyPercent =("Correy: {0:.0%}".format(counterCor/vote_count))
LiPercent =("Li: {0:.0%}".format(counterLi/vote_count))
OTooleyPercent =("O'Tooley: {0:.0%}".format(counterOte/vote_count))

header = "Election Results"
skipper = "----------------------------------"
K = (str(KhanPercent) + " " +"(" + str(counterKha) + ")")
C = (str(CorreyPercent) + " " +"(" + str(counterCor) + ")")
L = (str(LiPercent) + " " +"(" + str(counterLi) + ")")
O = (str(OTooleyPercent) + " " +"(" + str(counterOte) + ")")
#! Sill working on extracting "khan" as the winner
#Winner = "Winner: Khan"
#winner =max()
print(f"{header}\n"
      f"{skipper}\n"
      f"{tol_count}\n"
      f"{skipper}\n"
      f"{K}\n"
      f"{C}\n"
      f"{L}\n"
      f"{O}\n"
      f"{skipper}\n"
      f"{W}\n"
      f"{skipper}\n")

finalR = [header, skipper, tol_count, skipper,
          K, C, L, O, skipper, W, skipper]

with open(poll_outfile, "w") as resultspoll:
    writpoll = csv.writer(resultspoll)

    for row in finalR:
        resultspoll.write(row + '\n')



