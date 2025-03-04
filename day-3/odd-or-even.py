# Check Odd or Even of the input number
number = int(input("Input the number\n"))
modulo = number % 2

# Conditional statement with modulo operator
if modulo == 0:
    print("The number is even.")
else:
    print("The number is odd.")
