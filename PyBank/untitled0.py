#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:21:21 2021

@author: servontius
"""

# Import module to work with csv files
import csv
import numpy as np

# Declare variables to hold the input file, total months in the file, total profit/loss and max increase/decrease
input_path = "PyBank/Resources/budget_data.csv"
total_months = 0
net_profit_loss = 0
max_increase = 0
max_decrease = 0
counter = 0
previous_month = 0
current_month = 0

# Declare empty list to hold data within csv file
budget = []

# Open the CSV file to manipulate the data
with open(input_path, "r") as budgetfile:

    # Read the file and append the header information to the budget list
    budgetreader = csv.reader(budgetfile, delimiter=",")
    header = next(budgetreader)
    budget.append(header)

    # Iterate through each row of the file and convert the numeric values to int for maths
    for row in budgetreader:
        date = row[0]
        profit_loss = int(row[1])

        # Add the row to the Budget full budget List
        budget.append(row)

        # Increase the count of total months in the file
        total_months += 1

        # Calculate the total Net Profit/Loss
        net_profit_loss += profit_loss

        """Create a loop that checks the current value against the previous value and
            store it in a variable so that the increase and decrease in profits can be calculated."""

budget.pop(0)

for num in budget:
    if counter == 0:
        previous_month = int(num[1])
        counter = 1
    elif counter == 1:
        current_month = int(num[1])
        counter = 2
    elif counter == 2:
        max_increase = (current_month - previous_month)
        previous_month = 0
        current_month = 0
        counter = 0


print(previous_month)
print(current_month)
print(max_increase)
average_change = round(profit_loss / total_months)

'''print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_profit_loss}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {max_increase}")
print(f"Greatest Decrease in Profits: {max_decrease}")'''