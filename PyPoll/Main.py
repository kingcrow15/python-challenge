import os
import csv
from datetime import datetime
from dateutil import relativedelta
from collections import defaultdict

election_file_path = os.path.join(os.path.expanduser("~"), "Documents", "GitHub", "python-challenge", "PyPoll", "Resources", "election_data.csv")


def get_election_stats(file_path):
    with open(file_path) as csvfile:
        rows = csv.reader(csvfile)
        count = 0
        candidates = defaultdict(int)

        for voter_id, county, candidate in rows:
            if voter_id == "Voter ID":
                continue
            count += 1
            candidates[candidate] += 1

        print("Total votes cast: {}".format(count))
        print("List of candidates: {}".format(candidates.keys()))
        print("Votes for each candidate: {}".format(candidates.items()))
        percents = {candidate: str(100 * votes / count) for candidate, votes in candidates.items()}
        print("Percetage votes for each candidate: {}".format(percents.items()))
        most_votes = max([votes for votes in candidates.values()])
        for candidate, votes in candidates.items():
            if votes == most_votes:
                print("Winner: {}".format(candidate))


get_election_stats(election_file_path)