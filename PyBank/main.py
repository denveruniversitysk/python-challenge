import csv
import os

# Loading data and outputting analysis
loadedData = os.path.join("Resources", "budget_data.csv")
outputFile = os.path.join("analysis", "output.txt")

# Initializing variables
numberMonths = 0
netTotal = 0
pre_net = 0
ave_change = 0
monthly_change_list = []
increase_profit = ["", 0]
decrease_profit = ["", 9999999999999999999]

with open(loadedData) as budget_data:
    csvreader = csv.reader(budget_data)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    first_row = next(csvreader)
    numberMonths += 1
    netTotal += int(first_row[1])
    pre_net = int(first_row[1])

    # Beginning For Loop
    for row in csvreader:    
        monthly_pnl = int(row[1])
        numberMonths += 1
        netTotal += monthly_pnl
        net_change = monthly_pnl - pre_net
        pre_net = monthly_pnl
        monthly_change_list += [net_change]

        # Calculating greatest increase in profits
        if net_change > increase_profit[1]:
            increase_profit[0] = row[0]
            increase_profit[1] = net_change
            
        # Calculating greatest decrease in profits    
        if net_change < decrease_profit[1]:
            decrease_profit[0] = row[0]
            decrease_profit[1] = net_change

# Calculating average change
ave_change = sum(monthly_change_list)/len(monthly_change_list)

# Printing analysis and exporting text file
with open(outputFile, 'w') as results_file:
    financial_results = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {numberMonths}\n"
        f"Total: ${netTotal}\n"
        f"Average Change: ${ave_change:.2f}\n"
        f"Greatest Increase in Profits: {increase_profit[0]} (${increase_profit[1]})\n"
        f"Greatest Decrease in Profits: {decrease_profit[0]} (${decrease_profit[1]})"
        )

    print(financial_results)
    results_file.write(financial_results)