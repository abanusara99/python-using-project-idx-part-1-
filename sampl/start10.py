#switch
def sle(option):
    # Simulating switch-case using if-elif statements
    if option == 1:
        print("You selected option 1: Yes")
    elif option == 2:
        print("You selected option 2: No")
    elif option == 3:
        print("You selected option 3: Reset")
    elif option == 4:
        print("You selected option 4: LOL")
    else:
        print("Invalid option")
        return  # This acts like a continue by skipping further processing

# Example usage
try:
    user_choice = int(input("Enter a number (1-4): "))  # Prompt for user input
    sle(user_choice)  # Call the function with user input
except ValueError:
    print("Please enter a valid integer.")