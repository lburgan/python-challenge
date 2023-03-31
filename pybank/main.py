
import os 
import csv

#initialize all variables we will be using 
total_months = 0
total_budget = 0
changes = []
dates = []

#read the budget csv into python 
budgets_path = os.path.join("Resources","budget_data.csv")
with open(budgets_path, "r") as budgets_csv:
    budgets = csv.reader(budgets_csv, delimiter= ",")
#store the header
    header = next(budgets)
    print(header)
    
#store first row so we can initialize comparison value 
    first_row = next(budgets)
    total_months += 1
    total_budget = total_budget + int(first_row[1])
    compare = int(first_row[1])

#loop through the rows tracking changes 
    for row in budgets:

        #add to the total months
        total_months += 1

        #add to the total budget
        total_budget = total_budget + int(row[1])

        #add current date to dates list
        dates.append(row[0])

        #find the change from this month to last 
        change = int(row[1]) - compare

        #add the change to the change list 
        changes.append(change)

        #set current value as comparison for next iteration
        change = int(row[1])
    
#find the max increase
max_increase = max(changes)

#find the max decrease (AKA the minimum lol)
max_decrease = min(changes)

#find the months that match max and min values 
max_index = changes.index(max_increase)
max_month = dates[max_index]

min_index = changes.index(max_decrease)
min_month = dates[min_index]


#find average change 
total_changes = sum(changes)
avg_change = total_changes / len(changes)

print("Financial Analysis\n----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_budget}')
print(f'Average Change: ${round(avg_change)}')
print(f'Greatest Increase in Profits: {max_month}  ${max_increase}')
print(f'Greatest Decrease in Profits: {min_month}  ${max_decrease}')


#export to a .txt file 
output_path = os.path.join("Resources", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as new_txt:
    new_txt.write("Financial Analysis\n----------------------------\n")
    new_txt.write(str(f'Total Months: {total_months}\n'))
    new_txt.write(str(f'Total: ${total_budget}\n'))
    new_txt.write(str(f'Average Change: ${round(avg_change)}\n'))
    new_txt.write(str(f'Greatest Increase in Profits: {max_month}  ${max_increase}\n'))
    new_txt.write(str(f'Greatest Decrease in Profits: {min_month}  ${max_decrease}\n'))