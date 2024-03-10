import csv
import os
from pathlib import Path
 
#imported libraries

Total_months = 0
Total = 0
Average_change = 0
Greatest_Profit_Increase = 0
Greatest_Profit_Decrease = 0
#Output variables 

Date = []
Profit_Losses = []
#store csv data in these

Profit_Loss_calc = []

budget_data_csv = os.path.join("ResourcesPyBank", "budget_data.csv") #this calls the csv file and this works now 

with open(budget_data_csv) as budget_data_csv_file:
    budget_data_csv_reader = csv.reader(budget_data_csv_file, delimiter = ',') # ',' as delimiter does what? delimiter is what separates values in csv file 
    next(budget_data_csv_reader)

    for row in budget_data_csv_reader:
       Date.append(row[0])
       Profit_Losses.append(int(row[1]))
       #saves Data and Profit/Losses in tables 

    for month_count in range(len(Profit_Losses)-1):
        Profit_Loss_calc.append(Profit_Losses[month_count+1]-Profit_Losses[month_count])

#Outputs
total_months = len(Date)     
total_money = sum(Profit_Losses)

Greatest_Profit_Increase = max(Profit_Loss_calc)
Greatest_Profit_Decrease = min(Profit_Loss_calc)
Average_change = round(sum(Profit_Loss_calc)/len(Profit_Loss_calc),2)

Greatest_Increase_month = Profit_Loss_calc.index(max(Profit_Loss_calc))+1 #these two give the index value for the month in the month column but not the actual date
Greatest_Decrease_month = Profit_Loss_calc.index(min(Profit_Loss_calc))+1

#outputs to terminal screen
print("Financial Analysis")
print("Total months: ", total_months)
print("Total: ", total_money)
print("Average Change: ", Average_change)
print(f"Greatest Increase in Profits: {Date[Greatest_Increase_month]} ${(str(Greatest_Profit_Increase))}")
print(f"Greatest Decrease in Profits: {Date[Greatest_Decrease_month]} ${(str(Greatest_Profit_Decrease))}")

#prints to .txt file 
financial_output_txt_file = Path("..", "PyBank", "AnalysisPyBank", "PyBank_text_file_outputs")

with open(financial_output_txt_file, "w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")

    file.write("Total Months: ")
    file.write(str(total_months))
    file.write("\n")
    
    file.write("Total Profit: ")
    file.write(str(total_money))
    file.write("\n")

    file.write("Average Change: ") 
    file.write(str(Average_change))
    file.write("\n")

    file.write(f"Greatest Increase in Profits: {Date[Greatest_Increase_month]} ${(str(Greatest_Profit_Increase))}")
    file.write("\n")

    file.write(f"Greatest Decrease in Profits: {Date[Greatest_Decrease_month]} ${(str(Greatest_Profit_Decrease))}")