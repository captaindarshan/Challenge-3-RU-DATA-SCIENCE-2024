import csv
import os
#imported libraries

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data_csv) as budget_data_csv_file:
    budget_data_csv_reader = csv.reader(budget_data_csv_file, mode = 'r')

    print(budget_data_csv_reader)
