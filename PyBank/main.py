#Import so that code is recognized 
import csv
import os
import statistics 
#Create Variables for calculations
Count_Months=[]
Count_Profit=[]
Aver_Change=[]
#set up csv file to import
budget_data = os.path.join("..","Python-Challenge-master","PyBank","Resources","budget_data.csv")
#print("I ran")
#Open csv and read csv
with open("/Users/test/Desktop/Python-Challenge-master/PyBank/Resources/budget_data.csv", "r") as New:
    csv_reader=csv.reader(New)
   #skip the headers 
    next(csv_reader) 
    #for line in csv_reader: 
       #print(line)
    #this loop will create list for total number of months and profit/losses to be calculated
    #Counter=0
    for row in csv_reader:
        Count_Months.append(row[0])
        Count_Profit.append(int(row[1]))
        #Counter=+-1
        #print(len(Counter))
    print(f"Total Number of Months{Count_Months}")
    print(f"Total Profit/Loss:{len(Count_Profit)}")
  