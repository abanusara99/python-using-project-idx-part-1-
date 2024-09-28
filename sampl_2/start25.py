# Create a set
# normal
flying_machines = {'airplane', 'helicopter', 'drone'}

print("\n")
# Add an element
print("Add an element")
flying_machines.add('glider')
print(flying_machines)

print("\n")
# Remove an element
print("remove an element")
flying_machines.remove('helicopter')
print(flying_machines)

print("\n ")
# Get the length of the set
print("size of elements")
print(len(flying_machines)) 

print("\n Check membership ")
# Check membership
if 'airplane' in flying_machines:
    print("Airplane is in the set")  

print("\n Iterate over elements")
# Iterate over elements
for machine in flying_machines:
    print(machine)

print("\n")
# Set operations
print("set operations")
more_machines = {'glider', 'hot air balloon'}
all_machines = flying_machines.union(more_machines)
print(all_machines)
