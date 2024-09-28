# Create two sets
# maths
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)
print("\n")
print("Union:", union_set)  

# Intersection
intersection_set = set1.intersection(set2)
print("\n")
print("Intersection:", intersection_set)  

# Difference (set1 - set2)
diff1 = set1.difference(set2)
print("\n")
print("Difference (set1 - set2):", diff1)  
# Difference (set2 - set1) 
diff2 = set2.difference(set1)
print("\n")
print("Difference (set2 - set1):", diff2)  

# Symmetric Difference
symmetric_diff = set1.symmetric_difference(set2)
print("\n")
print("Symmetric Difference:", symmetric_diff)  