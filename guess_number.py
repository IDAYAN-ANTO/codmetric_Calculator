import random

def get_valid_number(prompt):
    """Validate integer input"""
    while True:
        user_input = input(prompt)
        if user_input.lower() == "exit":
            return None
        try:
            return int(user_input)
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def number_guessing_game():
    print("\n🎮 Welcome to the Number Guessing Game!")
    print("Try to guess the secret number between 1 and 100.")
    print("Type 'exit' anytime to quit.\n")

    # Difficulty selection
    difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
    if difficulty == "easy":
        max_attempts = 15
    elif difficulty == "medium":
        max_attempts = 10
    elif difficulty == "hard":
        max_attempts = 5
    else:
        print("⚠️ Invalid choice. Defaulting to Medium difficulty (10 attempts).")
        max_attempts = 10

    secret_number = random.randint(1, 100)
    attempts = 0
    guesses = []  # to store previous guesses

    while attempts < max_attempts:
        guess = get_valid_number(f"\nAttempt {attempts+1}/{max_attempts} - Enter your guess: ")
        if guess is None:
            print("👋 Game exited. Goodbye!")
            return

        attempts += 1
        guesses.append(guess)

        if guess < secret_number:
            print("⬇️ Too low!")
        elif guess > secret_number:
            print("⬆️ Too high!")
        else:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} correctly!")
            print(f"✅ Total attempts: {attempts}")
            print(f"📌 Your guesses: {guesses}")
            break
    else:
        print(f"\n❌ Out of attempts! The number was {secret_number}.")
        print(f"📌 Your guesses: {guesses}")

# Run the game
number_guessing_game()
