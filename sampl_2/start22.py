# Create a tuple, a immutable
fruits = ('apple', 'banana', 'cherry')

# Access elements
print("\n")
print("Access elements")
print(fruits[0])   
print(fruits[-1])  

# Concatenate tuples
print("\n")
print("Concatenate tuples")
more_fruits = ('orange', 'grape')
all_fruits = fruits + more_fruits
print(all_fruits)  

# Repeat a tuple
print("\n")
print("Repeat a tuple")
repeated_fruits = fruits * 3
print(repeated_fruits)  

# Check membership
print("\n")
print("Check membership")
if 'banana' in fruits:
    print("Banana is in the tuple")  
    
# Iterate over elements
print("\n")
print("Iterate over elements")
for fruit in fruits:
    print(fruit)