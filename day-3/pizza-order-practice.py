print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price = 0
# Check size's order and pepperoni
if size == "S":
    price = 15
    if pepperoni == "Y":
        price += 2
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price += 3
else:
    price = 25
    if pepperoni == "Y":
        price += 3

# Check for extra cheese
if extra_cheese == "Y":
    price += 1

# Print final bill
print(f"Your final bill is: ${price}.")
