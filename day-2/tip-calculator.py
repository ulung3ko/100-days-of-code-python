# Tip Calculator Project
# This Program
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
peoples = input("How many people to split the bill? ")

total_bill = int(total_bill)
tip = int(tip)
peoples = int(peoples)

bill_with_tip = total_bill + (total_bill * (tip /100))
result = bill_with_tip / peoples
print(f"Each person should pay: {round(result, 2)}")
