# Initial Setup and User Prompts
print("Welcome to the Tip Calculator")
total = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Tip Calculation
inc = percentage / 100
per = total * inc
bill_total = total + per

# Splitting the Bill
people = int(input("How many people to split the bill? "))
tot = bill_total / people

# Rounding and Final Calculation
div = round(tot, 2)  # Rounded calculation
final_result = "{:.2f}".format(tot)  # Formatted result

# Output the Results
print(f"Each person should pay: {div} and the total bill with tip is: {bill_total}")
print(f"Formatted final result: {final_result}")
