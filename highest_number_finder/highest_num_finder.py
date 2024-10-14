# Ask the user to input 5 numbers separately
number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))
number3 = float(input("Please enter the third number: "))
number4 = float(input("Please enter the fourth number: "))
number5 = float(input("Please enter the fifth number: "))

# Set a variable as the highest number
highest_num = number1 # Set highest_num to number1

# Use if statements to find the highest number
if number2 > highest_num: # If number2 is greater than highest_num
    highest_num = number2 # Update highest_num to number2

if number3 > highest_num: # If number3 is greater than highest_num
    highest_num = number3 # Update highest_num to number3

if number4 > highest_num: # If number4 is greater than highest_num
    highest_num = number4 # Update highest_num to number4

if number5 > highest_num: # If number5 is greater than highest_num
    highest_num = number5 # Update highest_num to number5

# Print the highest number