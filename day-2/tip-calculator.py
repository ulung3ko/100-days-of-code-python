# Tip Calculator Project
# This Program will calculate the amount of money each person has to pay.
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $")) #Float is more accurate for bill
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
peoples = int(input("How many people to split the bill? "))

bill_with_tip = total_bill + (total_bill * (tip /100))
result = bill_with_tip / peoples
print(f"Each person should pay: ${round(result, 2)}")
