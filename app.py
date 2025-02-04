import random  # Importing the random module

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0  # Counter to track the number of guesses
    
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        try:
            # Take user input and convert it to an integer
            guess = int(input("\nEnter your guess: "))
            attempts += 1  # Increase attempt count

            # Check if the guess is correct
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit loop if guessed correctly

            # Give hints to the player
            elif guess < secret_number:
                print("📉 Too low! Try again.")
            else:
                print("📈 Too high! Try again.")
        
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

# Main loop to allow replaying
while True:
    play_game()  # Start the game
    
    # Ask user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("Thanks for playing! 🎮")
        break  # Exit the game
