import csv 
import os
budget_data = os.path.join("Resources", "budget_data.csv")
with open(budget_data) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter = ",")

#skip header (first) row
  csv_header = next(csv_reader)
  total_months = 0
  total_profit_loss = 0
  pl_change=[]
  month_change=[]
  
  avg_change= 0  
#   * The total number of months included in the dataset
  for row in csv_reader:
    total_months = total_months + 1
    total_change=[]  
    

#   * The net total amount of "Profit/Losses" over the entire period
    total_profit_loss += int(row[1])
    pl_change.append(int(row[1]))
    month_change.append(row[0])
    for i in range(1,len(pl_change)):
      total_change.append((pl_change[i])-(pl_change[i-1]))

#   * The average of the changes in "Profit/Losses" over the entire period
avg_change = round(sum(total_change)/len(total_change))

#   * The greatest increase in profits (date and amount) over the entire period
max_change=max(total_change)

#   * The greatest decrease in losses (date and amount) over the entire period
min_change=min(total_change)

#index the max and min change to find max and min month
max_month = total_change.index(max_change) + 1
min_month = total_change.index(min_change) + 1

analysis = ("Financial Analysis\n" 
"---------------------------------------------------------------------------\n"
f"Total Months: {total_months}\n"
f"Change Over Period: ${total_profit_loss}\n"
f"Average Change: ${avg_change}\n"
f"Greatest Increase in Profit: {month_change[max_month]} : ${max_change}\n"
f"Greatest Decrease in Profit: {month_change[min_month]} : ${min_change}")

financial_analysis = os.path.join("Analysis", "fin_analysis_output.txt")
with open(financial_analysis, "w") as txt_file: 
    txt_file.write(analysis)
