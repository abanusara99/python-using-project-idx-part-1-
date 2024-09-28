# Create a dictionary
person = {
    'name': 'Anu',
    'age': 20,
    'city': 'Bangalore'
}

# Access values
print("\n")
print("Access elements")
print(person['name'])  
print(person['age'])  

# Add a new key-value pair
print("\n")
print("Add a new key-value pair")
person['email'] = 'abanusara@example.com'
print(person)  

# Update an existing value
print("\n")
print("update an existing value")
person['age'] = 30
print(person)  

# Remove a key-value pair
print("\n")
print("remove a ket-value pair")
del person['city']
print(person)  

# Check membership
print("\n")
print("Check membership")
if 'name' in person:
    print("Name is present in the dictionary")  

# Iterate over keys and values
print("\n")
print("Iterate over keys and values")
for key, value in person.items():
    print(f"{key}: {value}")
