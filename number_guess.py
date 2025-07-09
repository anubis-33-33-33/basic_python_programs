import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess: int, answer: int) -> bool:
    """Check the user's guess against the answer, print feedback, and return True if correct."""
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"🎉 You got it! The answer was {answer}.")
        return True
    return False

def get_difficulty() -> int:
    """Prompt the user to choose a difficulty level and return the number of turns."""
    while True:
        choice = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if choice == "easy":
            return EASY_LEVEL_TURNS
        elif choice == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid choice. Please enter 'easy' or 'hard'.")

def game():
    """Main game function."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = get_difficulty()

    while turns > 0:
        print(f"\nYou have {turns} turn{'s' if turns != 1 else ''} remaining.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        if check_answer(guess, answer):
            break

        turns -= 1
        if turns == 0:
            print(f"\n😢 You've run out of guesses. The number was {answer}. Better luck next time!")

if __name__ == "__main__":
    game()
