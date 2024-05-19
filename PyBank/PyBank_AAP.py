
# read csv file
# create seperate list for col1 adn col2
# len of row[0]
# summation of row[1]
# delta of row[1]
# min, max aand average of above list

# Modules
import csv
import os

# Set path for file
csvpath = "Resources/budget_data.csv"
OUTPUT_PATH = "analysis/PyBank.txt"
#c = Counter()

get_date = list()
get_pl_data = []
change_pl = []
delta_pl = 0.0
delta_tot = 0.0
delta_avg = 0.0
delta_change = 0
change_pl.append(0)
tot = 0.0
i = 0
j = 0
k = 0
# # Set variable to check if we found the comic book
# user_state = input("Enter a State: ")
# is_found = False

# Open the CSV using the UTF-8 encoding
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#     # loop the CSV
    for row in csvreader:
        # do work
        # add date to list
        get_date.append(row[0])

        # add Profit loss to a row
        get_pl_data.append(float(row[1]))

    while i < len(get_pl_data):
        tot = tot + get_pl_data[i]
        i += 1
    while j < len(get_pl_data) - 1:
        delta_pl =  get_pl_data[j+1] - get_pl_data[j]
        change_pl.append(delta_pl)
        j += 1
    while k < len(change_pl):
        delta_tot = delta_tot + change_pl[k]
        k += 1
    delta_avg = delta_tot/(len(change_pl) - 1)
    max_delta = max(change_pl)
    min_delta = min(change_pl)

    # print(max(change_pl))
    # print(min(change_pl))
    # print(change_pl.index(max_delta))
    # print(change_pl.index(min_delta))

    # print(len(get_date))
    # print(tot)
    # # print(change_pl)
    # print(delta_avg)

    # print(f"Greatest Increase in Profits: {get_date[change_pl.index(max_delta)]} (${(max_delta)})")
    # print(f"Greatest decrease in Profits: {get_date[change_pl.index(min_delta)]} (${(min_delta)})")

    output = f"""----------------------------
Financial Analysis
----------------------------
Total Months: {len(get_date)}
Total: ${(tot)}
Average Change: $-8311.11
Greatest Increase in Profits: {get_date[change_pl.index(max_delta)]} (${(max_delta)})
Greatest Decrease in Profits: {get_date[change_pl.index(min_delta)]} (${(min_delta)})"""
    print(output)
    with (open(OUTPUT_PATH,'w')as f):
        f.write(output)

