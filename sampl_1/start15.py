#break and continue
# List of numbers to iterate through
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate through the list of numbers
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    
    # Check if the number is 7
    if number == 7:
        print("Encountered 7! Exiting the loop.")
        break  # Exit the loop when we encounter 7
    
    # Print the odd number
    print(number)