import os 
import csv

total_votes = 0
candidates = []
individual_votes = []
vote_percent = []

#read the election csv into python 
poll_path = os.path.join("Resources","election_data.csv")
with open(poll_path, "r") as poll_csv:
    poll = csv.reader(poll_csv, delimiter= ",")
    #read in the header
    header = next(poll)

    #if a candidate is not in our list, add them to our list and count a vote for them
    #if they are in our list, find where they are and add a vote to them
    for row in poll:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            individual_votes.append(1)
        else:
            person = candidates.index(row[2])
            individual_votes[person] += 1  
    #find percents of each votes and add to a list 
    for votes in individual_votes:
        percent = round(((votes/ total_votes)*100),3)
        vote_percent.append(percent)
    #find the winner! 
    winner_index= individual_votes.index(max(individual_votes))
    winner = candidates[winner_index]
#lots of printing 
print("Election Results\n-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for person in candidates:
    person_index = candidates.index(person)
    print(f"{person}: {vote_percent[person_index]}% ({individual_votes[person_index]}) ")
    print("\n")
print("-------------------------\n")      
print(f"Winner:{winner}")

#export to a .txt file 
output_path = os.path.join("Resources", "results.txt")

# Open the file using "write" mode
with open(output_path, 'w') as new_txt:
    new_txt.write("Election Results\n-------------------------\n")
    new_txt.write(f"Total Votes: {total_votes}\n")
    new_txt.write(f"-------------------------\n")
    for person in candidates:
        person_index = candidates.index(person)
        new_txt.write(f"{person}: {vote_percent[person_index]}% ({individual_votes[person_index]}) ")
        new_txt.write("\n")
    new_txt.write("-------------------------\n")      
    new_txt.write(f"Winner:{winner}")
    

