print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price = 0
# Check size's order
if size == "S":
    price = 15
elif size == "M":
    price = 20
else:
    price = 25

# Check for pepperoni
if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

# Check for extra cheese
if extra_cheese == "Y":
    price += 1

# Print final bill
print(f"Your final bill is: ${price}.")
