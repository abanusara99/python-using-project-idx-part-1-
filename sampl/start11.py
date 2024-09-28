# Nested if statements
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
    height = float(input("Enter your height (in meters): "))
    if height >= 1.8:
        print("You are tall.")
    elif height >= 1.5:
        print("You have an average height.")
    else:
        print("You are short.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")