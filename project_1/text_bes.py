# Text-based Adventure Game: The Quest for the Lost Treasure

def start_game():
    print("Welcome to 'The Quest for the Lost Treasure'!")
    print("You are on an adventure to find the lost treasure.")
    first_choice()

def first_choice():
    print("\nYou find yourself at a crossroads in a dark forest.")
    print("Do you want to go left towards the river or right towards the mountains?")
    
    choice = input("Type 'left' or 'right': ").lower()
    
    if choice == 'left':
        river_path()
    elif choice == 'right':
        mountain_path()
    else:
        print("Invalid choice. Please try again.")
        first_choice()

def river_path():
    print("\nYou arrive at a beautiful river.")
    print("You can either swim across or walk along the riverbank.")
    
    choice = input("Type 'swim' or 'walk': ").lower()
    
    if choice == 'swim':
        swim_across()
    elif choice == 'walk':
        walk_riverbank()
    else:
        print("Invalid choice. Please try again.")
        river_path()

def mountain_path():
    print("\nYou reach the base of a steep mountain.")
    print("Do you want to climb the mountain or explore a cave?")
    
    choice = input("Type 'climb' or 'explore': ").lower()
    
    if choice == 'climb':
        climb_mountain()
    elif choice == 'explore':
        explore_cave()
    else:
        print("Invalid choice. Please try again.")
        mountain_path()

def swim_across():
    print("\nYou bravely swim across the river but get swept away by the current!")
    print("Unfortunately, you have drowned. Game over!")
    
def walk_riverbank():
    print("\nAs you walk along the riverbank, you find a hidden treasure chest!")
    print("Congratulations! You've found the lost treasure! You win!")

def climb_mountain():
    print("\nYou climb the mountain and reach a breathtaking view.")
    print("However, you encounter a fierce dragon!")
    
    choice = input("Do you want to fight the dragon or run away? (type 'fight' or 'run'): ").lower()
    
    if choice == 'fight':
        print("\nYou bravely fight the dragon but it defeats you. Game over!")
    elif choice == 'run':
        print("\nYou successfully escape but get lost in the mountains. Game over!")
    else:
        print("Invalid choice. Please try again.")
        climb_mountain()

def explore_cave():
    print("\nInside the cave, you find ancient drawings and a mysterious potion.")
    
    choice = input("Do you want to drink the potion or leave it? (type 'drink' or 'leave'): ").lower()
    
    if choice == 'drink':
        print("\nThe potion gives you magical powers! You can now find your way out of the cave safely.")
        print("Congratulations! You've found your way back home with stories to tell!")
    elif choice == 'leave':
        print("\nYou leave the cave and get lost in the forest. Game over!")
    else:
        print("Invalid choice. Please try again.")
        explore_cave()

# Start the game
start_game()