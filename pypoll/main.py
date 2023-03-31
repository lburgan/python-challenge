import os 
import csv

total_votes = 0
candidates = []

#read the election csv into python 
poll_path = os.path.join("Resources","election_data.csv")
with open(poll_path, "r") as poll_csv:
    poll = csv.reader(poll_csv, delimiter= ",")

    header = next(poll)
    first_row = next(poll)
   
    total_votes += 1

    for row in poll:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
  

        


    

print(candidates)
