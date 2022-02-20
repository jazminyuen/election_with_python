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

# Initialize variable to count votes
total_votes = 0
# Initialize a list for candidates
candidate_options = []
# Initialize dictionary to count votes by candidate
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read it
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header row to skip it
    headers = next(file_reader)
    print(headers)
    # Print each row
    for row in file_reader:
        total_votes += 1
        print(total_votes)
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add candidate name to the candidate_options list
            candidate_options.append(candidate_name)
            # Set initial candidate's vote count to 0
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Get the percentage of votes for each candidate
# 1. Iterate through the candidate list to get the candidate's name
for candidate_name in candidate_votes:
    # 2. Get the candidate votes from the candidate_votes dictionary
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of the vote count
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print out each candidate's stats
    print(f'{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n')
    # Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
# Print winning candidate's stats
winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"-----------------------\n")
print(winning_candidate_summary)


