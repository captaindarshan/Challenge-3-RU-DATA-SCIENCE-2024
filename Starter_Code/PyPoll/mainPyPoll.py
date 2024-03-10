import os
import csv
from pathlib import Path
#imported libraries 

total_votes = 0 
votes_Stockham = 0
votes_DeGette = 0
votes_Doane = 0

poll_data_csv = os.path.join("Resources", "election_data.csv")

with open(poll_data_csv) as poll_data_csv_file:
    poll_data_csv_reader = csv.reader(poll_data_csv_file, delimiter = ',')
    next(poll_data_csv_reader)

    for row in poll_data_csv_reader:
      total_votes += 1

      if row[2] == "Charles Casper Stockham" :
        votes_Stockham += 1 
      elif row[2] == "Diana DeGette" :
        votes_DeGette += 1
      elif row[2] == "Raymon Anthony Doane" :
        votes_Doane += 1


#make dictionary to find winners 
candidates = ["Charles Casper Stockham", "Diana Degette", "Raymon Anthony Doane"]    
candidate_votes =[votes_Stockham, votes_DeGette, votes_Doane]

dict_candidates_with_votes = dict(zip(candidates, candidate_votes))
key_winner = max(dict_candidates_with_votes, key = dict_candidates_with_votes.get)
key_winner_str = str(key_winner)

#winner percents
Stockham_percent = round((votes_Stockham/total_votes)*100,2)
DeGette_percent = round((votes_DeGette/total_votes)*100,2)
Doane_percent = round((votes_Doane/total_votes)*100,2)

print("Election Results")
print("Total votes: ", total_votes)
print("Charles Casper Stockham: ", Stockham_percent, "%", "(",votes_Stockham, ")")
print("Diana DeGette: ", DeGette_percent, "%", "(",votes_DeGette, ")")
print("Raymon Anthony Doane: ", Doane_percent, "%", "(",votes_Doane, ")")
#print(key_winner)

#Output file
election_result_txt_file = Path("..", "PyPoll", "AnalysisPyPoll", "PyPoll_text_file_outputs.txt")

with open(election_result_txt_file, 'w') as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"-----------")
    file.write("\n")

    file.write(f"Total Votes: {total_votes}")
    file.write("\n")

    file.write(f"Charles Casper Stockham Votes: {Stockham_percent}% ({votes_Stockham})")
    file.write("\n")

    file.write(f"Diane DeGette Votes: {DeGette_percent}% ({votes_DeGette})")
    file.write("\n")

    file.write(f"Raymon Anthony Doane Votes: {Doane_percent}% ({votes_Doane})")
    file.write("\n")           

    file.write(f"The winner is:  {key_winner}")

