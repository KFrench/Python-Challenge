#Import so that code is recognized 
import csv
import os
import statistics 

#set up csv file to import
election_data = os.path.join("Resources","election_data.csv")

#Open csv and read csv
with open(election_data, "r") as New:
    csv_reader=csv.reader(New, delimiter=",")

     #skip the headers 
    next(csv_reader) 
    
    #for line in csv_reader:
        #print(line)

    #Create variables for all calculations
    tot_votes = 0
    #Candidate Names as a dictionary 
    candi_Name = {}
    #Find the winner 
    winner = " "
    winner_count_vote = 0

    #Create the loop to evaluate each row in the file
    for row in csv_reader:
        tot_votes = tot_votes + 1

        if row[2] in candi_Name:
            candi_Name[row[2]] = candi_Name[row[2]] + 1
        else:
            candi_Name[row[2]] = 1
    
    for candidates_name in candi_Name:
        num_of_vote = candi_Name [candidates_name]
        percentage = (candi_Name [candidates_name] / tot_votes) * 100 

        if num_of_vote > winner_count_vote:
            winner_count_vote = num_of_vote
            winner = candi_Name 

    print(f"Total Votes:{tot_votes}")
    print(f"{candi_Name}: {percentage:.3f}% ({num_of_vote})")
    print(f"Winner: {winner}") 