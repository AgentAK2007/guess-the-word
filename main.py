def update_game_state(secret_word: str, guessed_letters: list[str], guess: str, lives: int) -> tuple[list[str], int]:
    """Return updated guessed letters and lives after one letter guess.

    Rules enforced:
    - Only single alphabetic guesses are accepted.
    - Guess comparisons are case-insensitive.
    - Repeated guesses do not change state.
    - Lives never drop below zero.
    """

    if len(guess) != 1 or not guess.isalpha():
        return guessed_letters[:], lives
        
    clean_guess = guess.upper()
    clean_secret = secret_word.upper()
    clean_guessed = [letter.upper() for letter in guessed_letters]
    
    if clean_guess in clean_guessed:
        return guessed_letters[:], lives
        
    new_guessed_letters = guessed_letters + [clean_guess]
    
    # Deduct one life only for a new wrong guess.
    new_lives = lives if clean_guess in clean_secret else max(0, lives - 1)
    
    return new_guessed_letters, new_lives

import random

def get_random_word(word_list: list[str]) -> str:
    return random.choice(word_list).upper()

def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    # This uses a list comprehension instead of string replacement functions
    clean_guessed = [letter.upper() for letter in guessed_letters]
    chars = [char if char in clean_guessed else "_" for char in secret_word]
    return " ".join(chars)

def check_win(secret_word: str, guessed_letters: list[str]) -> bool:
    clean_guessed = [letter.upper() for letter in guessed_letters]
    return all(char in clean_guessed for char in secret_word)

def check_loss(lives: int) -> bool:
    return lives <= 0

def play_single_round(word_list: list[str]):
    secret_word = get_random_word(word_list)
    guessed_letters = []
    lives = 6
    game_active = True
    
    print("\nStarting the game of Guess The Word!")
    
    # Constraint 1: No while True loop
    while game_active:
        masked = get_masked_word(secret_word, guessed_letters)
        print("\nWord: " + masked)
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Lives remaining: {lives}")
        
        guess = input("Enter a single letter: ").strip()
        
        # Call your pure logic function
        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)
        
        if check_win(secret_word, guessed_letters):
            print("\nWord: " + get_masked_word(secret_word, guessed_letters))
            print("Congrats! You guessed the word correctly!")
            game_active = False
            
        elif check_loss(lives):
            print(f"\nGame over! The secret word was {secret_word}.")
            game_active = False

def main():
    words = ["Apple", "Dog", "Cat", "Cucumber", "Computer", "Python", "Programming", "Giraffe", "Elephant", "Banana"]
    
    play_again = "Y"
    while play_again == "Y":
        play_single_round(words)
        
        user_choice = input("\nWould you like to play again? (Y/N): ").strip().upper()
        if user_choice != "Y":
            play_again = "N"
            
    print("Thanks you for playing!")

if __name__ == "__main__":
    main()