print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# If Else (Conditional Statement)
if height >= 120: # Greater than or equal to comparison operator
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay %5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
