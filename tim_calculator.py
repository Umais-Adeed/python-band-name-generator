# Initial Setup and User Prompts
print("Welcome to the Tip Calculator")
total = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Tip Calculation
inc = percentage / 100
per = total * inc
bill_total = total + per
