import csv

# Set the path and output for the budget_data.csv file
budget_path = "C:/Users/fishm/Documents/UT Bootcamp/HW3/python-challenge/PyBank/Resources/budget_data.csv"
budget_output = "budget_results.txt"

# Set the path and output for the election_data.csv file
election_path = "C:/Users/fishm/Documents/UT Bootcamp/HW3/python-challenge/PyPoll/Resources/election_data.csv"
election_output = "election_results.txt"

# Initialize budget data variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Initialize election data variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

#------------------------------------------------------------------------------ Budget Data Portion ---------------------------------------------------------------------------------------
# Read the budget_data.csv file
with open(budget_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Skips header row

    # Iterate through the rows in the CSV file
    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the total profit/loss
        total_profit_loss += int(row[1])

        # Calculate the change in profit/loss from the previous month
        current_profit_loss = int(row[1])
        if total_months > 1:
            profit_loss_change = current_profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)

            # Track the greatest increase and decrease in profits
            if profit_loss_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_loss_change
            if profit_loss_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_loss_change

        previous_profit_loss = current_profit_loss

# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

with open(budget_output, "w") as file:
# Print the analysis results
    file.write("Financial Analysis\n")
    file.write("-----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(f"Budget results exported to {budget_output}")


#------------------------------------------------------------------------------ Election Data Portion ---------------------------------------------------------------------------------------
# Read the election_data.csv file
with open(election_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Skip the header row

    # Iterate through the rows in the CSV file
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1

        # Get the candidate from the row
        candidate = row[2]

        # Update the vote count for the candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Open the output file in write mode
with open(election_output, "w") as file:
    # Write the analysis results to the file
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    # Calculate and write the results for each candidate
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        # Check if the current candidate has more votes than the previous maximum
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

# Print a message indicating the export was successful
print(f"Election results exported to {election_output}")

