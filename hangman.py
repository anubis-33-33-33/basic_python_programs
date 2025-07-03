import random
import string

HANGMAN_STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    r"""
  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
=========
"""
]

WORD_LIST = [
    'aardvark', 'baboon', 'camel', 'donkey', 'elephant',
    'fossil', 'giraffe', 'hippo', 'iguana', 'jaguar',
    'kangaroo', 'lemur', 'mongoose', 'narwhal', 'ostrich',
    'penguin', 'quokka', 'raccoon', 'salamander', 'tortoise',
    'urchin', 'vulture', 'walrus', 'xenops', 'yak', 'zebra'
]

MAX_LIVES = len(HANGMAN_STAGES) - 1


def choose_word(word_list):
    """Randomly pick and return a word from the list."""
    return random.choice(word_list)


def display_state(lives, correct_positions, guessed_letters):
    """Print the current hangman stage, the word with blanks, and guessed letters."""
    print(HANGMAN_STAGES[MAX_LIVES - lives])
    print("Word: ", " ".join(correct_positions))
    print(f"Lives remaining: {lives}")
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print()


def get_guess(already_guessed):
    """Prompt for a single-letter guess, validating input."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("  → Please enter a single letter (a–z).")
        elif guess in already_guessed:
            print(f"  → You already guessed '{guess}'. Try another.")
        else:
            return guess


def update_correct_positions(word, correct_positions, guess):
    """Reveal positions of `guess` in the word."""
    for idx, letter in enumerate(word):
        if letter == guess:
            correct_positions[idx] = guess


def play_hangman():
    word = choose_word(WORD_LIST)
    lives = MAX_LIVES
    guessed_letters = set()
    correct_positions = ["_"] * len(word)

    print("Welcome to Hangman!")
    # Uncomment next line to see the word (for debugging)
    # print(f"(DEBUG) The word is: {word}\n")

    while lives > 0 and "_" in correct_positions:
        display_state(lives, correct_positions, guessed_letters)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            update_correct_positions(word, correct_positions, guess)
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            lives -= 1
            print(f"❌ Sorry, '{guess}' is not in the word.\n")

    # Final state
    display_state(lives, correct_positions, guessed_letters)

    if "_" not in correct_positions:
        print(f"🎉 You win! The word was '{word}'.")
    else:
        print(f"💀 You lose... The word was '{word}'.")


if __name__ == "__main__":
    play_hangman()
