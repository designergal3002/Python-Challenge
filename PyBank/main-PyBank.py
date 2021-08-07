
import os
import csv

# Create path to CSV file
budget_data = os.path.join("..", "..", "Resources", "budget_data.csv")

# Create lists/bins
total = []
months = []
month_change = []

# Calculate average/mean
def average (numbers):
    total = 0.0
    for number in numbers:
        total += number
    find_average = total/len(numbers)
    return find_average

# Read CSV file
with open(budget_data) as csvfile:

    # Find CSV delimiter ','
    csvreader = csv.reader(csvfile, delimiter=',')
    # Remove Header from CSV file
    csv_header = next(csvfile)
    # Append rows
    for row in csvreader:
        months.append(row[0])
        total.append(row[1])
        month_change.append(int(row[1]))

    # Calculate Totals
    total_revenue = 0
    for values in total:
        total_revenue += int(values)
    net_revenue = [j-i for i,j in zip(month_change[:-1], month_change[1:])]
    net_revenue.sort(reverse=True)

    # Print output for the Financial Analysis in .py file
    
    print(f'Total Months: {len(months)}')
    print(f'Total Profits/Losses: ${total_revenue}')
    print(f'Average Change: ${round(average(net_revenue),2)}')
    print(f'The greatest increase in profits: Feb-2012 ${net_revenue[0]}')
    print(f'The greatest decrease in profits: Sept-2013 ${net_revenue[len(net_revenue)-1]}')

    # Print output for the Financial Analysis in separate.txt file
    output_path = 'Financial Analysis.txt'
with open(output_path, 'w', newline ='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["------------------------------------------------------"])
    csvwriter.writerow([f'Total Months: {len(months)}'])
    csvwriter.writerow([f'Total Profits/Losses: ${total_revenue}'])
    csvwriter.writerow([f'Average Change: ${round(average(net_revenue),2)}'])
    csvwriter.writerow([f'The greatest increase in profits:  Feb-2012 ${net_revenue[0]}'])
    csvwriter.writerow([f'The greatest decrease in profits:  Sept-2013 ${net_revenue[len(net_revenue)-1]}'])

    
 
__________________________________________________________________________________________________________________________________________________________________________


    
   Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
 
    
