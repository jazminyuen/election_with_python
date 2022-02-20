# The data I need to retrieve
# 1. Total number of votes cast
# 2. Complete list of candidates that received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. Winner of election based on popular vote

# Modules
import os
import csv
# Assign a variable for the csv filepath
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable for the txt filepath
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results
with open(file_to_load) as election_data:
    # Read and analyze data
    csvreader = csv.reader(election_data)
    headers = next(csvreader)
    print(headers)