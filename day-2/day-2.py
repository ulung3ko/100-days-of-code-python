# Subscripting
# Display last character with negative number indexing
print("Hello"[-1])

# String
print("123" + "345") # Concatenation

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

# Fix the TypeError
len("12345")

# Check any data types use type() function
print(type(123))

# Type check for 4 data types
print(type("Eko"))
print(type(123))
print(type(123.456))
print(type(True ))

# Type conversion
print(int("123") + int("456"))

# Task - Solution of the task (with variables and type check)
#username = input("Enter your name\n")
#length_Of_username = len(username)

#print(type("Number of letters in your name: ")) #str
#print(type(length_Of_username))

#print("Number of letters in your name: " + str(length_Of_username))

# Mathematical Operations
# Addition
print(123 + 456)
# Subtraction
print(7 - 3)
# Multiplication
print(3 * 2)
# Dvision
print(6 / 3) # The result is float
print(5 / 3) # The result is float
print(6 // 3) # The result is integer (remove decimal)
print(5 // 3) # The result is integer (remove decimal)
# Exponents
print(2 ** 2)

# PEMDAS LR (Lef-Right)
# ()
# **
# * OR /
# + OR -

# How to the result of this code is 3
print(3 * (3 + 3) / 3 - 3)

# BMI
bmi = 84 / 1.65 ** 2

print(bmi)

# Converting bmi into integer
print(int(bmi))

# Remove decimal using round() function
print(round(bmi))

# round() function with ndigits
print(round(bmi, 2))

# Assignment Operator

score = 0
score += 1
print(score)

score = 0
score -= 1
print(score)

# f-strings
score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}.")
