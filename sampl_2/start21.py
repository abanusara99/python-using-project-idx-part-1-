# Create a list, a mutable
numbers = [1, 2, 3, 4, 5]

# Access elements
print("Access elements")
print(numbers[0])   
print(numbers[-1])  

# Modify an element
print("Modify elements") 
numbers[2] = 10
print(numbers)     

# Add elements
print("Add elements")
numbers.append(6)
numbers.insert(2, 7)
print(numbers)     

# Remove elements 
print("remove elements")
numbers.remove(10)
del numbers[2]
print(numbers)     

# Concatenate lists
print("Concatenate lists")
more_numbers = [7, 8, 9]
all_numbers = numbers + more_numbers
print(all_numbers)  

# Iterate over elements
print("Iterate over elements")
for num in numbers:
    print(num)