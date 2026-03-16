import random
import time
import string

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
    
    #Deduct one life only for a new wrong guess.
    new_lives = lives if clean_guess in clean_secret else max(0, lives - 1)
    
    return new_guessed_letters, new_lives

def get_random_word(word_list: list[str]) -> str:
    return random.choice(word_list).upper()

def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    clean_guessed = [letter.upper() for letter in guessed_letters]
    chars = [char if char in clean_guessed else "_" for char in secret_word]
    return " ".join(chars)

def check_win(secret_word: str, guessed_letters: list[str]) -> bool:
    clean_guessed = [letter.upper() for letter in guessed_letters]
    return all(char in clean_guessed for char in secret_word)

def check_loss(lives: int) -> bool:
    return lives <= 0

def play_single_round(word_list: list[str], auto_play: bool):
    secret_word = get_random_word(word_list)
    guessed_letters = []
    lives = 6
    game_active = True
    
    #Track unused letters so computer does not guess same letter twice
    available_letters = list(string.ascii_uppercase)
    
    mode_text = "Auto Play" if auto_play else "Manual"
    print(f"\nStarting the game of Guess The Word! ({mode_text} Mode)")
    
    # Constraint 1: No while True loop
    while game_active:
        masked = get_masked_word(secret_word, guessed_letters)
        print("\nWord: " + masked)
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Lives remaining: {lives}")
        
        if auto_play:
            # Computer selects randomly from letters it hasn't used yet
            guess = random.choice(available_letters)
            available_letters.remove(guess)
            print(f"Computer guesses: {guess}")
            time.sleep(1) # Add 1 second delay to see it play
        else:
            guess = input("Enter a single letter: ").strip()
        
        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)
        
        if check_win(secret_word, guessed_letters):
            print("\nWord: " + get_masked_word(secret_word, guessed_letters))
            print("Congrats! The word was guessed correctly!")
            game_active = False
            
        elif check_loss(lives):
            print(f"\nGame over! Secret word was {secret_word}.")
            game_active = False

def main():
    words = ["APPLE", "DOG", "CAT", "CUCUMBER", "COMPUTER", "PYTHON", "PROGRAMMING", "GIRAFFE", "ELEPHANT", "BANANA"]
    
    playing = True
    while playing:
        print("\n" + "="*30)
        print("Guess The Word - SELECT OPTIONS")
        print("P = Play Game")
        print("A = Auto Play Mode")
        print("Q = Quit")
        
        user_choice = input("Enter your choice (P/A/Q): ").strip().upper()
        
        if user_choice == "P":
            play_single_round(words, auto_play=False)
        elif user_choice == "A":
            play_single_round(words, auto_play=True)
        elif user_choice == "Q":
            playing = False
        else:
            print("Invalid choice. ONLY enter P, A, or Q.")         
    print("Thank you for playing!")

if __name__ == "__main__":
    main()