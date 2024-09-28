#switch
def se(option):
    # Simulating switch-case using if-elif statements
    if option == 1:
        print("You selected option 1: Start")
    elif option == 2:
        print("You selected option 2: Stop")
    elif option == 3:
        print("You selected option 3: Pause")
    elif option == 4:
        print("You selected option 4: Exit")
    else:
        print("Invalid option")
        return  # This acts like a continue by skipping further processing

# Assigned values for demonstration
assigned_values = [1, 2, 3, 4, 5]  # List of assigned values to test

# Example usage with assigned values
for user_choice in assigned_values:
    print(f"Testing with input: {user_choice}")
    se(user_choice)  # Call the function with each assigned value

# it won't work     