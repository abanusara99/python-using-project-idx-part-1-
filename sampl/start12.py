#Determine if a number is even or odd using the ternary operator

# Prompt user for input
number = int(input("Enter a number: "))

# Using the ternary operator to check if the number is even or odd
result = "Even" if number % 2 == 0 else "Odd"

# Print the result
print(f"The number {number} is {result}.")