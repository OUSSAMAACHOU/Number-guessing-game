import random

def Number_Guessing_Game():
    # Difficulty level selection
    print("Select Difficulty Level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    while True:
        try:
            difficulty = int(input("Enter the difficulty level (1/2/3): "))
            if difficulty in [1, 2, 3]:
                break
            else:
                print("Please enter 1, 2, or 3")
        except ValueError:
            print("Invalid input. Please enter a number (1/2/3)")

    # Set range based on difficulty
    if difficulty == 1:
        max_range = 50
    elif difficulty == 2:
        max_range = 100
    else:
        max_range = 200

    # Generate random number
    random_number = random.randint(1, max_range)
    
    # Game loop
    attempts = 0
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {max_range}: "))
            if guess < 1 or guess > max_range:
                print(f"Please enter a number between 1 and {max_range}")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number")
            continue
        
        attempts += 1
        
        if guess < random_number:
            print("Too low! Try again")
        elif guess > random_number:
            print("Too high! Try again")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

# Run the game
if __name__ == "__main__":
    Number_Guessing_Game()
