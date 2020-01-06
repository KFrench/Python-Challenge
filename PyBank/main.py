#Import so that code is recognized 
import csv
import os
import statistics 

#Create lists for calculations
Count_Months=[]
Count_Profit=[]
Aver_Change=[]

#set up csv file to import
budget_data = os.path.join("Resources","budget_data.csv")

#Open csv and read csv
with open(budget_data, "r") as New:
    csv_reader=csv.reader(New)
   
   #skip the headers 
    next(csv_reader) 
   
   #Create variables for calculating average change
    cur_month = None  
    pre_month = None 
    total_change = []

   #Create loop for reading through each row in the csv file
    for row in csv_reader:
        Count_Months.append(row[0])
        Count_Profit.append(int(row[1]))
    print(f"Total Number of Months:{len(Count_Months)}")
    
    # Sum numeric values for profit/loss
    Sum_Count_Profit=sum(Count_Profit)
    print(f"Total Profit/Loss:${Sum_Count_Profit}")
   
    #find the average change 
        if cur_month is None: 
            cur_month = int(row[1])
            pre_month = int(row[1])
        else:
            cur_month = int(row[1])
            total_change.append(cur_month - pre_month)
    Average_Change=sum(total_change)/len(total_change)
    print(f"Average Change:${Average_Change}")
   
    #Find greatest increase 
   