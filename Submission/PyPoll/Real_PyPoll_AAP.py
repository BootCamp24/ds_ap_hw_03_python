# read csv file
# create seperate list for col1 adn col2
# len of row[0]
# summation of row[1]
# delta of row[1]
# min, max aand average of above list

# Modules
import csv

# Set path for file
csvpath = "Starter_Code\PyPoll\Resources\election_data.csv"
#c = Counter()

get_ballot = list()
get_candidate = []
candidate_col = []
count_list =[]
i = 0
count1 = 0


# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # loop the CSV
    for row in csvreader:
        # do work
        # get Voters count
        get_ballot.append(row[0])
        candidate_col.append(row[2])
        candidate_name = row[2]
        # list of candidates
        if candidate_name not in get_candidate:
            get_candidate.append(row[2])
    # total number of votes
    for names in get_candidate:
        count1 = candidate_col.count(names)
        count_list.append(count1)
    # max vote and name of the Candidate
    max_vote = max(count_list)
    indx = int(count_list.index(max_vote))
    # print("----------------------------------")
    # print(f"Total Votes: {len(get_ballot)}")
    # print("----------------------------------")
    # output file
    output = f"""Election Results
-------------------------
Total Votes: {len(get_ballot)}
-------------------------\n"""

    print(f"List of the Candidates : {get_candidate}")
    for i in range(3):
        names = get_candidate[i]
        # print(f"{names}: {round(count_list[i]/len(get_ballot)*100,3)} ({count_list[i]})")
        line = f"{names}: {round(count_list[i]/len(get_ballot)*100,3)}% ({count_list[i]})\n"
        output += line
    # print("----------------------------------")  
    # print(f"Winner : {get_candidate[indx]}")
    # print("----------------------------------")

    last_line = f""" -------------------------
Winner : {get_candidate[indx]}
-------------------------\n"""
    output += last_line
    print(output)
    with (open("output_PyPoll.txt",'w')as f):
        f.write(output)
       

    
            





    


