# removing duplicates and adding '*' instead
arr = [1, 2, 2, 3, 4, 4, 5]
seen = set()
new_arr = []

for num in arr:
    if num in seen:
        new_arr.append('*')  # Replace duplicate with '*'
    else:
        new_arr.append(num)
        seen.add(num)
print("\n")
print(new_arr) 
print("\n")
