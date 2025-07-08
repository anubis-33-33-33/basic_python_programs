import random

def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score.
       0 will represent a Blackjack (two‑card 21)."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Handle Aces
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compare user and computer scores and return the result string."""
    if user_score == computer_score:
        return "Draw 🙃"
    if computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    if user_score == 0:
        return "Win with a Blackjack 😎"
    if user_score > 21:
        return "You went over. You lose 😭"
    if computer_score > 21:
        return "Opponent went over. You win 😁"
    if user_score > computer_score:
        return "You win! 🎉"
    return "You lose 😤"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Initial deal
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # Check for end‑game conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal_more = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_more == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn: must hit until score is 17 or more (unless Blackjack)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Main loop
while input("Do you want to play a game of Blackjack? Type 'y' to continue, 'n' to quit: ") == 'y':
    print("\n" * 20)
    play_game()
